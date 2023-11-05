import content_css from './Container.module.css';
import ProductList from "./ProductList/ProductList";
import Search from "./Search/Search";
import {Route, Routes} from "react-router-dom";
import Login from "../Login/Login";
import Account from "./Account/Account";

function Content(props) {
    return (
        <div className={content_css.block}>
            <div>
                <Routes>
                    <Route path='/account/*' element={<Account/>}/>
                </Routes>
            </div>
            <div>
                <div className={content_css.searchbar}>
                    <Search/>
                </div>
                <div className={content_css.con}>
                    <ProductList/>
                    <ProductList/>
                </div>
            </div>
        </div>
    );
}

export default Content;