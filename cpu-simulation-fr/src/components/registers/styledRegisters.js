import styled from "styled-components";

export const StyledRegisters = styled.div`
  background-color: ${({ theme }) => theme.cBody};
  border: 1px solid ${({ theme }) => theme.primary};
  border-radius: 15px;
  padding: 20px 10px;
  && > .top > span {
    font-size: 20px;
    margin: 0px 15px;
  }
`;

export const StyledRegister = styled.div`
  border: solid 1px ${({ theme }) => theme.primary};
  background-color: ${({ theme }) => theme.background};
  border-radius: 10px;
  padding: 2px 4px;
  box-shadow: inset 0 0 8px ${({ theme }) => theme.cBody};
  margin-bottom: 5px;
  && div:first-child {
    background-image: radial-gradient(
      ${({ theme }) => theme.cBody},
      ${({ theme }) => theme.primary},
      ${({ theme }) => theme.secondary}
    );
    border: solid 1px ${({ theme }) => theme.cBody};
    border-radius: 15px;
    padding: 3px 5px;
    width: 38%;
    font-size: 1vw;
    text-align: center;
  }
  .sub {
    font-size: 0.6vw;
    margin-left: 4px;
  }
  .addr {
    width: 13vw;
    text-align: center;
  }
`;
