import React, { Component } from 'react'
import { BrowserRouter as Router } from 'react-router-dom'

import Header from './components/Header.js'
import Main from './components/Main.js'

import './App.css'

class App extends Component {
  render() {
    return (
      <div>
        <Router>
          <div>
            <Header />
            <Main />
          </div>
        </Router>
      </div>
    )
  }
}

export default App