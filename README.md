# Enronalyse
App to analyse the Enron email dataset using a vector database.  
Based on blog post **TODO insert link here**

## Setup

Create a .env file with the following settings. Fill in the *** with your own values.

    EMAIL_FOLDER = "***"
    VDB_URL = "https://***.weaviate.network"
    OPENAI_API_KEY="***"

## Import data
Use the import/read_emails script.

## Run  

    uvicorn app.main:app --reload

