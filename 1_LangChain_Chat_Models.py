# Google Gemini with LangChain Chat Models
# Learn how to use Google Gemini chat models within LangChain for basic text generation and conversation tasks.

import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Ensure the GOOGLE_API_KEY environment variable is set 
if "GOOGLE_API_KEY" not in os.environ:
    raise ValueError("Please set the GOOGLE_API_KEY environment variable in your .env file.")   

 
# Initialize model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)
 
# Simple invocation
messages = [
    ("system", "You are a helpful assistant that translates English to French."),
    ("human", "I love programming."),
]
response = llm.invoke(messages)
print(response.content)  # Output: J'adore la programmation.