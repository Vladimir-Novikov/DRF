import React from "react";
import { Link } from 'react-router-dom';

const Header = () => {
    return (

        <nav>
            <ul>
                <li><Link to='/users'>Пользователи</Link></li>
                <li><Link to='/projects'>Проекты</Link></li>
                <li><Link to='/todo'>Заметки</Link></li>
            </ul>
        </nav>

    )
}

export default Header