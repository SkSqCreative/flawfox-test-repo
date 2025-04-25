// Test file for XSS vulnerability

function displayData(userData) {
  const displayElement = document.getElementById('user-data');
  if (displayElement) {
    // Vulnerable line: Setting innerHTML directly from input
    displayElement.innerHTML = 'Welcome, ' + userData.name + '!';
  }
}

const potentiallyUnsafeData = { name: '<script>alert("XSS attack!")</script>' };
displayData(potentiallyUnsafeData);
