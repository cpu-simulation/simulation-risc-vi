import styled from "styled-components";

export const StyledMemory = styled.div`
  background-color: ${({ theme }) => theme.cBody};
  border: solid 1px ${({ theme }) => theme.primary};
  padding: 10px;
  border-radius: 15px;

  input {
    width: 100%;
    border-radius: 15px;
    border: solid 1px ${({ theme }) => theme.primary};
    background-color: ${({ theme }) => theme.background};
    padding: 2px 8px;
    outline: none;
    box-shadow: inset 0 0 8px ${({ theme }) => theme.cBody};
  }
  input::placeholder {
    color: ${({ theme }) => theme.text};
  }
  .cells-body {
    background-color: ${({ theme }) => theme.background};
    width: 100%;
    border-radius: 15px;
    overflow-y: scroll;
    height: 280px;
    padding: 6px;
    border-radius: 15px;
    border: solid 1px ${({ theme }) => theme.primary};
    margin-top: 8px;
    /* &::-webkit-scrollbar {
      width: 30px;
    }
    &::-webkit-scrollbar-track {
      box-shadow: inset 0 0 5px grey;
      border-radius: 10px;
    }
    &::-webkit-scrollbar-thumb {
      background: red;
      border-radius: 10px;
    } */
  }

  .cell {
    text-align: center;
    padding: 8px;
    filter: blur();
    height: 36px;
    border-radius: 8px;
    border: solid 1px ${({ theme }) => theme.primary};
    margin-bottom: 4px;
    background-image: radial-gradient(
      ${({ theme }) => theme.cBody},
      ${({ theme }) => theme.background},
      ${({ theme }) => theme.primary}
    );
  }
`;
