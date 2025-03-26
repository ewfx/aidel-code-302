import React, { useState } from "react";
import { Button, Input, Box , Typography } from "@mui/material";

const FileUpload = ({ onFileUpload }) => {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleUpload = () => {
    if (selectedFile) {
      onFileUpload(selectedFile);
    }
  };

  return (
    <Box sx={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
    <Typography variant="h6" sx={{ mb: 1, fontWeight: "bold" }}>
      Add your transaction file
    </Typography>
    <Input type="file" onChange={handleFileChange} />
    <Button
      variant="contained"
      sx={{ mt: 2, backgroundColor: "#b31b1b", color: "white" }}
      onClick={handleUpload}
      disabled={!selectedFile}
    >
      Upload CSV
    </Button>
  </Box>
  );
};

export default FileUpload;
