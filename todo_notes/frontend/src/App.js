import React from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User';
import Header from './components/Header';
import Footer from './components/Footer';

class App extends React.Component {
  constructor(prop) {
    super(prop)
    this.state = {
      'users': []
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
  }
  render() {
    return (
      <div class='wrapper'>
        <div class='header'>
          <Header />
        </div>
        <div class='main'>
          <UserList users={this.state.users} />
        </div>
        <div class='footer'>
          <Footer />
        </div>
      </div>

    )
  }
}

export default App;
