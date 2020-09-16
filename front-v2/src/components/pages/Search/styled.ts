import styled from "styled-components";

export const InputContainer = styled.div`
  & > input {
    width: 400px;
  }
`;

export const KeywordsContainer = styled.div`
  display: flex;
  flex-wrap: wrap;
  max-width: 1000px;
`;

export const Button = styled.div`
  display: flex;
  align-items: center;
  padding: ${({ theme }) => `${theme.spacing * 0.75}px ${theme.spacing}px`};
  border: 0;
  cursor: pointer;
  border-radius: ${({ theme }) => theme.radius}px;
  background-color: ${({ theme }) => theme.palette.background.hint};
  white-space: nowrap;
  transition: all 0.3s;
  &:hover {
    background-color: ${({ theme }) => theme.palette.background.active};
  }
`;
