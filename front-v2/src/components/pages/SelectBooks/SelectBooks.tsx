import React from "react";
import * as Styled from "./styled";
import * as queryString from "query-string";
import { Spacer, Flex, Typography, Spinner, Button } from "ingred-ui";
import { useHistory } from "react-router";
import { client } from "../../../client";
import { Response } from "../../../client/types";
import { BookCard } from "../../elements/BookCard";
import { useConfirmUser } from "../../../hooks/useConfirmUser";

const SelectBooks: React.FunctionComponent = () => {
  const history = useHistory();
  useConfirmUser(history);

  const [requesting, setRequesting] = React.useState<boolean>(false);
  const [books, setBooks] = React.useState<Response.GetBooks["info_list"]>([]);
  const [selectedBookIds, setSelectedBookIds] = React.useState<Set<number>>(
    new Set<number>(),
  );

  React.useEffect(() => {
    const parsedParam = queryString.parse(location.search.slice(1), {
      arrayFormat: "comma",
      parseNumbers: true,
    });
    const getBooks = async () => {
      setRequesting(true);
      const res = await client.getBooks({
        book_ids: (parsedParam["book_ids"] as number[]) || [],
      });
      setBooks(res.data.info_list);
      setRequesting(false);
    };
    getBooks();
  }, []);

  function handleSelectBook(id: number) {
    const newSet = new Set(selectedBookIds);
    if (selectedBookIds.has(id)) {
      newSet.delete(id);
    } else {
      newSet.add(id);
    }
    setSelectedBookIds(newSet);
  }

  async function handleClickButton() {
    const bookIds: number[] = [];
    selectedBookIds.forEach((bookId) => bookIds.push(bookId));
    const userId = localStorage.getItem("userId");
    if (bookIds.length !== 0 && userId !== null) {
      setRequesting(true);
      await client.registerBookIds({ user_id: +userId, book_ids: bookIds });
      setRequesting(false);
      history.push(`/evaluationSystem`);
    } else {
      history.push(`/evaluationSystem`);
    }
  }

  return (
    <>
      <Spacer pt={10} />
      <Flex display="flex" alignItems="center" flexDirection="column">
        <Typography weight="bold" size="xxxl" align="center">
          興味を持った本を選択してください
          <br />
          ※タイトルのリンクからあらすじを参照できます
        </Typography>
        <Spacer pt={6} />
        {requesting ? (
          <Spinner />
        ) : (
          <>
            <Styled.BooksContainer>
              {books.map((book) => (
                <BookCard
                  key={book.id}
                  id={book.id}
                  name={book.name}
                  imageUrl={book.image_url}
                  checked={selectedBookIds.has(book.id)}
                  onSelect={handleSelectBook}
                />
              ))}
            </Styled.BooksContainer>
            <Spacer pt={6} />
            <Button inline onClick={handleClickButton}>
              決定
            </Button>
          </>
        )}
      </Flex>
    </>
  );
};

export { SelectBooks };
