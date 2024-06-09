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
      <ThemeProvider theme={theme ? dark : light}>
        {/* need a toggler */}
        <GlobalStyle />
        <div className="App">
          <Cpu />
          <div onClick={()=>{setTheme(!theme)}} className="bg-slate-600 inline">
            <DarkModeToggler />
          </div>
        </div>
      </ThemeProvider>
    </>
  );
}

export default App;
