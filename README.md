# Simple-Chatbot
A simple interactive chatbot that utilizes OpenAI's GPT to understand user queries and generate human-like responses

Objective of this project is to develop a simple interactive chatbot that utilizes OpenAI's GPT to understand user queries and generate human-like responses.

# Development Steps - Pytrhon Approach

## Step 1: Setup and Prerequisites
1. Sign up for OpenAI and obtained API key.
2. Environment Setup: Created a new Python virtual environment for this project using PyCharm, created requirements.txt file to manage dependencies.

## Step 2: Install OpenAI Python Package
1. Through "pip install -r requirements.txt" commad installed the OpenAI Python package. openai package is required to interact with the OpenAI API.

## Step 3: Implementing the Chatbot
1. Initialize the API: Created a Python class OpenAiConnectionManager to initialize the OpenAI API with the API key.
2. Created a Python class ChatService to Implement integratioin with OpenAI API, sending a question to ChatGPT and fetching a generated response.
3. Implemented a simple for loop that allows sending each question as ChatGPT queriy and receive response from the chatbot. 