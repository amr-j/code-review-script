import requests

# Define the URL and payload
url = "http://localhost:11434/api/generate"
payload = {
    "model": "codellama",
    "prompt": "Write me a function that outputs the fibonacci sequence"
}

# Send the POST request
response = requests.post(url, json=payload)

# Print the status code and response text
print("Status Code:", response.status_code)
print("Response Text:", response.text)
