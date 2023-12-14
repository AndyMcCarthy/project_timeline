# %%
from paperqa import Docs
from glob import glob
# get a list of paths

my_docs = glob.glob('*/documents/*.pdf')
print(my_docs)
docs = Docs(llm='gpt-3.5-turbo')
for d in my_docs:
    docs.add(d)

answer = docs.query("What manufacturing challenges are unique to bispecific antibodies?")
print(answer.formatted_answer)