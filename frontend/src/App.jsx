import Navbar from './Navbar/Navbar.jsx';
import {BrowserRouter} from 'react-router-dom'
import Content from "./Container/Container";
import Footer from "./Footer/Footer";
import './App.css'

function App() {
    return (
        <div>
            <Navbar/>
            <Content/>
            <Footer/>
        </div>
    );
}

// document.documentElement.style.setProperty('--main-color', 'white');
window.addEventListener('resize', function () {
    console.log(window.innerWidth);
});

export default App;
