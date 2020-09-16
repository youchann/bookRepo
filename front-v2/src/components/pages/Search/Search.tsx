import React from "react";
import * as Styled from "./styled";
import {
  Spacer,
  Flex,
  Typography,
  Input,
  Button,
  useTheme,
  Spinner,
  ActionButton,
} from "ingred-ui";
import { useHistory } from "react-router";
import { client } from "../../../client";

const Search: React.FunctionComponent = () => {
  const theme = useTheme();
  const history = useHistory();
  const [text, setText] = React.useState<string>("");
  const [requesting, setRequesting] = React.useState<boolean>(false);
  const [keywords, setKeywords] = React.useState<string[]>([]);

  React.useEffect(() => {
    const getSuggestKeywords = async () => {
      setRequesting(true);
      setKeywords((await client.getSuggestKeywords()).data.keywords);
      setRequesting(false);
    };
    getSuggestKeywords();
  }, []);

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

  const handleClickKeyword = (keyword: string) => {
    return function () {
      setText(text === "" ? keyword : `${text} ${keyword}`);
    };
  };

  return (
    <>
      <Spacer pt={10} />
      <Flex display="flex" alignItems="center" flexDirection="column">
        <Typography weight="bold" size="xxxl">
          あなたの欲しい本に近しいキーワードをなるべく多く入力してください
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
            onKeyPress={handleEnter}
          />
        </Styled.InputContainer>
        {requesting ? (
          <Spinner />
        ) : (
          <Spacer py={4}>
            <Typography
              weight="bold"
              size="xxl"
              align="center"
              color="secondary"
            >
              下記の単語群からも入力可能です
            </Typography>
            <Spacer pt={3} />
            <Styled.KeywordsContainer>
              {keywords.map((keyword) => (
                <Spacer key={keyword} p={1}>
                  <Styled.Button onClick={handleClickKeyword(keyword)}>
                    <Typography>{keyword}</Typography>
                  </Styled.Button>
                </Spacer>
              ))}
            </Styled.KeywordsContainer>
          </Spacer>
        )}
        <Button inline onClick={handleClickButton}>
          決定
        </Button>
      </Flex>
    </>
  );
};

export { Search };
