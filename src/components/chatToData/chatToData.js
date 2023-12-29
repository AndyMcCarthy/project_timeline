import React, { useEffect, useRef, useState} from "react";
import './form.css'

export const ChatToData = () => {

    const [question, setQuestion] = useState('');
    const [answer, setAnswer] = useState('');

    
    const fetchData = async () => {
        try {
          const response = await fetch("/api/question", {
            method: 'POST',
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                question: 'yourValue',
                User: 'me',
            })
          });

          const data = await response.json();
          setAnswer(data);
        } catch (error) {
          console.error("Error answering question:", error);
        }
      };

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(question)
        fetchData();
        console.log(answer)
    }

    return <>
    <div className="form-box">
    <form onSubmit={handleSubmit}>
    <textarea id= "question" name = "question" type = "text" onChange={e => setQuestion(e.target.value)} rows = {5} cols={150} placeholder={"Ask your question"}></textarea >
    <button type ='Submit' className="Sbmtbtn" >Submit </button>
    </form>
    {(answer !== '') ? <p> {answer.response}</p>:null}
    </div>
    </>
};