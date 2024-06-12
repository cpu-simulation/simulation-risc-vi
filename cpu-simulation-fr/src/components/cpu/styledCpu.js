import styled from "styled-components";

export const StyledCpu = styled.div`
  background-image: radial-gradient(
    circle at 50% 10%,
    ${({ theme }) => theme.secondary},
    ${({ theme }) => theme.primary},
    ${({ theme }) => theme.background},
    ${({ theme }) => theme.cBody}
  );
  width: 75vw;
  min-height: 90vh;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  border: 2px solid ${({ theme }) => theme.primary};
  border-radius: 15px;
`;

export const StyledHeader = styled.div`
  background-color: ${({ theme }) => theme.cBody};
  padding: 10px;
  width: 90%;
  /* left: 50%;
  transform: translateX(-50%); */
  margin-top: 30px;
  border-radius: 50px;
  border: solid 2px ${({ theme }) => theme.primary};
`;
