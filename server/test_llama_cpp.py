from llama_cpp import Llama
llm = Llama(model_path="./server/llama-2-7b.Q4_K_M.gguf")
output = llm(
      "Q: Name the planets in the solar system? A: ", # Prompt
      max_tokens=32, # Generate up to 32 tokens
      stop=["Q:", "\n"], # Stop generating just before the model would generate a new question
      echo=True # Echo the prompt back in the output
) # Generate a completion, can also call create_completion
print(output)
{
  "id": "cmpl-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "object": "text_completion",
  "created": 1679561337,
  "model": "./models/7B/llama-model.gguf",
  "choices": [
    {
      "text": "Q: Name the planets in the solar system? A: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune and Pluto.",
      "index": 0,
      "logprobs": None,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 14,
    "completion_tokens": 28,
    "total_tokens": 42
  }
}


""" 
Need a GPU for this!
from paperqa import Docs
from glob import glob

from langchain.llms import LlamaCpp
from langchain import PromptTemplate, LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.embeddings import LlamaCppEmbeddings
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


# Make sure the model path is correct for your system!
llm = LlamaCpp(
    model_path="./llama-2-7b.Q4_K_M.gguf", callbacks=[StreamingStdOutCallbackHandler()]
)
embeddings = LlamaCppEmbeddings(model_path="./llama-2-7b.Q4_K_M.gguf")

docs = Docs(llm=llm, embeddings=embeddings)


# %%
# get a list of paths
docs = Docs(llm=llm, embeddings=embeddings)
my_docs = glob(os.getcwd() + '\documents\*')
print(my_docs)

for d in my_docs:
    docs.add(d,chunk_chars=500)

#test
answer = docs.query("What is an siRNA?", limit=3)
print(answer.formatted_answer) 
"""