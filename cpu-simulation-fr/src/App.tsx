import { useState } from "react";
import GlobalStyle from "./assets/styled-components/globalStyles";
import { ThemeProvider } from "styled-components";
import { dark, light } from "./assets/styled-components/theme";

function App() {
  const [theme, setTheme] = useState(dark);
  return (
    <>
      <ThemeProvider theme={theme}>
        {/* need a toggler */}
        <GlobalStyle />
        <div className="App"></div>
      </ThemeProvider>
    </>
  );
}

export default App;
