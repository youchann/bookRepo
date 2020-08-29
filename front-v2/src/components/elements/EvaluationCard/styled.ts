import styled from "styled-components";
import { Card as OriginalCard } from "ingred-ui";

export const Card = styled(OriginalCard)`
  border: 1px solid ${({ theme }) => theme.palette.divider};
`;
