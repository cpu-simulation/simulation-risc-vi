import { useState } from "react";
import { StyledMemory } from "./styledMemory";
import { IUserInp } from "../../assets/interfaces/interfaces";

const Memory = (props: { memory: any[] }) => {
  const [search, setSearch]: IUserInp = useState("");
  const [searched, setSearched] = useState([""]);

  return (
    <StyledMemory className="col-span-2 row-span-4">
      <div className="flex">
        <input
          className="block"
          type="text"
          placeholder="Address : Value"
          onChange={(e) => {
            setSearch(e.target.value);
            setSearched(
              props.memory.filter((element) => {
                return element[0] === e.target.value;
              })
            );
          }}
        />
      </div>
      <div className="cells-body">
        {search === ""
          ? props.memory.map((c) => (
              <div className="cell">{`${parseInt(c[0]).toString(16)} : ${parseInt(
                c[1]
              ).toString(16)}`}</div>
            ))
          : searched.map((c) => (
              <div className="cell">{`${parseInt(c[0]).toString(16)} : ${parseInt(
                c[1]
              ).toString(16)}`}</div>
            ))}
      </div>
    </StyledMemory>
  );
};

export default Memory;
