import React from "react";
import * as Styled from "./styled";
import { Spacer, Flex, Divider, Typography, RadioButton } from "ingred-ui";

type Props = {
  description: string;
  value: number;
  onChange: (value: number) => void;
};

const EvaluationCard: React.FunctionComponent<Props> = ({
  description,
  value,
  onChange,
}) => {
  function handleChange(event: React.ChangeEvent<HTMLInputElement>) {
    onChange(+event.target.value);
  }
  return (
    <Styled.Card>
      <Flex display="flex" alignItems="center">
        <Spacer p={2}>
          <Typography weight="bold">{description}</Typography>
        </Spacer>
      </Flex>
      <Divider />
      <Flex
        display="flex"
        alignItems="center"
        justifyContent="center"
        height="50px"
      >
        <Typography weight="bold" component="div">
          はい
        </Typography>
        <Spacer pl={3} />
        <Flex display="flex" alignItems="center" height="50px">
          {[...Array(4)].map((_, i) => (
            // eslint-disable-next-line react/no-array-index-key
            <Spacer key={i} px={2}>
              <RadioButton
                value={i + 1}
                checked={value === i + 1}
                onChange={handleChange}
              />
            </Spacer>
          ))}
        </Flex>
        <Spacer pl={3} />
        <Typography weight="bold" component="div">
          いいえ
        </Typography>
      </Flex>
    </Styled.Card>
  );
};

export { EvaluationCard };
