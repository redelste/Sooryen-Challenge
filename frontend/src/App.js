import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      listings: [],
      currentListing: 0
    }
  }

  componentDidMount = () => {
    fetch('/db-result')
      .then(r => r.json())
      .then((data) => {
        this.setState({ listings: data.data })
        console.log(data)
      })
  }
  render() {
    if (this.state.listings[this.state.currentListing]) {
      const { title, price } = this.state.listings[this.state.currentListing]
      return (
        <div className="App container">
          <div>
            <div>
              <p>{title}, ${price}</p>
            </div>
            {this.state.currentListing == 0 ? null : <button onClick={() =>this.setState({currentListing: this.state.currentListing-1})}>
              Previous Listing
            </button>}
            {this.state.currentListing == this.state.listings.length-1 ? null : <button onClick={() => this.setState({currentListing : this.state.currentListing+1})}>
              Next Listing
            </button>}

          </div>
        </div>
      );
    } else {
      return (
        <div className="App">
          <div>
            Page does not Exist
          </div>
        </div>
      )
    }
  }
}

export default App;
