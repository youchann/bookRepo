import React from "react";
import ReactDom from "react-dom";
import { Global } from "@emotion/core";

import { globalStyle } from "./styles/globalStyle";

const initialization = async () => {
  try {
    ReactDom.render(
      <>
        <Global styles={globalStyle} />
        <div>hoge</div>
      </>,
      document.getElementById("root"),
    );
  } catch (e) {
    // eslint-disable-next-line no-console
    console.error(e);
  }
};

initialization();
