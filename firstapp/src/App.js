import {React, useState, createContext} from "react";
import logo from './logo.svg';
import './App.css';
import Header from "./components/Header";
import Nav from "./components/Nav";
import Search from "./components/Search";

// Create a new context and export
export const SearchContext = createContext();

// Create a Context Provider
const SearchContextProvider = ({ children }) => {
    const [result, setResult] = useState(undefined);

    return (
      <SearchContext.Provider value={{result, setResult}}>
        {children}
      </SearchContext.Provider>
    );
};

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
