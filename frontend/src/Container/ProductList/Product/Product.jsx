import product_css from './Product.module.css';

function Product(props) {
    return (
        <div className={product_css.item}>
            <img src={ props.productInfo.image } alt={ props.productInfo.name }/>
            <p>{ props.productInfo.name }</p>
        </div>
    );
}

export default Product;