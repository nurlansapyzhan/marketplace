import React from "react";
import nav_link_css from "./NavbarLink.module.css";
import {NavLink, useLocation} from "react-router-dom";

function NavbarLink(props) {
    let currentUrl = useLocation().pathname;
    let newUrl = props.url;
    let linkArray = ['login', 'logout', 'register']
    if (!(currentUrl === '/')) {
        let currentUrlArray = currentUrl.split('/')
        let firstLinkUrl = currentUrlArray[1]
        if (linkArray.includes(props.url) || currentUrlArray.length <= 1) {
            newUrl = props.url + currentUrl;
        }
    }

    return (
        <div className={nav_link_css.navbar_link}>
            <NavLink to={newUrl}>{props.name}</NavLink>
        </div>
    );
}

export default NavbarLink;
