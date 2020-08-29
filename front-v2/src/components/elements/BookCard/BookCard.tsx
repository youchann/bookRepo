import React from "react";
import * as Styled from "./styled";
import { Spacer, Checkbox } from "ingred-ui";

type Props = {
  id: number;
  name: string;
  imageUrl: string;
  checked: boolean;
  onSelect: (id: number) => void;
};

const BookCard: React.FunctionComponent<Props> = ({
  id,
  name,
  imageUrl,
  checked,
  onSelect,
}) => {
  const handleSelect = (id: number) =>
    function () {
      onSelect(id);
    };
  return (
    <Styled.Card checked={checked}>
      <Spacer pt={1} />
      <img height="200px" width="150px" src={imageUrl} />
      <Spacer pt={0.5} />
      <Styled.Link
        href={`https://bookmeter.com/books/${id}`}
        target="_blank"
        rel="noreferrer"
      >
        {name}
      </Styled.Link>
      <Styled.Divider my={1} />
      <Checkbox checked={checked} onChange={handleSelect(id)} />
    </Styled.Card>
  );
};

export { BookCard };
