import React, {useState} from 'react';
import {useParams, useNavigate} from 'react-router-dom';
import search_css from './Search.module.css';

function Search(props) {
    const {query} = useParams();
    const [searchTerm, setSearchTerm] = useState(query || '');
    const [enterPressed, setEnterPressed] = useState(false);
    const navigate = useNavigate();

    const handleSearch = () => {
        if (searchTerm.trim() !== '') {
            navigate(`/?search=${searchTerm}`);
        } else if (searchTerm.trim() === '') {
            navigate(``);
        }
    };

    const handleKeyPress = (e) => {
        if (e.key === 'Enter') {
            setEnterPressed(true);
            handleSearch();
            // Сбрасываем состояние enterPressed через небольшой интервал
            setTimeout(() => {
                setEnterPressed(false);
            }, 100);
        }
    };

    const buttonStyle = {
        backgroundColor: enterPressed ? getComputedStyle(document.documentElement).getPropertyValue('--main-search-button-active-bg-color') : getComputedStyle(document.documentElement).getPropertyValue('--main-search-button-bg-color'),
    };

    return (<div className={search_css.d2}>
        <input
            type="text"
            placeholder="Искать здесь..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            onKeyPress={handleKeyPress}
        />
        <button
            onClick={handleSearch}
            style={buttonStyle}
        >AA</button>
    </div>);
}

export default Search;