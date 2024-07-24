import React, { useContext } from "react";
import { SearchContext } from "../App"

function Header(props) {

    const {result} = useContext(SearchContext);

    const styles = {
        color: "black", fontSize: "40px"
    }
    
    return (
        <div>
            <h1 style={styles}> Hello, {result}!</h1>
        </div>
    );
};

export default Header;