import { StyledCpu, StyledHeader } from "./styledCpu";
import HomeIcon from "@mui/icons-material/Home";
import PersonIcon from "@mui/icons-material/Person";
import UserInput from "../userInput/userInput";
import Memory from './../memory/Memory';
import Registers from '../registers/registers';
import States from '../states/states';
import { useState } from "react";

const Cpu = () => {
    const [registers, setRegisters] = useState({
      AC: "0x0",
      AR: "0x0",
      DR: "0x0",
      PC: "0x0",
      IR: "0x0",
      TR: "0x0",
      INPR: "0x0",
      OUTR: "0x0",
    });

    
    const [memory, setMemory] = useState([[0,0],[0,0]]); // get bulk read for this
    return (
      <>
        <StyledCpu className="flex flex-col items-center">
          <StyledHeader className="flex align-middle justify-between">
            <div className="hover:cursor-pointer ml-2">
              <HomeIcon />
            </div>
            <div className="hover:cursor-default text-xl font-light">
              Mano's basic computer simulator
            </div>
            <div className="hover:cursor-pointer mr-2">
              <PersonIcon />
            </div>
          </StyledHeader>

          <div className="grid grid-cols-7 grid-rows-7 w-[90%] gap-x-5 gap-y-2 mt-3 pb-[30px]">
            <UserInput
              registers={registers}
              setMemory={setMemory}
              setRegisters={setRegisters}
            />
            <Memory memory={memory} />
            <Registers registers={registers} />
            <States />
          </div>
        </StyledCpu>
      </>
    );
};

export default Cpu;
