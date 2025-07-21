import React, {useEffect, useState} from "react";

export default function GmailMessage(){
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(()=> {
    fetch("http://localhost:8000/api/messages")
		.then((res) => res.json())
		.then((data)=> {
			setMessages(data.messages);
			setLoading(false);
		})
		.catch((err)=> {
			console.error("Error fetching messages: ",err);
			setLoading(false);
		});

  }, []);


	if (loading) return <p>Loading Inbox...</p>;
	
	return (
    <div>
      <h2>Gmail Messages with Unsubscribe Links</h2>
      <ul>
        {messages.map((msg) => (
          <li key={msg.id}>
            <p><strong>Message ID:</strong> {msg.id}</p>
            <ul>
              {msg.unsubscribe_links.length > 0 ? (
                msg.unsubscribe_links.map((link, index) => (
                  <li key={index}>
                    <a href={link} target="_blank" rel="noopener noreferrer">{link}</a>
                  </li>
                ))
              ) : (
                <li>No unsubscribe links found.</li>
              )}
            </ul>
          </li>
        ))}
      </ul>
    </div>
  );
}