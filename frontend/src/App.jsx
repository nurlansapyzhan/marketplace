import Navbar from './Navbar/Navbar.jsx';
import {BrowserRouter, Route, Routes, useLocation} from 'react-router-dom'
import Content from "./Container/Container";
import Footer from "./Footer/Footer";
import './App.css'
import Login from "./Login/Login";
import login_css from "./Login/Authorization.module.css";
import {useEffect} from "react";
import Register from "./Login/Register";

function App() {

    const location = useLocation();

    function createOverlay() {
        const overlayDiv = document.createElement('div');
        overlayDiv.className = `${login_css.overlay}`;
        document.body.appendChild(overlayDiv);
    }

    function removeOverlay() {
        const overlayDivs = document.getElementsByClassName(`${login_css.overlay}`);
        const overlayArray = Array.from(overlayDivs);

        overlayArray.forEach((overlayDiv) => {
            if (overlayDiv && overlayDiv.parentNode) {
                overlayDiv.parentNode.removeChild(overlayDiv);
            }
        });
    }

    useEffect(() => {
        if (location.pathname === '/login' || location.pathname === '/register') {
            removeOverlay();
            createOverlay();
        } else {
            removeOverlay();
        }
    }, [location.pathname]);

    return (
        <div>
            <Navbar/>
            <Routes>
                <Route path="/login" element={ <Login/> }/>
                <Route path="/register" element={ <Register/> }/>
            </Routes>
            <Content/>
            <Footer/>
        </div>
    );
}

// document.documentElement.style.setProperty('--main-color', 'white');

// window.addEventListener('resize', function () {
//     console.log(window.innerWidth);
// });

export default App;
