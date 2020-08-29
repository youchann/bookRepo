import React from "react";
import * as Styled from "./styled";
import { Spacer, Flex, Typography, Input, Button, useTheme } from "ingred-ui";
import { useHistory } from "react-router";

const Search: React.FunctionComponent = () => {
  const theme = useTheme();
  const history = useHistory();
  const [text, setText] = React.useState<string>("");

  const nextPage = () => {
    history.push(`/selectSynonyms?word=${text}`);
  };

  function handleChangeInput(event: React.ChangeEvent<HTMLInputElement>) {
    setText(event.target.value);
  }

  function handleClickButton() {
    if (text === "") return;
    nextPage();
  }

  function handleEnter(event: React.KeyboardEvent<HTMLInputElement>) {
    if (event.key !== "Enter" || text === "") return;
    nextPage();
  }

  return (
    <>
      <Spacer pt={10} />
      <Flex display="flex" alignItems="center" flexDirection="column">
        <Typography weight="bold" size="xxxl">
          あなたの欲しい本に近しいキーワードを入力してください
        </Typography>
        <Typography weight="bold" size="xxl" color={theme.palette.danger.main}>
          ※１つ以上の名詞または形容詞を含めるようにしてください
        </Typography>
        <Spacer pt={6} />
        <Styled.InputContainer>
          <Input
            autoFocus
            placeholder="(例) 感動 泣ける 青春"
            value={text}
            onChange={handleChangeInput}
            onKeyDown={handleEnter}
          />
        </Styled.InputContainer>
        <Spacer pt={6} />
        <Button inline onClick={handleClickButton}>
          決定
        </Button>
      </Flex>
    </>
  );
};

export { Search };
