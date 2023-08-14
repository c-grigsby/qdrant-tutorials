from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import os

# Get environment vars
load_dotenv()
qdrant_url = os.getenv("QDRANT_URL")


class NeuralSearcher:

    def __init__(self, collection_name):
        self.collection_name = collection_name
        # Initialize encoder model
        self.model = SentenceTransformer('all-MiniLM-L6-v2', device='cpu')
        # Initialize Qdrant Client
        self.qdrant_client = QdrantClient(qdrant_url)
        
        print(f"QDRANT_URL: {qdrant_url}\n")

    def search(self, text: str):
        # Convert text query into a vector
        vector = self.model.encode(text).tolist()

        search_result = self.qdrant_client.search(
            # The collection to query
            collection_name=self.collection_name,
            # The query vector
            query_vector=vector,
            # The filter you wish to apply (see documentation)
            query_filter=None,  
            # The limit of results
            limit=20 
        )
        
        results = []

        # Return the payload and hit score from our results
        for hit in search_result:
            results.append({"payload": hit.payload, "score": hit.score, "result_number": len(results)})

        return results