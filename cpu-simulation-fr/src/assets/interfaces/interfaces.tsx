import { Dispatch, SetStateAction } from "react";

export type IMemCells = [string[], Dispatch<SetStateAction<string[]>>]

export type IUserInp = [string, Dispatch<SetStateAction<string>>];