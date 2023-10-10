from typing import Optional
import re
from fastapi import Depends, Request, HTTPException
from fastapi_users import BaseUserManager, IntegerIDMixin, models, schemas

from src.database import User, get_user_db

from src.auth.schemas import UserUpdate

from src.auth.schemas import UserCreate

from src.auth.exceptions import PasswordTooShort, UserNotFound, UserAlreadyExists

SECRET = "SECRET"


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def create(
            self,
            user_create: UserCreate,
            safe: bool = False,
            request: Optional[Request] = None,
    ) -> models.UP:
        await self.validate_password(user_create.password, user_create)

        if not self.is_valid_email(user_create.email):
            raise HTTPException(status_code=400, detail="Invalid email address")

        existing_user = await self.user_db.get_by_email(user_create.email)
        if existing_user is not None:
            raise UserAlreadyExists("Пользователь уже существует")

        user_dict = (
            user_create.create_update_dict()
            if safe
            else user_create.create_update_dict_superuser()
        )
        password = user_dict.pop("password")
        user_dict["hashed_password"] = self.password_helper.hash(password)
        user_dict["role_id"] = 1
        user_dict["is_active"] = True
        user_dict["is_superuser"] = False
        user_dict["is_verified"] = False


        created_user = await self.user_db.create(user_dict)

        await self.on_after_register(created_user, request)

        return created_user

    async def update(
            self,
            user_id: int,
            user_update: UserUpdate,
            request: Optional[Request] = None,
    ) -> models.UP:
        existing_user = await self.user_db.get(user_id)
        if not existing_user:
            raise UserNotFound("Пользователь не найден")

        update_dict = {}
        if user_update.username:
            update_dict["username"] = user_update.username

        if user_update.password:
            await self.validate_password(user_update.password, user_update)
            update_dict["hashed_password"] = self.password_helper.hash(
                user_update.password
            )

        updated_user = await self.user_db.update(existing_user, update_dict)

        return updated_user

    async def validate_password(self, password: str, user_create: schemas.UC):
        if len(password) < 2:
            raise PasswordTooShort("Длина пароля должна быть длиньше 2 символов")

            # if not re.search(r'[A-Z]', password):
            #     raise PasswordMissingUppercase("Пароль должен содержать хотя бы одну заглавную букву")
            #
            # if not re.search(r'[a-z]', password):
            #     raise PasswordMissingLowercase("Пароль должен содержать хотя бы одну букву нижнего регистра")
            #
            # if not re.search(r'[0-9]', password):
            #     raise PasswordMissingDigit("Пароль должен содержать хотя бы одну цифру")

    def is_valid_email(self, email: str) -> bool:
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(email_regex, email) is not None


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
