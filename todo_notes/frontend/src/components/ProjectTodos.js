import React from "react"
import { useParams } from "react-router-dom"

// Фильтрация заметок по проекту

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

const ProjectTodos = ({ todos }) => {
    let { id } = useParams();
    console.log(id)
    let filteredTodos = todos.filter((todo) => todo.project == id)


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
            {filteredTodos.map((todo) => <TodoItem todo={todo} />)}
        </table>
    )
}

export default ProjectTodos;
