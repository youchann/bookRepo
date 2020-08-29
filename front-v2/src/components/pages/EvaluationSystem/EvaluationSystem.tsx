import React from "react";
import * as Styled from "./styled";
import { Spacer, Flex, Typography, Spinner, Button } from "ingred-ui";
import { useHistory } from "react-router";
import { client } from "../../../client";
import { Response } from "../../../client/types";
import { EvaluationCard } from "../../elements/EvaluationCard";
import { useConfirmUser } from "../../../hooks/useConfirmUser";

type EvaluationData = {
  [id: number]: number;
};

const EvaluationSystem: React.FunctionComponent = () => {
  const history = useHistory();
  const [requesting, setRequesting] = React.useState<boolean>(false);
  const [evaluationItems, setEvaluationItems] = React.useState<
    Response.EvaluationItems["evaluation_list"]
  >([]);
  const [evaluationData, setEvaluationData] = React.useState<EvaluationData>(
    {},
  );

  useConfirmUser(history);

  React.useEffect(() => {
    const getEvaluationItems = async () => {
      setRequesting(true);
      const res = await client.getEvaluationItems();
      setEvaluationItems(res.data.evaluation_list);
      setRequesting(false);
    };
    getEvaluationItems();
  }, []);

  React.useEffect(() => {
    const data: EvaluationData = {};
    for (const evaluationItem of evaluationItems) {
      data[evaluationItem.id] = 2;
    }
    setEvaluationData(data);
  }, [evaluationItems]);

  const handleChangeEvaluation = (id: number) =>
    function (evaluation: number) {
      const data = { ...evaluationData };
      data[id] = evaluation;
      setEvaluationData(data);
    };

  async function handleClickButton() {
    const userId = localStorage.getItem("userId");
    const normalizedData = Object.keys(evaluationData).map((id) => ({
      evaluation_id: +id,
      evaluation: evaluationData[+id],
    }));
    if (userId !== null) {
      setRequesting(true);
      await client.saveEvaluationData({
        user_id: +userId,
        evaluation_data: normalizedData,
      });
      setRequesting(false);
      history.push(`/end`);
    }
  }

  return (
    <>
      <Spacer pt={10} />
      <Flex display="flex" alignItems="center" flexDirection="column">
        <Typography weight="bold" size="xxxl">
          システムの評価をしてください
        </Typography>
        <Spacer pt={6} />
        {requesting ? (
          <Spinner />
        ) : (
          <Styled.EvaluationItemsContainer>
            {evaluationItems.map((item) => (
              <Spacer key={item.id} py={2}>
                <EvaluationCard
                  description={item.description}
                  value={evaluationData[item.id] as number}
                  onChange={handleChangeEvaluation(item.id)}
                />
              </Spacer>
            ))}
          </Styled.EvaluationItemsContainer>
        )}
        <Spacer py={6}>
          <Button inline onClick={handleClickButton}>
            決定
          </Button>
        </Spacer>
      </Flex>
    </>
  );
};

export { EvaluationSystem };
