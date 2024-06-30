# Local_deployment_Sentiment_Analysis
The project involves setting up a sentiment analysis application using Hugging Face's transformer models, FastAPI for building the API, and Docker for containerization. This setup allows for local deployment, ensuring the sentiment analysis service runs efficiently on a local machine or server.

# Sentiment Analysis API

This project is a sentiment analysis API built using Hugging Face's `transformers` library, FastAPI for serving the model, and Docker for containerization.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Docker Deployment](#docker-deployment)
- 
## Overview

The sentiment analysis API allows you to analyze the sentiment of text input, providing a classification of the sentiment using a pre-trained model from Hugging Face called Emotion English DistilRoBERTa-base. 

## Features

- **Sentiment Analysis**: Analyze the sentiment of a given text.
- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.6+.
- **Docker**: Containerized application for easy deployment.

## Setup

### Prerequisites

- Python 3.7+
- pip (Python package installer)
- Docker (for containerization)
- Numpy < 2.0

### Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/your-username/sentiment-analysis-api.git
    cd sentiment-analysis-API
    ```

2. **Install the required Python packages**:

    Create a virtual environment:

    ```sh
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

    Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

3. **Run the FastAPI application**:

    ```sh
    uvicorn main: app --reload
    main is the name of the Python file where API endpoints are created and app is the name of the FastAPI instance.
    ```
    The API will be available at `http://127.0.0.1:8000`.

## Usage

### Sample Request

You can use `curl` or any API testing tool (like Postman) to send a request to the API.

```sh
curl -X POST "http://127.0.0.1:8000/analyze" -H "Content-Type: application/json" -d '{"text": "I don't like this!"}'

```

Click on URL given and you'll see FastAPI swagger UI 
Click on Try it Out! 
Write the sentence in the input, then click on execute.

![image](https://github.com/Jyoti200/Local_deployment_Sentiment_Analysis/assets/86410759/cda01929-9579-476b-8208-1a75675b9cc3)


## API Endpoints
## POST /analyze
Analyzes the sentiment of the provided text.

## Request Body:

text: The input text to be analyzed (string).
Response:
label: The sentiment label (e.g., anger 🤬
disgust 🤢
fear 😨
joy 😀
neutral 😐
sadness 😭
surprise 😲).
score: The confidence score of the prediction.

### Docker Deployment
# Building the Docker Image
1. Create a Dockerfile
2. Build the Docker image
3. Run the Docker container
