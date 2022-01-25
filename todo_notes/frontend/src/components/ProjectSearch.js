import React from 'react'
import { Link } from "react-router-dom"

class ProjectSearch extends React.Component {
    constructor(prop) {
        super(prop)
        this.state = {
            'title': ''
        }
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }


    handleSubmit(event) {
        this.props.search_project(this.state.title)
        event.preventDefault()
    }

    render() {
        return (
            <div>
                <form onSubmit={(event) => this.handleSubmit(event)}>
                    <input type='text' name='title' placeholder='название проекта' value={this.state.title} onChange={(event) => this.handleChange(event)} />
                    <input type='submit' value='Поиск' />
                </form>
                <div class='main'>
                </div>
            </div>
        )
    }
}


export default ProjectSearch;
