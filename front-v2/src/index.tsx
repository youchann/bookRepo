import React from "react";
import ReactDom from "react-dom";
import styled from "styled-components";
import { ThemeProvider, createTheme, Typography } from "ingred-ui";
import { Global } from "@emotion/core";

import { globalStyle } from "./styles/globalStyle";

const Hoge = styled.div``;

const initialization = async () => {
  const theme = createTheme();
  try {
    ReactDom.render(
      <ThemeProvider theme={theme}>
        <Global styles={globalStyle} />
        <Hoge>hoge</Hoge>
        <Typography>hoge</Typography>
      </ThemeProvider>,
      document.getElementById("root"),
    );
  } catch (e) {
    // eslint-disable-next-line no-console
    console.error(e);
  }
};

initialization();
