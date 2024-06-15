import styled from "styled-components";
import PressStart2P from "../../assets/fonts/Press_Start_2P/PressStart2P-Regular.ttf";

export const StyledUserInput = styled.div`
  background-color: ${({ theme }) => theme.cBody};
  border: solid 1px ${({ theme }) => theme.primary};
  padding: 10px 20px;
  border-radius: 0px 15px 15px 15px;
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

export const UserInputTop = styled.div`
  background-color: ${({ theme }) => theme.cBody};
  border: solid 1px ${({ theme }) => theme.primary};
  border-bottom: none;
  padding: 10px 20px;
  border-radius: 15px 15px 0px 0px;
  margin-bottom: -2px;
`;

export const Btn = styled.button`
  width: 30px;
  height: 30px;
  padding: 5px;
  border-radius: 100px;
  border: solid 2px ${({ theme }) => theme.primary};
  background-image: radial-gradient(
    ${({ theme }) => theme.primary},
    ${({ theme }) => theme.background},
    ${({ theme }) => theme.cBody}
  );
  margin-right: 10px;
`;

export const LongButton = styled(Btn)`
  width: auto;
  margin-right: 0px;
`

export const CoEx = styled.div`
  background-color: ${({ theme }) => theme.cBody};
  border: solid 1px ${({ theme }) => theme.primary};
  padding: 0px 20px;
  border-radius: 40px;
  .line {
    border-right:1px solid ${({theme})=> theme.text};
  }
`;