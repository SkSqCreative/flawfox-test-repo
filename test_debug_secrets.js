// Potential debug mode check
if (process.env.NODE_ENV !== 'production') {
  console.log('Running in development mode');
}

// Hardcoded secret
const accessToken = "ghp_abcdefghijklmnopqrstuvwxyz0123456789";
const secretKey = 'myVeryLongAndSecureLookingSecretKey123!';
console.log(`Using token: ${accessToken}`);
