import React, { useState, useEffect } from "react";
import { Box, CssBaseline, Toolbar,Paper,Typography } from "@mui/material";
import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";
import FileUpload from "./components/Fileupload";
import TransactionTable from "./components/TransactionTable";

const drawerWidth = 240;
const navbarHeight = 64;

const App = () => {
  const [transactions, setTransactions] = useState([]);

  const handleFileUpload = async () => {
    try {
      const response = await fetch("/risk_analysis_results.json");
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const rawData = await response.json();
      
      console.log("Raw Data:", rawData); // Debugging log
  
      // Normalize keys to camelCase
      const formattedData = rawData.map(txn => ({
        transactionId: txn["Transaction ID"] || "N/A",
        extractedEntity: txn["Extracted Entity"] || [],
        entityType: txn["Entity Type"] || [],
        riskScore: typeof txn["Risk Score"] === "number" ? txn["Risk Score"] : 0,
        supportingEvidence: txn["Supporting Evidence"] || [],
        confidenceScore: txn["Confidence Score"] || 0,
        reason: txn["Reason"] || "N/A"
      }));
  
      console.log("Processed Data:", formattedData); // Debugging log
      setTransactions(formattedData);
    } catch (error) {
      console.error("Error loading transaction data:", error);
    }
  };

  const getRiskSummary = (transactions) => {
    const summary = { high: 0, medium: 0, low: 0, total: transactions.length };

    transactions.forEach((txn) => {
      if (txn.riskScore >= 0.8) summary.high++;
      else if (txn.riskScore >= 0.3) summary.medium++;
      else summary.low++;
    });

    return summary;
  };
  
  const summary = getRiskSummary(transactions);

  return (
    <Box sx={{ display: "flex", width: "100vw", height: "100vh" }}>
      <CssBaseline />
      <Sidebar />

      <Box
        component="main"
        sx={{
          flexGrow: 1,
          p: 3,
          width: `calc(100% - ${drawerWidth}px)`,
          ml: `${drawerWidth}px`,
          mt: `${navbarHeight}px`,
        }}
      >
        <Navbar />

      <Box
  component="main"
  sx={{
    flexGrow: 1,
    marginLeft: 0, // Override default drawer margin
    padding: 0,
    width: "100%",
  }}
>
  <FileUpload onFileUpload={handleFileUpload} />

  {transactions.length > 0 && (
            <Box sx={{ mt: 2, width: "100%", textAlign: "left", padding: 0 }}>
              {/* 🔹 Summary Box */}
              <Paper sx={{ mb: 2, p: 2, bgcolor: "#f5f5f5", borderRadius: 2, width: "100%" }}>
                <Typography variant="h6">Transaction Summary</Typography>
                <Typography>Total Transactions: {summary.total}</Typography>
                <Typography>High Risk: {summary.high}</Typography>
                <Typography>Medium Risk: {summary.medium}</Typography>
                <Typography>Low Risk: {summary.low}</Typography>
              </Paper>

              {/* Transaction Table */}
              <TransactionTable transactions={transactions} />
            </Box>
          )}
</Box>
    </Box>
    </Box>
    
  );
};

export default App;
