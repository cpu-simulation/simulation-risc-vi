import styled from "styled-components";
import PressStart2P from "../../assets/fonts/Press_Start_2P/PressStart2P-Regular.ttf";

export const StyledUserInput = styled.div`
  background-color: ${({ theme }) => theme.cBody};
  border: solid 1px ${({ theme }) => theme.primary};
  padding: 10px 20px;
  border-radius: 15px;
  textarea {
    @font-face {
      font-family: PressStart2P;
      src: url(${PressStart2P}) format("truetype");
      font-weight: normal;
      font-style: normal;
    }
    font-family: PressStart2P;
    line-height: 20px;
    font-size: 10px;
    width: 100%;
    height: 250px;
    margin-top: 50px;
    border-radius: 15px;
    border: solid 1px ${({ theme }) => theme.primary};
    background-color: ${({ theme }) => theme.background};
    resize: none;
    padding: 20px 20px;
    outline: none;
    overflow: scroll;
  }
  textarea::-webkit-scrollbar {
    display: none;
  }
`;
