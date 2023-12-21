
# %%
import nest_asyncio
nest_asyncio.apply()
import os
from dotenv import load_dotenv
load_dotenv()
# %%


# %%

from paperqa import Docs
from glob import glob

docs = Docs(llm='gpt-3.5-turbo')
my_docs = glob(os.getcwd() + '\documents\*\*')
print(my_docs)

for d in my_docs:
    docs.add(d)

#test
#answer = docs.query("What is an siRNA?", limit=3)
#print(answer.formatted_answer)







