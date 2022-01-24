import React from 'react'


class TodoForm extends React.Component {
    constructor(prop) {
        super(prop)
        this.state = {
            'project': '',
            'text': '',
            'user': ''

        }
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }


    handleSubmit(event) {
        this.props.create_todo(this.state.project, this.state.text, this.state.user)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <select name='project' onChange={(event) => this.handleChange(event)} >
                    <option selected disabled>Выберите проект</option>
                    {this.props.projects.map((project) => <option value={project.id}>{project.title}</option>)}
                </select>
                <input type='text' name='text' placeholder='текст заметки' value={this.state.text} onChange={(event) => this.handleChange(event)} />
                <select name='user' onChange={(event) => this.handleChange(event)} >
                    <option selected disabled>Укажите автора</option>
                    {this.props.users.map((user) => <option value={user.id}>{user.username} {user.first_name} {user.last_name}</option>)}
                </select>
                <input type='submit' value='Создать заметку' />
            </form>
        )
    }
}

export default TodoForm;
