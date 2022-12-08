import './App.css';
import { useState } from "react";

function Contacts() {
    const [data, setData] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [err, setErr] = useState('');

    const URL = 'https://us-central1-psychic-catwalk-370506.cloudfunctions.net/contacts'
    const URLDelete = "https://us-central1-psychic-catwalk-370506.cloudfunctions.net/deletecontact"

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

      const handleClickDelete = async () => {
        console.log(URLDelete)
        setIsLoading(true);
        try {
          const response = await fetch(URLDelete, {
            method: 'GET',
          });
    
          const result = await response.text();
    
          console.log('result is: ', result);
          alert("result")
        } catch (err) {
          setErr(err.message);
        } finally {
          setIsLoading(false);
          handleClick()
        }
      };

    return (
    <div style={{maxWidth:"30vw"}}>
        {/* {err && <h2>{err}</h2>} */}
        <button onClick={handleClick}>Refresh</button>
        <button onClick={handleClickDelete}>Delete</button>
        <p>List of Contacts in Group:</p>
        <table >
            <tr>
                <th>id</th>
                <th>Last</th>
                <th>First</th>
                <th>Phone</th>
                <th>Email</th>
            </tr>
        {
        data.map((element) => 
            <tr>
                <td>{element[0]}</td>
                <td>{element[1]}</td>
                <td>{element[2]}</td>
                <td>{element[3]}</td>
                <td>{element[4]}</td>
            </tr>
            )
            
        }
        </table>
        
        {isLoading && <h2>Loading...</h2>}

    </div>
      )
    }


export default Contacts;