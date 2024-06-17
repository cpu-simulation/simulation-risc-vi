import { StyledStats } from "./styledStats";
import Img from "../../assets/svgs/states.svg";

const States = () => {
  return (
    <StyledStats className="col-span-2 row-span-3">
      <img src={Img} alt="" />
      <div className="texts">
        <div className="text-xs">usage</div>
        <div className="usage">21%</div>
        <div className="flex justify-between text-xs leading-5">
          <div>memory frequency</div>
          <div>4800 Mhr</div>
        </div>
        <div className="flex justify-between text-xs leading-5">
          <div>Temperature</div>
          <div>46 C</div>
        </div>
        <div className="flex justify-between text-xs leading-5">
          <div>Voltage</div>
          <div>753 mV</div>
        </div>
      </div>
      <div></div>
    </StyledStats>
  );
};

export default States;
