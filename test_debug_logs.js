// Test file for console.log debug detection

function processUserData(user) {
  console.log('Processing user:', user.id); // This should be flagged

  const importantData = user.secretToken; // Example sensitive data
  // This is bad - logging sensitive data!
  console.log(`User token found: ${importantData}`); // This should be flagged
  
  // Some logic here...
  const result = importantData.toUpperCase();

  // console.log('Processing complete for user:', user.id); // This is commented out, should NOT be flagged

  return result;
}

function setupConfig() {
    const configValue = process.env.CONFIG_VAR || 'default';
    console.log("Config value set to:", configValue); // This should be flagged
}

const sampleUser = { id: 'user123', secretToken: 'tok_abc123xyz' };
processUserData(sampleUser);
setupConfig();

// Use a proper logger in production!
// import logger from './logger';
// logger.info('User processed', { userId: user.id });
