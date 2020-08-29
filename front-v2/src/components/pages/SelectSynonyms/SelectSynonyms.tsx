import React from "react";
import * as Styled from "./styled";
import * as queryString from "query-string";
import { useHistory } from "react-router";
import { client } from "../../../client";
import { Spacer, Flex, Typography, Checkbox, Spinner, Button } from "ingred-ui";
import { RootContext } from "../../container/RootContainer";

const SelectSynonyms: React.FunctionComponent = () => {
  const history = useHistory();
  const parsed = queryString.parse(location.search);
  const inputedWord = parsed["word"];
  if (typeof inputedWord !== "string") history.replace("/");

  const { addSelectedWords } = React.useContext(RootContext);
  const [requesting, setRequesting] = React.useState<boolean>(false);
  const [synonyms, setSynonyms] = React.useState<string[]>([]);
  const [selectedSynonyms, setSelectedSynonyms] = React.useState<Set<string>>(
    new Set<string>(),
  );

  React.useEffect(() => {
    const getSynonyms = async () => {
      setRequesting(true);
      const res = await client.getSynonyms({ keyword: inputedWord as string }); // MEMO: 前の処理で型を保証済み
      setSelectedSynonyms(
        new Set<string>([
          ...res.data.analyzed_keywords.adjective,
          ...res.data.analyzed_keywords.noun,
        ]),
      );
      setSynonyms(res.data.similar_words);
      setRequesting(false);
    };
    getSynonyms();
  }, [inputedWord]);

  function handleSelectSynonym(event: React.ChangeEvent<HTMLInputElement>) {
    const newSet = new Set(selectedSynonyms);
    if (event.target.checked) {
      newSet.add(event.target.value);
    } else {
      newSet.delete(event.target.value);
    }
    setSelectedSynonyms(newSet);
  }

  function handleClickButton() {
    const synonymsArray: string[] = [];
    selectedSynonyms.forEach((synonym) => synonymsArray.push(synonym));
    addSelectedWords(synonymsArray);
    history.push("/selectAdjectiveTopics");
  }

  return (
    <Spacer pt={10}>
      <Flex display="flex" alignItems="center" flexDirection="column">
        <Typography weight="bold" size="xxxl">
          あなたが欲しい本と関連の近い単語を選択してください
        </Typography>
        <Spacer pt={6} />
        {requesting ? (
          <Spinner />
        ) : (
          <>
            <Styled.CheckboxesContainer>
              <Flex display="flex" flexWrap="wrap" flexShrink={0}>
                {synonyms.map((synonym) => (
                  <Spacer key={synonym} p={2}>
                    <Checkbox
                      checked={selectedSynonyms.has(synonym)}
                      value={synonym}
                      onChange={handleSelectSynonym}
                    >
                      {synonym}
                    </Checkbox>
                  </Spacer>
                ))}
              </Flex>
            </Styled.CheckboxesContainer>
            <Spacer pt={6} />
            <Button
              inline
              disabled={selectedSynonyms.size === 0}
              onClick={handleClickButton}
            >
              決定
            </Button>
          </>
        )}
      </Flex>
    </Spacer>
  );
};

export { SelectSynonyms };
