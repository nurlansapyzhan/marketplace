import login_css from './Authorization.module.css';
import { NavLink, useLocation } from "react-router-dom";
import React, { useEffect } from "react";
import { adjustAuthorizationBlockPosition } from "./AuthorizationBlockPosition";

function Login(props) {
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
                    <input type="password" placeholder="password" required/>
                </div>
                <button type="submit">Login</button>
                <div className={login_css.register_link}>
                    <span>Don't have an account?</span>
                    <NavLink to='/register'>Register</NavLink>
                </div>
            </form>
        </div>
    );
}

export default Login;