import React from "react";
import { Spacer, Flex, Typography } from "ingred-ui";
import { useHistory } from "react-router";
import { useConfirmUser } from "../../../hooks/useConfirmUser";

const End: React.FunctionComponent = () => {
  const history = useHistory();
  useConfirmUser(history);
  return (
    <>
      <Spacer pt={10} />
      <Flex display="flex" alignItems="center" flexDirection="column">
        <Typography weight="bold" size="xxxl">
          実験は以上です。お疲れ様でした。
        </Typography>
      </Flex>
    </>
  );
};

export { End };
