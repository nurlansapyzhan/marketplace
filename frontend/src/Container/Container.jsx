import content_css from './Container.module.css';
import ProductList from "./ProductList/ProductList";
import Search from "./Search/Search";

function Content(props) {
    return (
        <div>
            <div className={content_css.searchbar}>
                <Search/>
            </div>
            <div className={content_css.con}>
                <ProductList/>
                <ProductList/>
            </div>
        </div>
    );
}

export default Content;