// import logo from './logo.svg';
import './App.css';
import SMSInterface from './SMSInterface';
import Contacts from './Contacts';
import Messages from './Messages';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={"https://lh5.googleusercontent.com/-FAewbXY6Bn4/AAAAAAAAAAI/AAAAAAAAAAA/N8rJKh8bpT8/s88-p-k-no-ns-nd/photo.jpg"} className="App-logo logo" alt="logo" scale={0.1}/>
        <p>
        <br/>Below are some example components for demo purposes<br/>
        </p>
      </header>
      <body>
        <div className="grid-container" style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gridGap: 10 }}>
          <div><SMSInterface/></div>
          <div><Contacts/></div>
          <div><Messages/></div>
        </div>
      </body>
      
    </div>
  );
}

export default App;
