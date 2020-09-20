import React from "react";
import * as Styled from "./styled";
import { Typography } from "ingred-ui";
import { ErrorBoundary } from "../../boundaries/ErrorBoundary";

const RootContainer: React.FunctionComponent = ({ children }) => {
  return (
    <Styled.Container>
      <Styled.Header>
        <Typography component="h1" size="xxl" weight="bold">
          いい感じに本を探すやつ
        </Typography>
      </Styled.Header>
      <ErrorBoundary>
        <Styled.Content>{children}</Styled.Content>
      </ErrorBoundary>
    </Styled.Container>
  );
};

export { RootContainer };
