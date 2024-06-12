import { useState } from "react";
import { StyledUserInput } from "./styledUserInput";

const UserInput = () => {
  const [input, setInput] = useState("")
  return (
    <>
      <StyledUserInput className="col-span-5 row-span-4">
        <textarea onChange={(e)=>setInput(e.target.value)}></textarea>
      </StyledUserInput>
    </>
  );
};

export default UserInput;
