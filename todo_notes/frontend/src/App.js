import React from 'react';
import { HashRouter, BrowserRouter, Route, Routes, Switch, Link, Navigate } from 'react-router-dom';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User';
import ProjectList from './components/Project';
import Header from './components/Header';
import Footer from './components/Footer';
import ProjectTodos from './components/ProjectTodos';
import TodoList from './components/Todo';



const NotFound = () => {
  return (
    <div>Страница не найдена</div>
  )
}

class App extends React.Component {
  constructor(prop) {
    super(prop)
    this.state = {
      'users': [],
      'projects': [],
      'todos': []
    }
  }

  componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/users')
      .then(response => {
        const users = response.data
        this.setState(
          {
            'users': users
          }
        )
      }).catch(error => console.log(error))

    axios.get('http://127.0.0.1:8000/api/projects')
      .then(response => {
        const projects = response.data
        this.setState(
          {
            'projects': projects
          }
        )
      }).catch(error => console.log(error))

    axios.get('http://127.0.0.1:8000/api/todo')
      .then(response => {
        const todos = response.data
        this.setState(
          {
            'todos': todos
          }
        )
      }).catch(error => console.log(error))
  }
  render() {
    return (
      <div class='wrapper'>
        {/* <div class='header'>
          <Header />
        </div> */}
        <div class='main'>
          <BrowserRouter>
            <div style={{ backgroundColor: '#ccc' }}>
              <nav>
                <ul>
                  <li><Link to='/users'>Пользователи</Link></li>
                  <li><Link to='/projects'>Проекты</Link></li>
                  <li><Link to='/todo'>Заметки</Link></li>
                </ul>
              </nav>
            </div >

            <Routes>
              <Route exact path='/users' element={<UserList users={this.state.users} />} />
              <Route exact path='/projects' element={<ProjectList projects={this.state.projects} />} />
              <Route exact path='/todo' element={<TodoList todos={this.state.todos} />} />
              <Route path='/' element={<Navigate to='/users' />} />
              <Route path='/project/:id' element={<ProjectTodos todos={this.state.todos} />} />
              <Route path='*' element={<NotFound />} />
            </Routes>
          </BrowserRouter>
        </div>
        <div class='footer'>
          <Footer />
        </div>
      </div>

    )
  }
}

export default App;
