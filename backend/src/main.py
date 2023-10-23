from fastapi_users import FastAPIUsers

from fastapi import FastAPI, Depends, HTTPException

from src.auth.auth import auth_backend
from src.database import User
from src.auth.manager import get_user_manager
from src.auth.schemas import UserRead, UserCreate

from src.product.routers import router as router_product
from src.product.routers import seller_product_router, seller_products_size_router, photo_router, brand_router, \
    router_only_read_all
from src.basket.routers import product_basket_router, address_router, discount_coupon_router, check_router
from src.reviews.routers import review_router

from src.auth.schemas import UserUpdate
from starlette import status

from src.auth.exceptions import UserNotFound
from src.auth.manager import UserManager

app = FastAPI(
    title="Trading App"
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"


@app.patch("/update-user/{user_id}", response_model=UserRead, tags=["auth"])
async def update_user(
        user_id: int,
        user_update: UserUpdate,
        user_manager=Depends(get_user_manager),
):
    try:
        updated_user = await user_manager.update(user_id, user_update)
        return updated_user
    except HTTPException as e:
        return e


@app.put("/update-password/{user_id}", tags=["auth"])
async def update_user_password(
        user_id: int,
        current_password: str,
        new_password: str,
        user_manager: UserManager = Depends(get_user_manager)
):
    try:
        updated_user = await user_manager.update_password(
            user_id, current_password, new_password
        )
        return updated_user
    except UserNotFound as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except HTTPException as e:
        raise e


app.include_router(router_product)
app.include_router(seller_product_router)
app.include_router(seller_products_size_router)
app.include_router(photo_router)
app.include_router(brand_router)
app.include_router(product_basket_router)
app.include_router(address_router)
app.include_router(discount_coupon_router)
app.include_router(review_router)
app.include_router(check_router)
app.include_router(router_only_read_all)
