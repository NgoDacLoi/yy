import React, { useState, useEffect } from "react"
import TodoItem from "./ToDoItem"
import "./App.css"
const App = (props) => {
  const [items, setItems] = useState("")
  const [currentid, setCurrentid] = useState("")
  const [currentfirstname, setCurrentfirstname] = useState("")
  const [currentlastname, setCurrentlastname] = useState("")

  useEffect(() => {
    readItem()
  }, [])

  const readItem = () => {
    var requestOptions = {
      method: 'GET',
      redirect: 'follow'
    };

    fetch("http://127.0.0.1:5000/data", requestOptions)
      .then(response => response.text())
      .then(result => {
        setItems(JSON.parse(result).items)
      })
      .catch(error => console.log('error', error));
  }
 
  const addItem = () => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({ "id": currentid,"firstname": currentfirstname,"lastname": currentlastname });
    setCurrentfirstname('')
    setCurrentid('')
    setCurrentlastname('')

    var requestOptions = {
      method: 'POST',
      headers: myHeaders,
      body: raw,
      redirect: 'follow'
    };

    fetch("http://127.0.0.1:5000/data", requestOptions)
      .then(response => response.text())
      .then(result => {
        console.log(result)
        readItem()
      })
      .catch(error => console.log('error', error));
  }

  return (
    <div className="todo-list">
      <h1> Danh sách các cầu thủ </h1>
      <h4>fname</h4>
      <input value={currentfirstname} onChange={(event) => {
        setCurrentfirstname(event.target.value);
      }}
      />
      <h4>id</h4>
      <input value={currentid} onChange={(event) => {
        setCurrentid(event.target.value);
      }}
      />
      <h4>lastname</h4>
      <input value={currentlastname} onChange={(event) => {
        setCurrentlastname(event.target.value);
      }}
      />

      <button onClick={() => addItem()}>Add</button>
     
    </div>
  )

}

export default App;
