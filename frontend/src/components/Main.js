import React, { Component } from 'react'
import { Redirect, Route, Switch } from 'react-router-dom'
import EntryTab from '../views/entry.js'

import '../App.css'

class Main extends Component {
  render() {
    return (
      <div>
        <div className="App-content">
          <Switch>
            <Route path="/entry" component={EntryTab} />
            <Redirect from="/" to="/entry" />
          </Switch>
        </div>
      </div>
    )
  }
}

export default Main
