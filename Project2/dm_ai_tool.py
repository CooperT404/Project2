import requests
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- Document Store (Example Documents) ---
DOCUMENTS = [
    "The ancient halls echo with the footsteps of long-forgotten heroes. The magic of the old world lingers in every stone.",
    "Deep within the dungeon lurks a dangerous and cunning foe. Shadows dance and move in the dim, uncertain light.",
    "Crumbled stone walls bear the scars of ancient battles, and hidden treasures lie buried beneath a layer of dust and decay."
]

def retrieve_documents(query: str, documents: list = DOCUMENTS, top_k: int = 2) -> list:
    """
    Given a query, retrieve the top_k relevant documents from the document store.
    """
    vectorizer = TfidfVectorizer()
    # Fit the vectorizer on our document store
    doc_vectors = vectorizer.fit_transform(documents)
    # Convert the query into the same vector space.
    query_vector = vectorizer.transform([query])
    # Compute cosine similarity between the query and all documents.
    scores = cosine_similarity(query_vector, doc_vectors)
    # Get the indices of the top_k documents in descending order of similarity.
    top_indices = np.argsort(scores[0])[-top_k:][::-1]
    # Return the corresponding documents.
    retrieved_docs = [documents[i] for i in top_indices]
    return retrieved_docs

def generate_rag_narrative(game_log: str, query: str) -> str:
    """
    Generates a narrative description from the AI endpoint using a Retrieval Augmented Generation method.

    It retrieves context documents based on the query, augments the prompt with that context and the game log,
    and then sends the prompt to the DeepSeek model endpoint. The response is expected to include the assistant's
    generated text.

    Args:
        game_log (str): The current game log.
        query (str): A query string used to retrieve relevant context.

    Returns:
        str: The generated narrative, or a fallback response if generation fails.
    """
    # Retrieve relevant documents.
    retrieved_docs = retrieve_documents(query)
    context = "\n\n".join(retrieved_docs)
    
    # Build the augmented prompt.
    prompt_text = (
    f"Context:\n{context}\n\n"
    f"Game Log:\n{game_log}\n\n"
    "Please generate a vivid narrative description of the dungeon."
)


    api_url = "http://localhost:11434/api/generate"

    if not prompt_text.strip():
        return "The Dungeon Master awaits your command, but no story was provided."

    prompt_payload = {
        "model": "deepseek-r1:1.5b",
        "options": {
            "temperature": 0.7,
            "max_tokens": 250
        },
        "messages": [
            {
                "role": "system",
                "content": "You are a Dungeon Master for an epic fantasy adventure."
            },
            {
                "role": "user",
                "content": prompt_text
            }
        ]
    }

    try:
        response = requests.post(api_url, json=prompt_payload)
        response.raise_for_status()
        json_resp = response.json()
    except Exception as e:
        print(f"API Error: {str(e)}")
        return "The dungeon remains silent as something went wrong."

    # Extract narrative from response
    narrative = ""
    if "messages" in json_resp:
        for msg in json_resp["messages"]:
            if msg.get("role") == "assistant":
                narrative += msg.get("content", "")
    else:
        narrative = json_resp.get("response", "")

    return narrative if narrative else "The dungeon stands silent, holding its secrets close."

if __name__ == "__main__":
    # The base game log.
    current_log = "The dungeon awaits your adventurers!"
    # A query string to retrieve relevant context from our document store.
    query_text = "ancient halls heroic battles treasures dungeon shadows"
    
    narrative = generate_rag_narrative(current_log, query_text)
    print("Generated Narrative:")
    print(narrative)
