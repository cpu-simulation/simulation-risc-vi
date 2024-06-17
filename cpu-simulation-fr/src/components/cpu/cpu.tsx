import { StyledCpu, StyledHeader } from "./styledCpu";
import HomeIcon from "@mui/icons-material/Home";
import PersonIcon from "@mui/icons-material/Person";
import UserInput from "../userInput/userInput";
import Memory from './../memory/Memory';
import Registers from '../registers/registers';
import States from '../states/states';

const Cpu = () => {
  return (
    <>
      <StyledCpu className="flex flex-col items-center">
        <StyledHeader className="flex align-middle justify-between">
          <div className="hover:cursor-pointer ml-2">
            <HomeIcon />
          </div>
          <div className="hover:cursor-default text-xl font-light">
            HELLO! <sub>welcome to the Simulation page</sub>
          </div>
          <div className="hover:cursor-pointer mr-2">
            <PersonIcon />
          </div>
        </StyledHeader>

        <div className="grid grid-cols-7 grid-rows-7 w-[90%] gap-x-5 gap-y-2 mt-3 pb-[30px]">
          <UserInput />
          <Memory />
          <Registers />
          <States />
        </div>
      </StyledCpu>
    </>
  );
};

export default Cpu;
