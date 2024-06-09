import { createGlobalStyle } from "styled-components";

const GlobalStyle = createGlobalStyle`
  body{
    background-color: ${({ theme }) => theme.body};
    color: ${({ theme }) => theme.text};
    transition: all ease-in-out 200ms;
  }
`;

export default GlobalStyle;
