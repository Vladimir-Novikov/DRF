import React from 'react';
import { BrowserRouter, Route, Routes, Navigate, useLocation, Link } from 'react-router-dom';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User';
import ProjectList from './components/Project';
import Header from './components/Header';
import Footer from './components/Footer';
import ProjectTodos from './components/ProjectTodos';
import TodoList from './components/Todo';
import LoginForm from './components/LoginForm';



const NotFound = () => {
  let location = useLocation();
  return (
    <div>Страница {location.pathname} не найдена</div>
  )
}

class App extends React.Component {
  constructor(prop) {
    super(prop)
    this.state = {
      'users': [],
      'projects': [],
      'todos': [],
      'token': ''
    }
  }

  get_token(login, password) {
    axios.post('http://127.0.0.1:8000/api-token-auth/', { 'username': login, 'password': password })
      .then(response => {
        const token = response.data.token
        localStorage.setItem('token', token)
        this.setState({
          'token': token
        }, this.get_data)
      })
      .catch(error => console.log(error))
  }

  logout() {
    localStorage.setItem('token', '')
    this.setState({
      'token': ''
    }, this.get_data)
  }

  componentDidMount() {
    let token = localStorage.getItem('token')
    this.setState({
      'token': token
    }, this.get_data)
  }

  is_auth() {
    return !!this.state.token
  }

  get_headers() {
    if (this.is_auth()) {
      return {
        'Authorization': 'Token ' + this.state.token
      }
    }
    return {}
  }

  get_data() {
    let headers = this.get_headers()
    axios.get('http://127.0.0.1:8000/api/users/', { headers })
      .then(response => {
        const users = response.data.results
        this.setState(
          {
            'users': users
          }
        )
      }).catch(error => {
        console.log(error)
        this.setState({
          'users': []
        })
      })


    axios.get('http://127.0.0.1:8000/api/projects/', { headers })
      .then(response => {
        const projects = response.data.results
        this.setState(
          {
            'projects': projects
          }
        )
      }).catch(error => {
        console.log(error)
        this.setState({
          'projects': []
        })
      })

    axios.get('http://127.0.0.1:8000/api/todo/', { headers })
      .then(response => {
        const todos = response.data.results
        this.setState(
          {
            'todos': todos
          }
        )
      }).catch(error => {
        console.log(error)
        this.setState({
          'todos': []
        })
      })
  }
  render() {
    return (
      <div class='wrapper'>
        <BrowserRouter>
          <div class='header' style={{ backgroundColor: '#ccc', color: '#fff', marginTop: '10px', marginBottom: '5px', paddingTop: '5px', paddingBottom: '5px' }}>
            <Header />
            <div>
              {this.is_auth() ? <button onClick={() => this.logout()}> Logout </button> : <Link to='/login'>Login</Link>}
            </div>

          </div>
          <div class='main'>
            <Routes>
              <Route exact path='/users' element={<UserList users={this.state.users} />} />
              <Route exact path='/projects' element={<ProjectList projects={this.state.projects} />} />
              <Route exact path='/todo' element={<TodoList todos={this.state.todos} />} />
              <Route exact path='/login' element={<LoginForm get_token={(login, password) => this.get_token(login, password)} />} />
              <Route path='/' element={<Navigate to='/users' />} />
              <Route path='/project/:id' element={<ProjectTodos todos={this.state.todos} />} />
              <Route path='*' element={<NotFound />} />
            </Routes>
          </div>
        </BrowserRouter >
        <div class='footer'>
          <Footer />
        </div>
      </div >
    )
  }
}

export default App;
