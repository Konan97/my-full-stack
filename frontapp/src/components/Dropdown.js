import { useState } from "react";
import { openInNewTab } from "./openNewTab";

export default function Dropdown() {
    const [selectedUrl, setSelectUrl] = useState("https://app.powerbi.com/groups/ff1203b9-d8ea-4be4-9858-eb407bb4a0ae/reports/3050ca82-7201-4755-ba60-12685c0122ea?experience=power-bi");
    function handleSubmit(e) {
        e.preventDefault();
        openInNewTab(selectedUrl);
    }
    return (
        <form method="post" onSubmit={handleSubmit}>
        <label>
            Choose the resource: {' '}
            <select name="select link"
                value={selectedUrl}
                onChange={e=> setSelectUrl(e.target.value)}>
                <option value="https://app.powerbi.com/groups/ff1203b9-d8ea-4be4-9858-eb407bb4a0ae/reports/3050ca82-7201-4755-ba60-12685c0122ea?experience=power-bi">Daily Paint Quality</option>
                <option value="https://app.powerbi.com/groups/ff1203b9-d8ea-4be4-9858-eb407bb4a0ae/reports/046ae874-8093-417c-9a19-330887306de0?experience=power-bi">Weekly Paint Quality</option>
                <option value="https://app.powerbi.com/groups/ff1203b9-d8ea-4be4-9858-eb407bb4a0ae/reports/d46f10ce-8dcd-4a50-af47-f591eb1713d4?experience=power-bi">Monthly Paint Quality</option>
            </select>
          </label>
          <button type="reset">Reset</button>
          <button type="submit">Submit</button>
        </form>
    )
}