import React, { useState } from "react";
import { AppBar, Toolbar, Typography, IconButton, Menu, MenuItem } from "@mui/material";
import AccountCircleIcon from "@mui/icons-material/AccountCircle";

const Navbar = ({ toggleDrawer }) => {
  const [anchorEl, setAnchorEl] = useState(null);

  const handleMenuOpen = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleMenuClose = () => {
    setAnchorEl(null);
  };

  return (
    <AppBar position="fixed" sx={{ backgroundColor: "#B71C1C", zIndex: 1201 }}>
      <Toolbar>

        {/* Wells Fargo Logo */}
        <img
          src="/wellsFargo.png"
          alt="Wells Fargo"
          style={{ height: "40px", marginLeft: "10px", marginRight: "10px" }}
        />
        
        <Typography variant="h6" sx={{ flexGrow: 1 }}>
          Suspicious Transaction Analyzer
        </Typography>

        {/* Admin/Login Menu */}
        <IconButton color="inherit" onClick={handleMenuOpen}>
          <AccountCircleIcon />
        </IconButton>
        <Menu anchorEl={anchorEl} open={Boolean(anchorEl)} onClose={handleMenuClose}>
          <MenuItem onClick={handleMenuClose}>Admin</MenuItem>
          <MenuItem onClick={handleMenuClose}>Login</MenuItem>
        </Menu>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
