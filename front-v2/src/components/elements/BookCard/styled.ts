import styled, { css } from "styled-components";
import { Card as OriginalCard, Divider as OriginalDivider } from "ingred-ui";

export const CARD_WIDTH = "230px";

export const Card = styled(OriginalCard)<{ checked: boolean }>`
  display: flex;
  flex-direction: column;
  align-items: center;
  width: ${CARD_WIDTH};
  height: 282px;
  border: 1px solid ${({ theme }) => theme.palette.divider};
  ${({ checked, theme }) =>
    checked &&
    css`
      background-color: ${theme.palette.background.active};
    `}
`;

export const Link = styled.a`
  display: block;
  width: inherit;
  text-align: center;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
`;

export const Divider = styled(OriginalDivider)`
  width: 100%;
`;
