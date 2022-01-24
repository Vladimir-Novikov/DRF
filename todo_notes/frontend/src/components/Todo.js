import React from "react"

const TodoItem = ({ todo, delete_todo }) => {
    return (
        <tr>
            <td>
                <input type="checkbox" checked={todo.is_active} />
            </td>
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
            <td>
                {todo.is_active ? <button onClick={() => delete_todo(todo.id)} type='button'>Пометить заметку как 'выполнена'</button> : <div>Сделано</div>}
                {/* <button onClick={() => delete_todo(todo.id)} type='button'>Пометить заметку как 'выполнена'</button> */}
            </td>
        </tr>
    )
}

const TodoList = ({ todos, delete_todo }) => {
    return (
        <table>
            <th>
                Активна
            </th>
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
            <th></th>
            {todos.map((todo) => < TodoItem todo={todo} delete_todo={delete_todo} />)}
        </table>
    )
}

export default TodoList
