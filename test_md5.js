// Test file for weak MD5 hash detection in JS contexts

// JS doesn't have native MD5, but patterns might look for the string

function calculateMD5Hash(data) {
  // Assume this function uses an external library or a custom MD5 implementation
  console.log("Simulating MD5 hash calculation for:", data);
  // This line contains 'md5' and should be flagged
  const hashType = 'md5'; 
  return 'simulated-md5-hash-' + data; 
}

function calculateStrongHash(data) {
  // Simulate using a stronger hash (e.g., built-in SubtleCrypto for SHA-256)
  console.log("Simulating strong hash calculation for:", data);
  return 'simulated-strong-hash-' + data;
}

const userData = 'important_data';
const weakHash = calculateMD5Hash(userData); // Call involving 'MD5'
const strongHash = calculateStrongHash(userData);

// These console.logs should also be flagged by the debug pattern
console.log(`Weak hash (simulated MD5): ${weakHash}`);
console.log(`Strong hash (simulated): ${strongHash}`);

// const md5Library = require('some-md5-lib'); // Example import
