import requests
# Define the input data
input_data = {
    "input": "I strongly dislike this website!"
}

# Send a POST request to the FastAPI endpoint
response = requests.post("http://127.0.0.1:8000/sentiment", json=input_data)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the response data
    response_data = response.json()
    
    # Print the results
    print(response_data)
else:
    print("Error:", response.text)