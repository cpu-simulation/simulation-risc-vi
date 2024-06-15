import { Dispatch, SetStateAction } from "react";

export type IMemCells = [number[], Dispatch<SetStateAction<number[]>>]

export type IUserInp = [string, Dispatch<SetStateAction<string>>];