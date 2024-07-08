import { Dispatch, SetStateAction } from "react";

type tupple = [number,number]
export type IMemCells = [tupple[], Dispatch<SetStateAction<tupple[]>>]

export type IUserInp = [string, Dispatch<SetStateAction<string>>];