// import React, { useState } from "react";

// import { IconButton, Tooltip } from "@mui/material";
// import InfoOutlinedIcon from "@mui/icons-material/InfoOutlined";
// import {
//   Table,
//   TableBody,
//   TableCell,
//   TableContainer,
//   TableHead,
//   TableRow,
//   Paper,
//   TablePagination,
//   TableSortLabel,
//   TextField,
//   Select,
//   MenuItem,
//   FormControl,
//   InputLabel,
// } from "@mui/material";

// const TransactionTable = ({ transactions }) => {
//   const [page, setPage] = useState(0);
//   const [rowsPerPage, setRowsPerPage] = useState(5);
//   const [sortOrder, setSortOrder] = useState("desc"); // Sorting order
//   const [riskFilter, setRiskFilter] = useState("all"); // Filter by risk category
//   const [searchQuery, setSearchQuery] = useState(""); // Search by Transaction ID

//   // Determine risk category color
//   const getRiskColor = (riskScore) => {
//     if (riskScore >= 0.8) return "#FFCDD2"; // Light Red for High Risk
//     if (riskScore >= 0.3) return "#FFF9C4"; // Light Yellow for Medium Risk
//     return "#C8E6C9"; // Light Green for Low Risk
//   };

//   // Sorting function (sort by risk score)
//   const sortedTransactions = [...transactions].sort((a, b) => {
//     return sortOrder === "asc" ? a.riskScore - b.riskScore : b.riskScore - a.riskScore;
//   });

//   // 🔹 **Fixed Filtering Logic**
//   const filteredTransactions = sortedTransactions.filter((txn) => {
//     // Determine the risk category based on the risk score
//     let riskCategory = "green"; // Default Low Risk
//     if (txn.riskScore >= 0.8) riskCategory = "red"; // High Risk
//     else if (txn.riskScore >= 0.3) riskCategory = "yellow"; // Medium Risk

//     return (
//       (riskFilter === "all" || riskCategory === riskFilter) &&
//       txn.transactionId.includes(searchQuery)
//     );
//   });

//   // Paginated transactions
//   const paginatedTransactions = filteredTransactions.slice(
//     page * rowsPerPage,
//     page * rowsPerPage + rowsPerPage
//   );

//   return (
//     <Paper sx={{ padding: 2, width: "100%", boxShadow: 3, borderRadius: 2 }}>
//       {/* 🔍 Search & Filter Controls */}
//       <div style={{ display: "flex", gap: "16px", marginBottom: "16px" }}>
//         <TextField
//           label="Search Transaction ID"
//           variant="outlined"
//           size="small"
//           value={searchQuery}
//           onChange={(e) => setSearchQuery(e.target.value)}
//         />
//         <FormControl variant="outlined" size="small">
//           <InputLabel>Filter by Risk</InputLabel>
//           <Select value={riskFilter} onChange={(e) => setRiskFilter(e.target.value)} label="Filter by Risk">
//             <MenuItem value="all">All</MenuItem>
//             <MenuItem value="red">High Risk</MenuItem>
//             <MenuItem value="yellow">Medium Risk</MenuItem>
//             <MenuItem value="green">Low Risk</MenuItem>
//           </Select>
//         </FormControl>
//         {/* ℹ️ Info Button aligned to the right */}
//         <div style={{ marginLeft: "auto" }}>
//     <Tooltip
//         title={
//           <div>
//             <p style={{ margin: 0, color: "#00000" }}>🔴 High Risk </p>
//             <p style={{ margin: 0, color: "#00000" }}>🟡 Medium Risk</p>
//             <p style={{ margin: 0, color: "#00000" }}>🟢 Low Risk </p>
//           </div>
//         }
//         arrow
//         placement="right"
//       >
//         <IconButton>
//           <InfoOutlinedIcon color="primary" />
//         </IconButton>
//       </Tooltip>
//       </div>
//       </div>

//       {/* 📊 Transaction Table */}
//       <TableContainer>
//         <Table>
//           <TableHead>
//             <TableRow sx={{ backgroundColor: "#b71c1c", color: "#fff" }}>
//               <TableCell sx={{ color: "#fff", fontWeight: "bold" }}>Transaction ID</TableCell>
//               <TableCell sx={{ color: "#fff", fontWeight: "bold" }}>Extracted Entity</TableCell>
//               <TableCell sx={{ color: "#fff", fontWeight: "bold" }}>Entity Type</TableCell>
//               <TableCell sx={{ color: "#fff", fontWeight: "bold" }}>Risk Score</TableCell>
//               <TableCell sx={{ color: "#fff", fontWeight: "bold" }}>Supporting Evidence</TableCell>
//               <TableCell sx={{ color: "#fff", fontWeight: "bold" }}>Confidence Score</TableCell>
//               {/* <TableCell sx={{ color: "#fff", fontWeight: "bold" }}>Reason</TableCell> */}
//             </TableRow>
//           </TableHead>
//           <TableBody>
//             {paginatedTransactions.map((txn, index) => (
//               <TableRow key={index} sx={{ backgroundColor: getRiskColor(txn.riskScore) }}>
//                 <TableCell>{txn.transactionId}</TableCell>
//                 <TableCell>{txn.extractedEntity.join(", ")}</TableCell>
//                 <TableCell>{txn.entityType.join(", ")}</TableCell>
//                 <TableCell>{txn.riskScore.toFixed(2)}</TableCell>
//                 <TableCell>{txn.supportingEvidence.join(", ")}</TableCell>
//                 <TableCell>{txn.confidenceScore.toFixed(2)}</TableCell>
//                 {/* <TableCell>{txn.reason}</TableCell> */}
//               </TableRow>
//             ))}
//           </TableBody>
//         </Table>
//       </TableContainer>

//       {/* 📌 Pagination */}
//       <TablePagination
//         rowsPerPageOptions={[5, 10, 20]}
//         component="div"
//         count={filteredTransactions.length}
//         rowsPerPage={rowsPerPage}
//         page={page}
//         onPageChange={(event, newPage) => setPage(newPage)}
//         onRowsPerPageChange={(event) => {
//           setRowsPerPage(parseInt(event.target.value, 10));
//           setPage(0);
//         }}
//       />
//     </Paper>
//   );
// };

// export default TransactionTable;
import React, { useState } from "react";
import { IconButton, Tooltip } from "@mui/material";
import InfoOutlinedIcon from "@mui/icons-material/InfoOutlined";
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  TablePagination,
  TextField,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
} from "@mui/material";

const TransactionTable = ({ transactions }) => {
  const [page, setPage] = useState(0);
  const [rowsPerPage, setRowsPerPage] = useState(5);
  const [riskFilter, setRiskFilter] = useState("all"); // Filter by risk category
  const [searchQuery, setSearchQuery] = useState(""); // Search by Transaction ID

  // Determine risk category color
  const getRiskColor = (riskScore) => {
    if (riskScore >= 0.8) return "#FFCDD2"; // Light Red for High Risk
    if (riskScore >= 0.3) return "#FFF9C4"; // Light Yellow for Medium Risk
    return "#C8E6C9"; // Light Green for Low Risk
  };

  // 🔹 **Fixed Filtering Logic**
  const filteredTransactions = transactions.filter((txn) => {
    let riskCategory = "green"; // Default Low Risk
    if (txn.riskScore >= 0.8) riskCategory = "red"; // High Risk
    else if (txn.riskScore >= 0.3) riskCategory = "yellow"; // Medium Risk

    return (
      (riskFilter === "all" || riskCategory === riskFilter) &&
      txn.transactionId.includes(searchQuery)
    );
  });

  // Paginated transactions
  const paginatedTransactions = filteredTransactions.slice(
    page * rowsPerPage,
    page * rowsPerPage + rowsPerPage
  );

  return (
    <Paper sx={{ padding: 2, width: "100%", boxShadow: 3, borderRadius: 2 }}>
      {/* 🔍 Search & Filter Controls */}
      <div style={{ display: "flex", gap: "16px", marginBottom: "16px" }}>
        <TextField
          label="Search Transaction ID"
          variant="outlined"
          size="small"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
        />
        <FormControl variant="outlined" size="small">
          <InputLabel>Filter by Risk</InputLabel>
          <Select value={riskFilter} onChange={(e) => setRiskFilter(e.target.value)} label="Filter by Risk">
            <MenuItem value="all">All</MenuItem>
            <MenuItem value="red">High Risk</MenuItem>
            <MenuItem value="yellow">Medium Risk</MenuItem>
            <MenuItem value="green">Low Risk</MenuItem>
          </Select>
        </FormControl>
        {/* ℹ️ Info Button aligned to the right */}
        <div style={{ marginLeft: "auto" }}>
          <Tooltip
            title={
              <div>
                <p style={{ margin: 0, color: "#00000" }}>🔴 High Risk </p>
                <p style={{ margin: 0, color: "#00000" }}>🟡 Medium Risk</p>
                <p style={{ margin: 0, color: "#00000" }}>🟢 Low Risk </p>
              </div>
            }
            arrow
            placement="right"
          >
            <IconButton>
              <InfoOutlinedIcon color="primary" />
            </IconButton>
          </Tooltip>
        </div>
      </div>

      {/* 📊 Transaction Table */}
      <TableContainer>
        <Table>
          <TableHead>
            <TableRow sx={{ backgroundColor: "#b71c1c", color: "#fff" }}>
              <TableCell sx={{ color: "#fff", fontWeight: "bold" }}>Transaction ID</TableCell>
              <TableCell sx={{ color: "#fff", fontWeight: "bold" }}>Extracted Entity</TableCell>
              <TableCell sx={{ color: "#fff", fontWeight: "bold" }}>Entity Type</TableCell>
              <TableCell sx={{ color: "#fff", fontWeight: "bold" }}>Risk Score</TableCell>
              <TableCell sx={{ color: "#fff", fontWeight: "bold" }}>Supporting Evidence</TableCell>
              <TableCell sx={{ color: "#fff", fontWeight: "bold" }}>Confidence Score</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {paginatedTransactions.map((txn, index) => (
              <TableRow key={index} sx={{ backgroundColor: getRiskColor(txn.riskScore) }}>
                <TableCell>{txn.transactionId}</TableCell>
                <TableCell>{txn.extractedEntity.join(", ")}</TableCell>
                <TableCell>{txn.entityType.join(", ")}</TableCell>
                <TableCell>{txn.riskScore.toFixed(2)}</TableCell>
                <TableCell>{txn.supportingEvidence.join(", ")}</TableCell>
                <TableCell>{txn.confidenceScore.toFixed(2)}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>

      {/* 📌 Pagination */}
      <TablePagination
        rowsPerPageOptions={[5, 10, 20]}
        component="div"
        count={filteredTransactions.length}
        rowsPerPage={rowsPerPage}
        page={page}
        onPageChange={(event, newPage) => setPage(newPage)}
        onRowsPerPageChange={(event) => {
          setRowsPerPage(parseInt(event.target.value, 10));
          setPage(0);
        }}
      />
    </Paper>
  );
};

export default TransactionTable;
