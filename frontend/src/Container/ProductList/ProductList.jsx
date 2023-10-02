import product_list_css from './ProductList.module.css';
import Product from "./Product/Product";
import {NavLink} from "react-router-dom";

function Container(props) {
    const productList = [
        { name: "Продукт 1" },
        { name: "Продукт 2" },
        { name: "Продукт 3" },
        { name: "Продукт 4" },
        { name: "Продукт 5" },
        { name: "Продукт 6" },
        { name: "Продукт 7" },
        { name: "Продукт 8" },
        { name: "Продукт 9" },
        { name: "Продукт 10" },
        { name: "Продукт 11" },
        { name: "Продукт 12" },
        { name: "Продукт 13" },
        { name: "Продукт 14" },
        { name: "Продукт 15" }
    ];

    const newProductList = productList.map((product, index) => (
        <Product key={index} productInfo={product} />
    ));


    return (
        <div className={product_list_css.list}>
            <div className="product_list_header">Hello world</div>
            <div className={product_list_css.items}>
                {newProductList}
            </div>
        </div>
    );
}


export default Container;