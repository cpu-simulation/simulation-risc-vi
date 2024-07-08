import { useState } from "react";
import {
  Btn,
  LongButton,
  StyledUserInput,
  UserInputTop,
  CoEx,
} from "./styledUserInput";
import CodeIcon from "@mui/icons-material/Code";
import PlayArrowIcon from "@mui/icons-material/PlayArrow";
import {  IUserInp } from "../../assets/interfaces/interfaces";
import api from "../../api/api";

const UserInput = (props: any) => {
  const [input, setInput]: IUserInp = useState("");
  const compile = () => {

    api.post("/core/compile", {
      instructions : input,
    })

  };

  const execute = async() => {
    let response = await api.post("/core/execute", {
      instructions: input,
    });

    props.setRegisters(response.data)
  };
  return (
    <div className="col-span-5 row-span-4">
      <div className="flex justify-between">
        <UserInputTop>
          <Btn>
            <strong>B</strong>
          </Btn>
          <Btn>
            <i>I</i>
          </Btn>
          <Btn>
            <u>U</u>
          </Btn>
          <Btn>
            <del>S</del>
          </Btn>
          <Btn>
            X<sup>2</sup>
          </Btn>
          <Btn>
            X<sub>2</sub>
          </Btn>
          <Btn>
            <CodeIcon onClick={compile} />
          </Btn>
          <Btn>
            <PlayArrowIcon onClick={execute} />
          </Btn>
          <LongButton>merge tags</LongButton>
        </UserInputTop>
        <CoEx className="flex justify-around items-center">
          <div className="line pr-2 cursor-pointer" onClick={compile}>
            <CodeIcon />
            Compile
          </div>
          <div className="cursor-pointer pl-2" onClick={execute}>
            Execute <PlayArrowIcon />
          </div>
        </CoEx>
      </div>
      <StyledUserInput>
        <textarea onChange={(e) => setInput(e.target.value)}></textarea>
      </StyledUserInput>
    </div>
  );
};

export default UserInput;
