import React from "react";
import * as Styled from "./styled";
import { Spacer, Checkbox, Flex } from "ingred-ui";

type Props = {
  words: string[];
  checked: boolean;
  onClick?: () => void;
};

const TopicCard: React.FunctionComponent<Props> = ({
  words,
  checked,
  onClick,
}) => (
  <Styled.Card checked={checked} onClick={onClick}>
    <Spacer pt={0.5} px={2}>
      <Checkbox checked={checked} />
    </Spacer>
    <Flex display="flex" flexWrap="wrap">
      {words.map((word) => (
        <Spacer key={word} px={1}>
          {word}
        </Spacer>
      ))}
    </Flex>
  </Styled.Card>
);

export { TopicCard };
