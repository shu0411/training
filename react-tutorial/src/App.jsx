import { useState } from "react";

//今後やりたいこと
//名前の入力フォームを作成
//XOの表示を名前に変更
//勝敗が決まった時に、勝者の名前を表示
//盤面のサイズを変更できるようにする
//勝敗の判定をハードコーディングから動的に変更できるようにする

function Square({ value, onSquareClick }) {
  //  const [value, setValue] = useState(null);
  //
  //  function handleClick() {
  //    //console.log(num + " is clicked !");
  //    console.log(`${num} is clicked !`);
  //    setValue("X");
  //  }

  return (
    <button className="square" onClick={onSquareClick}>
      {value}
    </button>
  );
}

function Board({ xIsNext, squares, onPlay }) {
  function handleClick(i) {
    console.log(`${i} is clicked !`);
    if (calculateWinner(squares) || squares[i]) {
      return;
    }
    const nextSquares = squares.slice();
    if (xIsNext) {
      nextSquares[i] = "X";
    } else {
      nextSquares[i] = "O";
    }
    onPlay(nextSquares);
  }

  const winner = calculateWinner(squares);
  let status;
  if (winner) {
    status = "Winner: " + winner;
  } else {
    status = "Next player: " + (xIsNext ? "X" : "O");
  }

  //行数、列数を定義
  //const rows = Array(3).keys(); //Emptyの配列を使うので、非効率らしい
  //const cols = [0,1,2];
  let rows = [];
  let cols = [];
  for (let i = 0; i < 3; i++) {
    rows.push(i);
    cols.push(i);
  }

  return (
    <>
      <div className="status">{status}</div>
      {rows.map((row) => (
        <div key={row} className="board-row">
          {cols.map((col) => {
            const index = row * 3 + col;
            return (
              <Square
                key={index}
                value={squares[index]}
                onSquareClick={() => handleClick(index)}
              />
            );
          })}
        </div>
      ))}
    </>
  );
}

export default function Game() {
  const [history, setHistory] = useState([Array(9).fill(null)]);
  const [currentMoveID, setCurrentMoveID] = useState(0);
  const xIsNext = currentMoveID % 2 === 0;
  const currentSquares = history[currentMoveID];

  function handlePlay(nextSquares) {
    const nextHistory = [...history.slice(0, currentMoveID + 1), nextSquares];
    setHistory(nextHistory);
    setCurrentMoveID(nextHistory.length - 1);
  }

  function jumpTo(nextMoveID) {
    setCurrentMoveID(nextMoveID);
  }

  function getContent(moveID, description) {
    if (moveID < history.length - 1) {
      return <button onClick={() => jumpTo(moveID)}>{description}</button>;
    } else {
      return <p>You are at move # {moveID}</p>;
    }
  }

  const moves = history.map((squares, moveID) => {
    let description;
    if (moveID > 0) {
      description = "Go to move #" + moveID;
    } else {
      description = "Go to game start";
    }
    return <li key={moveID}>{getContent(moveID, description)}</li>;
  });

  return (
    <div className="game">
      <div className="game-board">
        <Board xIsNext={xIsNext} squares={currentSquares} onPlay={handlePlay} />
      </div>
      <div className="game-info">
        <ol>{moves}</ol>
      </div>
    </div>
  );
}

function calculateWinner(squares) {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];

  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
}
