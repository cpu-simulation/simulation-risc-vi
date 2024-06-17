import { StyledRegister, StyledRegisters } from "./styledRegisters";

const Registers = () => {
  return (
    <StyledRegisters className="col-span-5 row-span-3">
      <div className="top">
        <span>Registers</span>
      </div>
      <div className="grid grid-cols-6 mt-2 gap-x-2 gap-y-1">
        <StyledRegister className="col-span-3">
          <div className="inline-block">
            AC<span className="sub">accmulator</span>
          </div>
          <div className="inline-block addr">OX894F</div>
        </StyledRegister>
        <StyledRegister className="col-span-3">
          <div className="inline-block">
            AR<span className="sub">Address Register</span>
          </div>
          <div className="inline-block addr">OX387</div>
        </StyledRegister>
        <StyledRegister className="col-span-3">
          <div className="inline-block">
            DR<span className="sub">Data Register </span>
          </div>
          <div className="inline-block addr">OXFF11</div>
        </StyledRegister>
        <StyledRegister className="col-span-3">
          <div className="inline-block">
            PC<span className="sub">Program Counter</span>
          </div>
          <div className="inline-block addr">OX290</div>
        </StyledRegister>
        <StyledRegister className="col-span-3">
          <div className="inline-block">
            IR<span className="sub">Instruction Register</span>
          </div>
          <div className="inline-block addr">OX45EB</div>
        </StyledRegister>
        <StyledRegister className="col-span-3">
          <div className="inline-block">
            OUTR<span className="sub">Output Register</span>
          </div>
          <div className="inline-block addr">OXF1</div>
        </StyledRegister>
        <StyledRegister className="col-span-3">
          <div className="inline-block">
            TR<span className="sub">Temporary Register</span>
          </div>
          <div className="inline-block addr">OX8B4F</div>
        </StyledRegister>
        <StyledRegister className="col-span-3 flex">
          <div className="self-start">
            INTR<span className="sub">Input Register</span>
          </div>
          <div className="addr">OX04</div>
        </StyledRegister>
      </div>
    </StyledRegisters>
  );
};

export default Registers;
