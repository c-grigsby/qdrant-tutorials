# @packages
from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn
import os
# @scripts
from neural_searcher import NeuralSearcher

app = FastAPI()

# Get environment vars
load_dotenv()
qdrant_collection = os.getenv("QDRANT_COLLECTION")

print(f"QDRANT_COLLECTION: {qdrant_collection}")

# Create a Neural Searcher instance
neural_searcher = NeuralSearcher(collection_name=qdrant_collection)

@app.get("/api/search")
def search_startup(query: str):  
    return {
        "result": neural_searcher.search(text=query)
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)