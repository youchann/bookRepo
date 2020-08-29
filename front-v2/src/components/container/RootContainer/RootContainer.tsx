import React from "react";
import * as Styled from "./styled";
import { Typography } from "ingred-ui";

type RootContextType = {
  selectedWords: string[];
  addSelectedWords: (words: string[]) => void;
};

export const RootContext = React.createContext<RootContextType>({
  selectedWords: [],
  addSelectedWords: () => {}, // eslint-disable-line @typescript-eslint/no-empty-function
});

const RootContainer: React.FunctionComponent = ({ children }) => {
  const [selectedWords, setSelectedWords] = React.useState<string[]>([]);
  const addSelectedWords = (words: string[]) => {
    setSelectedWords(words);
  };
  return (
    <RootContext.Provider value={{ selectedWords, addSelectedWords }}>
      <Styled.Container>
        <Styled.Header>
          <Typography component="h1" size="xxl" weight="bold">
            いい感じに本を探すやつ
          </Typography>
        </Styled.Header>
        <Styled.Content>{children}</Styled.Content>
      </Styled.Container>
    </RootContext.Provider>
  );
};

export { RootContainer };
