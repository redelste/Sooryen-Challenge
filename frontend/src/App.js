import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      listings: []
    }
  }
  componentDidMount = () => {
    fetch('/db-result')
      .then(r => r.json())
      .then(({ data : listings}) => this.setState({listings}))
  }
  render() {
    return (
      <div className="App">
        <div>
          {this.state.listings.map(({title, price}) => (
            <div>
              <p>{title}</p>
              <p>${price}</p>
            </div>
          ))}
        </div>
      </div>
    );
  }
}

export default App;
