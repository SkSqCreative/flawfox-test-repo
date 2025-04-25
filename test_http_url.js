const apiEndpoint = 'http://example.com/api';
const anotherUrl = "http://internal.service/data";

async function fetchData() {
  try {
    // Using the insecure endpoint
    const response = await fetch(apiEndpoint);
    const data = await response.json();
    console.log('Data fetched:', data);
  } catch (error) {
    console.error('Failed to fetch data:', error);
  }
}

fetchData();
