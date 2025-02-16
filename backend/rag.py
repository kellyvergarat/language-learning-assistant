import chromadb
# setup Chroma in-memory, for easy prototyping. Can add persistence easily!
client = chromadb.Client()

# Create collection. get_collection, get_or_create_collection, delete_collection also available!
collection = client.create_collection("all-my-documents")

# unique for each doc
# Add docs to the collection. Can also update and delete. Row-based API coming soon!
# Read documents from local text files
documents = []
for file_path in ["doc1.txt", "doc2.txt"]:  # List your text file paths
    with open(file_path, "r") as f:
        documents.append(f.read())

collection.add(
    documents=documents, # Pass list of document contents read from files
    metadatas=[{"source": "doc1.txt"},
               {"source": "doc2.txt"}], # Use filenames as source
    ids=["doc1", 
        "doc2"], # unique for each doc
)

# Query/search 2 most similar results. You can also .get by id
results = collection.query(
    query_texts=["This is a query document"],
    n_results=2,
    # where={"metadata_field": "is_equal_to_this"}, # optional filter
    # where_document={"$contains":"search_string"}  # optional filter
)

print(results)