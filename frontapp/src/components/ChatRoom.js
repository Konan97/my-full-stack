import { useState, useEffect } from "react";
import { createConnection } from "../providers/chat.js";

export default function ChatRoom({ outgoingUrl }) {
    const [serverUrl, setServerUrl] = useState(outgoingUrl);
  
    useEffect(() => {
      const connection = createConnection(serverUrl);
      //connection.connect();
      return () => {
        //connection.disconnect();
      };
    }, [serverUrl]);
  
    return (
      <>
        <label>
          Server URL:{' '}
          <input
          value={serverUrl}
          onChange={e=> setServerUrl(e.target.value)}
          />
        </label>
      </>
    );
  }