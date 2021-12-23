import React from "react"
import { Link } from "react-router-dom"

const ProjectItem = ({ project }) => {
    return (
        <tr>
            <td>
                <Link to={`/project/${project.id}`}>{project.title}</Link>

            </td>
            {/* <td>
                {project.title}
            </td> */}
            <td>
                {project.repo_link}
            </td>
            <td>
                {project.users}
            </td>
        </tr>
    )
}

const ProjectList = ({ projects }) => {
    return (
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
            {projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}

export default ProjectList
