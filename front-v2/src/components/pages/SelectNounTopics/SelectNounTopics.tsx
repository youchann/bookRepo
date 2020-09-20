import React from "react";
import { useHistory } from "react-router";
import { Spacer, Flex, Typography, Spinner, Button } from "ingred-ui";
import { Response } from "../../../client/types";
import { client } from "../../../client";
import { TopicCard } from "../../elements/TopicCard";
import { RootContext } from "../../container/RootContainer";

const SelectNounTopics: React.FunctionComponent = () => {
  const history = useHistory();
  const { selectedWords } = React.useContext(RootContext);
  const [requesting, setRequesting] = React.useState<boolean>(false);
  // NOTE: [book_id: number, words: string[]][]
  const [topics, setTopic] = React.useState<
    Response.ShowNounTopics["noun_topics"]
  >([]);
  const [selectedIndexes, setSelectedIndexes] = React.useState<Set<number>>(
    new Set<number>(),
  );
  const [activeIndex, setActiveIndex] = React.useState<number | null>(null);
  const [reflectedIndex, setRefrectedIndex] = React.useState<boolean>(true);

  React.useEffect(() => {
    const getTopics = async () => {
      setRequesting(true);
      const res = await client.getNounTopics({
        selected_keywords: selectedWords,
      });
      setTopic(res.data.noun_topics);
      setRequesting(false);
    };
    getTopics();
  }, [selectedWords]);

  React.useEffect(() => {
    if (activeIndex === null || reflectedIndex) return;
    const newSet = new Set(selectedIndexes);
    if (selectedIndexes.has(activeIndex)) {
      newSet.delete(activeIndex);
    } else {
      newSet.add(activeIndex);
    }
    setSelectedIndexes(newSet);
    setRefrectedIndex(true);
  }, [reflectedIndex]); // eslint-disable-line react-hooks/exhaustive-deps

  // MEMO: <TopicCard />の再レンダリングを防ぐために複雑な実装となっている
  const handleSelectIndex = React.useCallback((index: number) => {
    setActiveIndex(index);
    setRefrectedIndex(false);
  }, []);

  function handleClickButton() {
    const bookIds: number[] = [];
    selectedIndexes.forEach((index) => bookIds.push(topics[index][0]));
    history.push(`/selectBooks?book_ids=${bookIds.join(",")}`);
  }

  return (
    <Spacer pt={10}>
      <Flex display="flex" alignItems="center" flexDirection="column">
        <Typography weight="bold" size="xxxl">
          あなたが欲しい本に近いイメージの単語群をなるべく多く選択してください
        </Typography>
        <Spacer pt={6} />
        {requesting ? (
          <Spinner />
        ) : (
          topics.map((topic, index) => (
            // eslint-disable-next-line react/no-array-index-key
            <Spacer key={index} py={2}>
              <TopicCard
                index={index}
                words={topic[1]}
                onClick={handleSelectIndex}
              />
            </Spacer>
          ))
        )}
        <Spacer pt={6} />
        <Button
          inline
          disabled={selectedIndexes.size === 0}
          onClick={handleClickButton}
        >
          決定
        </Button>
      </Flex>
    </Spacer>
  );
};

export { SelectNounTopics };
