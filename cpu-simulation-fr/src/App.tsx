import { useState } from "react";
import GlobalStyle from "./assets/styled-components/globalStyles";
import { ThemeProvider } from "styled-components";
import { dark, light } from "./assets/styled-components/theme";
import Cpu from "./components/cpu/cpu";
import DarkModeToggler from "./components/darkModeToggler/darkModeToggler";

function App() {
  const [theme, setTheme] = useState(true);
  return (
    <>
      <ThemeProvider theme={ theme ? dark : light}>
        <GlobalStyle />
        <div className="App">
          <Cpu />
          <span onClick={()=>{setTheme(!theme)}} className="absolute right-[293px] top-[54px]">
            <DarkModeToggler/>
          </span>
        </div>
      </ThemeProvider>
    </>
  );
}

export default App;
