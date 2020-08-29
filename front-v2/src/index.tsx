import React from "react";
import ReactDom from "react-dom";
import { ThemeProvider, createTheme } from "ingred-ui";
import { Global } from "@emotion/core";

import { globalStyle } from "./styles/globalStyle";
import { Router } from "./router";
import { RootContainer } from "./components/container/RootContainer";

const initialization = async () => {
  const theme = createTheme();
  try {
    ReactDom.render(
      <ThemeProvider theme={theme}>
        <Global styles={globalStyle} />
        <RootContainer>
          <Router />
        </RootContainer>
      </ThemeProvider>,
      document.getElementById("root"),
    );
  } catch (e) {
    // eslint-disable-next-line no-console
    console.error(e);
  }
};

initialization();
