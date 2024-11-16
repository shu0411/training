import { useState } from "react";

function Square({ num }) {
  const [value, setValue] = useState(null);

  function handleClick() {
    //console.log(num + " is clicked !");
    console.log(`${num} is clicked !`);
    setValue("X");
  }

  return (
    <button className="square" onClick={handleClick}>
      {value}
    </button>
  );
}

export default function Board() {
  return (
    <>
      <div className="board-row">
        <Square num="1" />
        <Square num="2" />
        <Square num="3" />
      </div>
      <div className="board-row">
        <Square num="4" />
        <Square num="5" />
        <Square num="6" />
      </div>
      <div className="board-row">
        <Square num="7" />
        <Square num="8" />
        <Square num="9" />
      </div>
    </>
  );
}
