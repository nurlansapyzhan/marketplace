import nav_css from './Navbar.module.css'
import NavbarLink from "./NavbarLink/NavbarLink";

function Navbar(props) {
    return (
            <div className={nav_css.navbar}>
                <nav>
                    <div className={nav_css.left_nav}>
                        <NavbarLink name="Hello" url="/"/>
                        <NavbarLink name="World" url="/bbb"/>
                        <NavbarLink name="Company" url="/ccc"/>
                    </div>
                    <div className={nav_css.right_nav}>
                        <NavbarLink name="Login" url="/login"/>
                        <NavbarLink name="Logout" url="/logout"/>
                        <NavbarLink name="Register" url="/register"/>
                    </div>
                </nav>
            </div>
    );
}
// document.documentElement.style.setProperty('--main-bg-color', 'yellow');

export default Navbar;
