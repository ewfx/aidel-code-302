import React from "react";
import {
  Drawer,
  List,
  ListItem,
  ListItemText,
  ListItemIcon,
  Divider,
  Typography,
} from "@mui/material";
import DashboardIcon from "@mui/icons-material/Dashboard";
import ReceiptIcon from "@mui/icons-material/Receipt";
import SettingsIcon from "@mui/icons-material/Settings";

const drawerWidth = 240;

const Sidebar = () => {
  return (
    <Drawer
      variant="permanent"
      sx={{
        width: drawerWidth,
        flexShrink: 0,
        "& .MuiDrawer-paper": {
          width: drawerWidth,
          backgroundColor: "#263238",
          color: "#ffffff",
        },
      }}
    >
      <Typography
        variant="h6"
        sx={{
          textAlign: "center",
          fontWeight: "bold",
          padding: "16px",
          color: "#FFC107",
        }}
      >
        Menu
      </Typography>
      <Divider sx={{ backgroundColor: "#FFC107" }} />
      <List>
        <ListItem button sx={{ "&:hover": { backgroundColor: "#455A64" } }}>
          <ListItemIcon>
            <DashboardIcon sx={{ color: "#FFC107" }} />
          </ListItemIcon>
          <ListItemText primary="Dashboard" />
        </ListItem>
        <ListItem button sx={{ "&:hover": { backgroundColor: "#455A64" } }}>
          <ListItemIcon>
            <ReceiptIcon sx={{ color: "#FFC107" }} />
          </ListItemIcon>
          <ListItemText primary="Transactions" />
        </ListItem>
        <ListItem button sx={{ "&:hover": { backgroundColor: "#455A64" } }}>
          <ListItemIcon>
            <SettingsIcon sx={{ color: "#FFC107" }} />
          </ListItemIcon>
          <ListItemText primary="Settings" />
        </ListItem>
      </List>
    </Drawer>
  );
};

export default Sidebar;
