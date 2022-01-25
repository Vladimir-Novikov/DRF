import React from "react"
import { Link } from "react-router-dom"


const ProjectItem = ({ project, delete_project }) => {
    return (
        < tr >
            <td>
                <Link to={`/project/${project.id}`}>{project.title}</Link>
            </td>
            <td>
                {project.repo_link}
            </td>
            <td>
                {project.users}
            </td>
            <td><button onClick={() => delete_project(project.id)} type='button'>Удалить проект</button></td>
        </tr >
    )
}



const ProjectList = ({ projects, delete_project }) => {

    return (
        <div>
            <table>
                <th>
                    Название
                </th>
                <th>
                    Ссылка
                </th>
                <th>
                    Пользователи
                </th>
                <th></th>
                {projects.map((project) => <ProjectItem project={project} delete_project={delete_project} />)}
            </table>
        </div>
    )
}

export default ProjectList
