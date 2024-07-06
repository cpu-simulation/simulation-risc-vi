import { useState } from "react";
import { StyledRegister, StyledRegisters } from "./styledRegisters";

const Registers = (props:any) => {
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
          <div className="inline-block addr">{props.registers.AC}</div>
        </StyledRegister>
        <StyledRegister className="col-span-3">
          <div className="inline-block">
            AR<span className="sub">Address Register</span>
          </div>
          <div className="inline-block addr">{props.registers.AR}</div>
        </StyledRegister>
        <StyledRegister className="col-span-3">
          <div className="inline-block">
            DR<span className="sub">Data Register </span>
          </div>
          <div className="inline-block addr">{props.registers.DR}</div>
        </StyledRegister>
        <StyledRegister className="col-span-3">
          <div className="inline-block">
            PC<span className="sub">Program Counter</span>
          </div>
          <div className="inline-block addr">{props.registers.PC}</div>
        </StyledRegister>
        <StyledRegister className="col-span-3">
          <div className="inline-block">
            IR<span className="sub">Instruction Register</span>
          </div>
          <div className="inline-block addr">{props.registers.IR}</div>
        </StyledRegister>
        <StyledRegister className="col-span-3">
          <div className="inline-block">
            OUTR<span className="sub">Output Register</span>
          </div>
          <div className="inline-block addr">{props.registers.OUTR}</div>
        </StyledRegister>
        <StyledRegister className="col-span-3">
          <div className="inline-block">
            TR<span className="sub">Temporary Register</span>
          </div>
          <div className="inline-block addr">{props.registers.TR}</div>
        </StyledRegister>
        <StyledRegister className="col-span-3 flex">
          <div className="self-start">
            INTR<span className="sub">Input Register</span>
          </div>
          <div className="addr">{props.registers.INPR}</div>
        </StyledRegister>
      </div>
    </StyledRegisters>
  );
};

export default Registers;
