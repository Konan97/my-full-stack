import React, { useContext } from "react";
import {SearchContext} from "../providers/SearchProvider";

export default function Search(){
    const {setResult} = useContext(SearchContext);

    function handleSubmit(e) {
        e.preventDefault();
        const form = e.target;
        const formData = new FormData(form);
        const query = formData.get("myInput");
        setResult(query);
    }
    
    return (
        <form method="post" onSubmit={handleSubmit}>
            <label>
                Text input: <input name = "myInput"/>
            </label>
            <button type="submit">Search</button>
        </form>
    );
};
