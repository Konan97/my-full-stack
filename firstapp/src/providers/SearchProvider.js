import React, { useState } from 'react';

export const SearchContext = React.createContext();

const SearchContextProvider = ({ children }) => { 
    const [result, setResult] = useState(undefined);

    return (
        <SearchContext.Provider value={{result, setResult}}>
            {children}
        </SearchContext.Provider>
    );

};


export default SearchContextProvider;