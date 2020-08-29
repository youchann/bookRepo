import * as React from "react";
import { History } from "history";

export function useConfirmUser(history: History<History.UnknownFacade>) {
  React.useEffect(() => {
    const userId = localStorage.getItem("userId");
    if (userId === null || isNaN(+userId)) {
      window.confirm("エラーが起きました。トップ画面からやり直してください。");
      history.replace("/");
    }
  }, [history]);
}
