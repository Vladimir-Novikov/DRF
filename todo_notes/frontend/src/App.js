import React from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js';
class App extends React.Component {
  constructor(prop) {
    super(prop)
    this.state = {
      'users': []
    }
  }

  // componentDidMount() {
  //   const users = [
  //     {
  //       "username": "admin",
  //       "first_name": "иван",
  //       "last_name": "бубликов",
  //       "email": "admin@mail.ru"
  //     },

  //   ]
  //   this.setState(
  //     {
  //       'users': users
  //     }
  //   )
  // }

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
  }
  render() {
    return (
      <div>
        <UserList users={this.state.users} />
      </div>
    )
  }
}

export default App;
