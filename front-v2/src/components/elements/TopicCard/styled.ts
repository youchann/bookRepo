import styled, { css } from "styled-components";
import { Card as OriginalCard } from "ingred-ui";

export const Card = styled(OriginalCard)<{ checked: boolean }>`
  cursor: pointer;
  display: flex;
  align-items: center;
  width: 1000px;
  min-height: 50px;
  border: 1px solid ${({ theme }) => theme.palette.divider};
  ${({ checked, theme }) =>
    checked &&
    css`
      background-color: ${theme.palette.background.active};
    `}
`;
