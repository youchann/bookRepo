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
import { useConfirmUser } from "../../../hooks/useConfirmUser";

const Search: React.FunctionComponent = () => {
  const theme = useTheme();
  const history = useHistory();
  useConfirmUser(history);

  const [text, setText] = React.useState<string>("");
  const [requesting, setRequesting] = React.useState<boolean>(false);
  const [keywords, setKeywords] = React.useState<string[]>([]);

  const getSuggestKeywords = async () => {
    setRequesting(true);
    setKeywords((await client.getSuggestKeywords()).data.keywords);
    setRequesting(false);
  };

  React.useEffect(() => {
    getSuggestKeywords();
  }, []);

  const nextPage = () => {
    // MEMO: スペースだとサーバーサイドで正規化時に意図通りの形態素解析ができないので「|」で区切る
    history.push(`/selectNounTopics?word=${text.replace(/\s+/g, "|")}`); // eslint-disable-line no-irregular-whitespace
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

  function handleClickReload() {
    getSuggestKeywords();
  }

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
        <Spacer pt={4} />
        <Flex display="flex" justifyContent="center" alignItems="center">
          <Typography weight="bold" size="xxl" color="secondary">
            下記の単語群からも入力可能です
          </Typography>
          <Spacer pl={2} />
          <ActionButton icon="search" onClick={handleClickReload}>
            再読み込み
          </ActionButton>
        </Flex>
        <Spacer pt={3} />
        {requesting ? (
          <Spinner />
        ) : (
          <Styled.KeywordsContainer>
            {keywords.map((keyword) => (
              <Spacer key={keyword} p={1}>
                <Styled.Button onClick={handleClickKeyword(keyword)}>
                  <Typography>{keyword}</Typography>
                </Styled.Button>
              </Spacer>
            ))}
          </Styled.KeywordsContainer>
        )}
        <Spacer py={2} />
        <Button inline disabled={text === ""} onClick={handleClickButton}>
          決定
        </Button>
        <Spacer pt={3} />
      </Flex>
    </>
  );
};

export { Search };
