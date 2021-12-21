import React from "react"
import { Link } from 'react-router-dom';

const TodoItem = ({ todo }) => {
    return (
        <tr>
            <td>
                {todo.project}
            </td>
            <td>
                {todo.text}
            </td>
            <td>
                {todo.user}
            </td>
            <td>
                {todo.created_at}
            </td>
        </tr>
    )
}

const TodoList = ({ todos }) => {
    return (
        <table>
            <th>
                Проект ID
            </th>
            <th>
                Содержание
            </th>
            <th>
                Автор
            </th>
            <th>
                Создана
            </th>
            {todos.map((todo) => <TodoItem todo={todo} />)}
        </table>
    )
}

export default TodoList
