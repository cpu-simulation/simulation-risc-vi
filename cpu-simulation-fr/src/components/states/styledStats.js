import styled from "styled-components";
import  Jockey_One  from "../../assets/fonts/Jockey_One/JockeyOne-Regular.ttf";

export const StyledStats = styled.div`
  background-color: ${({ theme }) => theme.cBody};
  border: solid 1px ${({ theme }) => theme.primary};
  padding: 10px;
  border-radius: 15px;
  position: relative;
  img {
    position: absolute;
    transform: scale(1.5);
    left: 130px;
    top: 14px;
  }
  img:hover {
    transform: scale(1.6);
    transition: all ease-in 500ms;
  }

  .texts {
    border-left: 4px solid rgba(51, 149, 94, 1);
    margin-top: 30px;
    padding-left: 10px;
  }
  .usage {
    @font-face {
      font-family: Jockey;
      src: url(${Jockey_One}) format("truetype");
      font-weight: normal;
      font-style: normal;
    }
    font-family: Jockey;
    font-size: xxx-large;
    line-height: 35px;
    margin-bottom: 70px;
  }
`;
