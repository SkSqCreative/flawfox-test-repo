// Assuming CryptoJS library is used for SHA1 (or similar pattern)
// const sha1Hash = CryptoJS.SHA1('message'); 
// Simplified for regex trigger:
const myHash = sha1('data');
console.log(`SHA1 Hash: ${myHash}`);

// Insecure random
const insecureRand = Math.random();
console.log(`Insecure random number: ${insecureRand}`);
