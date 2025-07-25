import React from "react";
import './css/EmailCard.css'

export default function EmailCard({email}){
    const {from,subject,unsubscribe_links} = email;

  return(
    <div className='email-card'>
      <h2 className="email-from">
        <strong>{from || "Unknown Sender"}</strong>
      </h2>

      <h3 className="email-subject"> {subject || "No Subject"}</h3>


        {unsubscribe_links && unsubscribe_links.length > 0 ? (
          <div className="email-links">
            <ul>
              {unsubscribe_links.map((link, index)=>(
                <li key={index}>
                  <a href={link} target="_blank" rel="noopener noreferrer">
                  <button> Unsubscribe</button>
                  </a>
                </li>
              ))}
            </ul>
          </div>
        ): (
        <p>No unsubscribe links found.</p>
      )}
    </div>
  );
}

