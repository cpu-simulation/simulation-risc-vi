import { StyledCpu, StyledHeader } from "./styledCpu";
import HomeIcon from "@mui/icons-material/Home";
import PersonIcon from "@mui/icons-material/Person";

const Cpu = () => {
  return (
    <StyledCpu className="relative">
      <StyledHeader className="flex absolute align-middle justify-between">
        <div className="hover:cursor-pointer ml-2">
          <HomeIcon />
        </div>
        <div className="hover:cursor-default text-xl font-light self-center">
          HELLO! <sub>welcome to the Simulation page</sub>
        </div>
        <div className="hover:cursor-pointer mr-2">
          <PersonIcon />
        </div>
      </StyledHeader>
    </StyledCpu>
  );
};

export default Cpu;
