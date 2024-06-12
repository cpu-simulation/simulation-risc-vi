import {  useState } from "react";
import { DarkModeSwitch } from "react-toggle-dark-mode";

const DarkModeToggler = () => {
  const [isDarkMode, setDarkMode] = useState(false);

  const toggleDarkMode = (checked: boolean) =>{
    setDarkMode(checked);
  };

  return (
    <DarkModeSwitch
      style={{}}
      checked={isDarkMode}
      onChange={toggleDarkMode}
      size={21}
      sunColor="rgba(216, 216, 216, 1)"
      moonColor="#363537"
    />
  );
};

export default DarkModeToggler;
