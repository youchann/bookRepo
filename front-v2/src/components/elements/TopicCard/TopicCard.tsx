import React from "react";
import * as Styled from "./styled";
import { Spacer, Checkbox, Flex } from "ingred-ui";

type Props = {
  index: number;
  words: string[];
  onClick: (index: number) => void;
};

const TopicCard: React.FunctionComponent<Props> = ({
  index,
  words,
  onClick,
}) => {
  const [checked, setChecked] = React.useState<boolean>(false);
  function handleClick() {
    setChecked(!checked);
    onClick(index);
  }
  return (
    <Styled.Card checked={checked} onClick={handleClick}>
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
};

export { TopicCard };
