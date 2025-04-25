// Test file for permissive CORS configuration

function setupServer(app) {
  app.use((req, res, next) => {
    // Vulnerable line: Setting CORS to allow any origin
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    if (req.method === 'OPTIONS') {
        return res.sendStatus(200);
    }
    next();
  });

  // ... other server setup
}

// Example usage (conceptual)
// const express = require('express');
// const app = express();
// setupServer(app);
// app.listen(3000);
