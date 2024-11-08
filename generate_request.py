import requests
import json


url = "http://localhost:11434/api/generate"
payload = {
    "model": "codellama",
    "prompt": "Write me a function that outputs the fibonacci sequence"
}

response = requests.post(url, json=payload, stream=True)

if response.status_code == 200: 
    complete_response = ""

    for line in response.iter_lines(decode_unicode=True): 
        if line:
            try: 
                json_line = json.loads(line)
                complete_response += json_line.get('response', '')
            except json.JSONDecodeError:
                print("Failed to parse line:", line)

    print(complete_response)
else:
    print("Failed to get a valid response.")
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
