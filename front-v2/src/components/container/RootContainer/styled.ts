import styled from "styled-components";

const HEADER_HEIGHT = "60px";

export const Container = styled.div`
  display: flex;
  flex-direction: column;
  width: 100vw;
  height: 100%;
`;

export const Header = styled.div`
  display: flex;
  align-items: center;
  padding: ${({ theme }) => theme.spacing * 2}px;
  height: ${HEADER_HEIGHT};
  border-bottom: 1px solid ${({ theme }) => theme.palette.divider};
`;

export const Content = styled.div`
  height: calc(100vh - ${HEADER_HEIGHT});
`;
