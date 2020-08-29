import React from "react";
import * as Styled from "./styled";
import {
  Spacer,
  Flex,
  Typography,
  TextField,
  Button,
  Spinner,
} from "ingred-ui";
import { useHistory } from "react-router";
import { client } from "../../../client";

const Home: React.FunctionComponent = () => {
  const history = useHistory();
  const [requesting, setRequesting] = React.useState<boolean>(false);
  const [studentNumber, setStudentNumber] = React.useState<string>("");

  const nextPage = async () => {
    setRequesting(true);
    try {
      const res = await client.registerUser({
        student_number: +studentNumber,
      });
      localStorage.setItem("userId", `${res.data.id}`);
      history.push(`/search`);
    } catch (e) {
      setRequesting(false);
      window.confirm(
        "エラーが起きました。なんども起きる場合は管理者にお問い合わせください。",
      );
      console.error(e); // eslint-disable-line no-console
    }
  };

  const validate = () => studentNumber === "" || isNaN(+studentNumber);

  function handleChangeInput(event: React.ChangeEvent<HTMLInputElement>) {
    setStudentNumber(event.target.value);
  }

  function handleClickButton() {
    nextPage();
  }

  function handleEnter(event: React.KeyboardEvent<HTMLInputElement>) {
    if (event.key !== "Enter") return;
    if (validate()) return;
    nextPage();
  }

  return (
    <>
      <Spacer pt={10} />
      <Flex display="flex" alignItems="center" flexDirection="column">
        <Typography weight="bold" size="xxxl">
          学籍番号を入力してください
        </Typography>
        <Spacer pt={6} />
        {requesting ? (
          <Spinner />
        ) : (
          <>
            <Styled.InputContainer>
              <Typography weight="bold">学籍番号</Typography>
              <Spacer pt={0.5} />
              <TextField
                autoFocus
                placeholder="(例) 12345678"
                value={studentNumber}
                errorText={
                  isNaN(+studentNumber) ? "数値を入力してください" : ""
                }
                onChange={handleChangeInput}
                onKeyDown={handleEnter}
              />
            </Styled.InputContainer>
            <Spacer pt={6} />
            <Button inline disabled={validate()} onClick={handleClickButton}>
              決定
            </Button>
          </>
        )}
      </Flex>
    </>
  );
};

export { Home };
