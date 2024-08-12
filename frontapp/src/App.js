/**
 * main app
 */
import {React} from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';
import Header from "./components/Header";
import Nav from "./components/Nav";
import Search from "./components/Search";
import SearchContextProvider from "./providers/SearchProvider";
import Dropdown from './components/Dropdown';

function App() {

  return (
    <div className="App">
      <SearchContextProvider>
        <Header/>
        <img src={logo} className="App-logo" alt="logo" />
        
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
        <Dropdown className="DropdownMenu"/>

      </SearchContextProvider>
    </div>
  );
}

export default App;
