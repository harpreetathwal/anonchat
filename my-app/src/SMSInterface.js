import './App.css';
import { useState } from "react";

function SMSInterface() {
    const [lname, setLName] = useState("");
    const [fname, setFName] = useState("");
    const [email, setEmail] = useState("");
    const [phone, setPhone] = useState("");
    const [data, setData] = useState("");
    const [isLoading, setIsLoading] = useState(false);
    const [err, setErr] = useState('');

    const URL = 'https://us-central1-psychic-catwalk-370506.cloudfunctions.net/create?' + new URLSearchParams({
        lname: lname,
        fname: fname,
        email: email,
        phone_number: phone
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
    
          setData(result);
          alert(result)
        } catch (err) {
          setErr(err.message);
        } finally {
          setIsLoading(false);
        }
      };

    return (
    <div>
      {/* {err && <h2>{err}</h2>} */}
      <button onClick={handleClick}>Create User</button>&nbsp;&nbsp;&nbsp;
      <br/><br/>

      {isLoading && <h2>Loading...</h2>}

        <form>
          <label>Enter your lastname:&nbsp;&nbsp;<br/>
            <input
              type="text" 
              value={lname}
              onChange={(e) => setLName(e.target.value)}
              placeholder="last"
            />
          </label>
          <br/><br/>
          <label>Enter your firstname:&nbsp;&nbsp;<br/>
          <input
              type="text" 
              value={fname}
              onChange={(e) => setFName(e.target.value)}
              placeholder="first"
            />
          </label>
          <br/><br/>
          <label>Enter your email:&nbsp;&nbsp;<br/>
          <input
              type="text" 
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="email"
            />
          </label>
          <br/><br/>
          <label>Enter 10-digit phone:&nbsp;&nbsp;<br/>
          <input
              type="text" 
              value={phone}
              onChange={(e) => setPhone(e.target.value)}
              placeholder="phone"
            />
          </label>
        </form>
    </div>
      )
    }


export default SMSInterface;