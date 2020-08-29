import styled from "styled-components";
import { CARD_WIDTH } from "../../elements/BookCard";

export const BooksContainer = styled.div`
  display: grid;
  grid-auto-rows: auto; /* 初期値 */
  grid-template-columns: repeat(auto-fit, ${CARD_WIDTH});
  grid-gap: ${({ theme }) => `${theme.spacing * 2}px`};
  justify-content: center;
  /* MEMO: card4枚分 */
  width: calc(${CARD_WIDTH} * 4 + ${({ theme }) => theme.spacing * 2 * 3}px);
`;
