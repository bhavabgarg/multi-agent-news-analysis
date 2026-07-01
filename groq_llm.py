from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq 

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",  
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0,  
    max_tokens= 120
)   
    