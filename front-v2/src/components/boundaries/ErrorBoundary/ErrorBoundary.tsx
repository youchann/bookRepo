import React from "react";
import shallowEqual from "shallowequal";
import { Flex, Typography, Button, Spacer } from "ingred-ui";

export type Props = {
  children: React.ReactNode;
};

type State = {
  hasError: boolean;
};

export class ErrorBoundary extends React.PureComponent<Props, State> {
  public state: State = {
    hasError: false,
  };

  public componentDidUpdate(prevProps: Props): void {
    if (
      this.state.hasError === true &&
      !shallowEqual(this.props.children, prevProps.children)
    ) {
      this.setState({
        hasError: false,
      });
    }
  }

  public componentDidCatch(): void {
    this.setState({
      hasError: true,
    });
  }

  public render(): React.ReactNode {
    const { props, state, handleClickButton } = this;

    return !state.hasError ? (
      props.children
    ) : (
      <Flex
        display="flex"
        justifyContent="center"
        alignItems="center"
        flexDirection="column"
      >
        <Spacer pt={10} />
        <Typography size="xxxl" weight="bold">
          エラーが起きました。何度も起こる場合は管理者に問い合わせください。
        </Typography>
        <Spacer pt={3} />
        <Button inline onClick={handleClickButton}>
          トップページに戻る
        </Button>
      </Flex>
    );
  }

  public handleClickButton(): void {
    window.location.href = "/";
  }
}
