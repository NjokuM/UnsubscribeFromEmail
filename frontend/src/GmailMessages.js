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
				<table> 
					<thead>
					<span>Number of Messages:{messages.length}</span>
					<tr></tr>
						<td> Message ID:</td>
						<td> Sender:</td>
						<td> Subject:</td>
						<td> Unsubscribe Link:</td>
					</thead>

					<tbody>
            {messages.map((msg) => (
              <tr key={msg.id}>
                <td>{msg.id}</td>
                <td>{msg.from}</td>
                <td>{msg.subject}</td>
                <td>
                  {msg.unsubscribe_links.length > 0 ? (
                    msg.unsubscribe_links.map((link, index) => (
                      <a key={index} href={link} >Unsubscribe</a>
                    ))
                  ) : (
                    <span>No unsubscribe links found.</span>
                  )}
                </td>
              </tr>
            ))}
					</tbody>
					
				</table>
      </ul>
    </div>
  );
}