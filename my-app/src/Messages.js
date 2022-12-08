import './App.css';
import { useState } from "react";

function cleanPhone(phone){
    let result;
    if (phone.length == 10) {
        result = '+1'+phone;
    } else if (phone.length == 11){
        result = '+'+phone;
    } else {
        result = phone
    }
    return result;
    
}

function Messages() {
    const [data, setData] = useState([]);
    const [message, setMessage] = useState("");
    const [phone, setPhone] = useState("");
    const [isLoading, setIsLoading] = useState(false);
    const [err, setErr] = useState('');

    const URL = 'https://us-central1-psychic-catwalk-370506.cloudfunctions.net/messages'

    const messageURL = 'https://us-central1-psychic-catwalk-370506.cloudfunctions.net/send?' + new URLSearchParams({
        message: message,
        to: cleanPhone(phone)
    })

    const handleClick = async () => {
        console.log(URL)
        setIsLoading(true);
        try {
          const response = await fetch(URL, {
            method: 'GET',
          });
    
          const result = await response.text();
    
          console.log('result is: ', result);
    
          setData(JSON.parse(result));
        //   alert("result")
        } catch (err) {
          setErr(err.message);
        } finally {
          setIsLoading(false);
        }
      };

      const handleClickSendMessage = async () => {
        console.log(messageURL)
        setIsLoading(true);
        try {
          const response = await fetch(messageURL, {
            method: 'GET',
          });
    
          const result = await response.text();
    
          console.log('result is: ', result);
        } catch (err) {
          setErr(err.message);
        } finally {
          setIsLoading(false);
        }
      };

    return (
    <div style={{maxWidth:"30vw"}}>
        {/* {err && <h2>{err}</h2>} */}
        <button onClick={handleClick}>Refresh</button>
        <p>Message Log:</p>
        <table >
            <tr>
                <th>id</th>
                <th>from</th>
                <th>message</th>
            </tr>
        {
        data.map((element) => 
            <tr>
                <td>{element[0]}</td>
                <td>{element[1]}</td>
                <td>{element[2]}</td>
            </tr>
            )
            
        }
        </table>
        
        {isLoading && <h2>Loading...</h2>}

        <br/>
        <form>
          <label>Enter your new message:&nbsp;&nbsp;<br/>
            <input
              type="text" 
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              placeholder="enter message..."
            />
          </label>
          <br/>
          <label>Enter a valid 10-digit phone number:&nbsp;&nbsp;<br/>
            <input
              type="text" 
              value={phone}
              onChange={(e) => setPhone(e.target.value)}
              placeholder="enter phone..."
            />
          </label>
        </form>
        <button onClick={handleClickSendMessage}>Send Message</button>

    </div>
      )
    }


export default Messages;