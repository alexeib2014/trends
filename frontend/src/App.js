import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';

class App extends Component {
  constructor() {
    super()
    this.state = {
      value: '',
      data: []
    }

    this.handleChange = this.handleChange.bind(this)
    this.handleSearch = this.handleSearch.bind(this)
  }

  handleChange(event) {
    this.setState({ value: event.target.value });
  }

  handleSearch() {
    axios.get('/api/trends?keyword=' + this.state.value)
         .then(response => {
            this.setState({ data: response.data.default.timelineData })
            console.log(response)
          })
  }

  render() {
    return (
      <div className="App">
        <input type="text" value={this.state.value} onChange={this.handleChange} />
        <button onClick={this.handleSearch}>
          Search
        </button>
        <table>
          { this.state.data.map(row => <tr>
                                          <td>
                                            { row.formattedAxisTime }
                                          </td>
                                          <td>
                                            { row.formattedValue[0] }
                                          </td>
                                        </tr>) }
        </table>
      </div>
    );
  }
}

export default App;
