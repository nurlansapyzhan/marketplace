import login_css from './Authorization.module.css';
import { NavLink, useLocation } from "react-router-dom";
import React, { useEffect } from "react";
import { adjustAuthorizationBlockPosition } from "./AuthorizationBlockPosition";

function Register(props) {
    useEffect(() => {
        adjustAuthorizationBlockPosition();
    }, []);

    return (
        <div className={`${login_css.authorization_block} ${login_css.no_overlay}`}>
            <form>
                <h1>Login</h1>
                <div className={login_css.input_box}>
                    <input type="text" placeholder="username" required/>
                </div>
                <div className={login_css.input_box}>
                    <input type="text" placeholder="firstname" required/>
                </div>
                <div className={login_css.input_box}>
                    <input type="text" placeholder="secondname" required/>
                </div>
                <div className={login_css.input_box}>
                    <input type="text" placeholder="surname"/>
                </div>
                <div className={login_css.input_box}>
                    <input type="email" placeholder="email" required/>
                </div>
                <div className={login_css.input_box}>
                    <input type="password" placeholder="password" required/>
                </div>
                <div className={login_css.input_box}>
                    <input type="password" placeholder="repeat password" required/>
                </div>
                <button type="submit">Register</button>
            </form>
        </div>
    );
}

export default Register;