import React from "react";
import { Link } from 'react-router-dom';

const Header = () => {
    return (
        <div style={{ backgroundColor: '#ccc', color: '#fff', marginTop: '10px', marginBottom: '5px', paddingTop: '5px', paddingBottom: '5px' }}>
            <nav>
                <ul>
                    <li><Link to='/users'>Пользователи</Link></li>
                    <li><Link to='/projects'>Проекты</Link></li>
                    <li><Link to='/todo'>Заметки</Link></li>
                    <li><Link to='/login'>Login</Link></li>
                </ul>
            </nav>
        </div >
    )
}

export default Header