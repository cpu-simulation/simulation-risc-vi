import { useState } from "react";
import { StyledMemory } from "./styledMemory";
import { IMemCells } from "../../assets/interfaces/interfaces";

const Memory = () => {
  const [memory, setMemory]: IMemCells = useState([
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
  ]); // get bulk read for this
  return (
    <div className="col-span-2 row-span-4">
      <StyledMemory>
        <div className="flex">
          <input className="block" type="text" placeholder="Adress..." />
          <div></div>
        </div>
        <div className="cells-body">
          {memory.map((c) => (
            <div className="cell">{c}</div>
          ))}
        </div>
      </StyledMemory>
    </div>
  );
};

export default Memory;
