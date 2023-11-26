from flask import Flask, request, jsonify 
import requests
from flask_cors import CORS

import os
import sys

import openai
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma

import constants

app = Flask(__name__)
CORS(app)

os.environ["OPENAI_API_KEY"] = constants.APIKEY

# Enable to save to disk & reuse the model (for repeated queries on the same data)
PERSIST = True

query = None
if len(sys.argv) > 1:
  query = sys.argv[1]

if PERSIST and os.path.exists("persist"):
  print("Reusing index...\n")
  vectorstore = Chroma(persist_directory="persist", embedding_function=OpenAIEmbeddings())
  index = VectorStoreIndexWrapper(vectorstore=vectorstore)
else:
  loader = DirectoryLoader("data/")
  if PERSIST:
    index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory":"persist"}).from_loaders([loader])
  else:
    index = VectorstoreIndexCreator().from_loaders([loader])

chain = ConversationalRetrievalChain.from_llm(
  llm=ChatOpenAI(model="gpt-3.5-turbo"),
  retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
)

chat_history = []

@app.route("/")
def endpoint():
    return "Home"

@app.get("/test")
def test():
    try:
        data = request.args.get('data')
        data += " Explain this to a "
        persona = request.args.get('persona')
        def switch(persona):
            if persona == 0:
                data += "beginner"
            elif persona == 1:
                data += "developer"
            elif persona == 2:
                data += "business analyst"
        print("request arguments: ", data)
        if data:
            response = chain({"question": data, "chat_history": chat_history})
            if response:
                print("AI response: ", response)
                chat_history.append((data, response['answer']))
                data = None
                return jsonify({'status': 'success', 'data': response}), 200
            else:
                return jsonify({'status': 'error', 'message': 'Could not fetch response from AI'}), 400
        else:
            return "sicko ok", 200

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == "__main__":
    app.run(port=8080, debug=True)