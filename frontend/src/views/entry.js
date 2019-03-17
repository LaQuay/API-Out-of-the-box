import React from 'react'

import EntryAPI from '../api/entryAPI.js'
import Entry from '../models/entry.js'

export class EntryTab extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
      entriesRows: []
    }
  }

  componentDidMount() {
    EntryAPI.getAllEntries(false, response => {
      var results = response.message.map(entry => {
        return new Entry(entry.id, entry.value, entry.date)
      })
      this.setState({ entriesRows: results })
    })
  }

  render() {
    return (
      <div className="container-fluid">
        {this.state.entriesRows.map(entry => {
          return (
            <div key={entry.id}>
              <dt>{entry.id}</dt>
              <dd>{entry.value}</dd>
              <dd>{entry.date}</dd>
              <hr />
            </div>
          )
        })}
      </div>
    )
  }
}

export default EntryTab
