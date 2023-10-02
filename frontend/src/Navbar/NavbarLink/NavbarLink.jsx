import React from "react";
import nav_link_css from "./NavbarLink.module.css";
import {NavLink} from "react-router-dom";

function NavbarLink(props) {
    return (
        <div className={nav_link_css.navbar_link}>
            <NavLink to={props.url}>{props.name}</NavLink>
        </div>
    );
}

export default NavbarLink;
