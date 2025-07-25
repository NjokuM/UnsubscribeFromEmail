import React, {useEffect, useState} from "react";
import EmailCard from "../Component/EmailCard";
import './css/GmailMessage.css'

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


	if (loading) return <p className="loader"></p>;
	
	return (
    <div className="card-grid">
      {messages.map((msg)=>(
        <EmailCard key={msg.id} email={msg}/>
      ))}
    </div>
  );
}