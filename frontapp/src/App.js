/**
 * main app
 */
import {React} from "react";
import logo from './logo.svg';
import './App.css';
import Header from "./components/Header";
import Nav from "./components/Nav";
import Search from "./components/Search";
import SearchContextProvider from "./providers/SearchProvider";


function App() {
  return (
    <div className="App">
      <SearchContextProvider>
        <Header/>
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <Nav className="Nav"/>
        <Search className="searchQuery"/>
      </SearchContextProvider>
    </div>
  );
}

export default App;
