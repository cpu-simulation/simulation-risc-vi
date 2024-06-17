import { createGlobalStyle } from "styled-components";
import jomolhari from '../fonts/Jomolhari/Jomolhari-Regular.ttf'

const GlobalStyle = createGlobalStyle`
  @font-face {
    font-family: jomolhari;
    src: url(${jomolhari}) format('truetype');
    font-weight: normal;
    font-style: normal;
  }
  body{
    background-color: ${({ theme }) => theme.body};
    color: ${({ theme }) => theme.text};
    transition: all ease-in-out 200ms;
    font-family: 'jomolhari';
  }

  *{
    cursor: default;
  }
`;

export default GlobalStyle;
