#Image Input
#Explore using image inputs (URLs or local files) with multimodal Gemini models in LangChain for vision tasks.

import os
import base64
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
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
)

# Using an image URL
message_url = HumanMessage(
    content=[
        {"type": "text", "text": "Describe this image."},
        {"type": "image_url", "image_url": "https://picsum.photos/seed/picsum/200/300"},
    ]
)
#result_url = llm.invoke([message_url])
#print(result_url.content)


# Using a local image
local_image_path = "./assets/person_cycling.jpg"
with open(local_image_path, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
 
message_local = HumanMessage(
    content=[
        {"type": "text", "text": "Describe this image."},
        {"type": "image_url", "image_url": f"data:image/png;base64,{encoded_image}"}
    ]
)
result_local = llm.invoke([message_local])
print(result_local.content)