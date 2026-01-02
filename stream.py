#importing requirments
import pandas as pd
import ollama
import os
import json
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

    
def create_embeddings(l):
    res = ollama.embed(
    model="qllama/bge-large-en-v1.5:q4_k_m",
    input=l
    )
    
    vector = res["embeddings"]
    return vector
def inference(prompt):
    model =ollama.generate(
        model="llama3.2:3b",
        prompt=prompt,
        stream=False
    )
    response =  model["response"]
    return response

def ask(query):
    df = pd.read_pickle("merge_data.pkl")
    incoming_query = query
    question_embedding = create_embeddings(incoming_query)[0]
    
    similarities  =cosine_similarity(np.vstack(df['embeddings']),[question_embedding]).flatten()
    top_results = 5
    max_idx = similarities.argsort()[::-1][0:top_results]
    new_df  = df.loc[max_idx]
    context_blocks = []
    for index,item in new_df.iterrows():
        context_blocks.append(f'''lecure title:{item["title"]},lecure number:{item["number"]},lecture text:{item["text"]},lecture timings:{item["Start"]}-{item["end"]}''')
    
    prompt = f'''You are a teaching assistant.

Use ONLY the lecture content below.
Follow this STRICT format:

Topic:
<one line>

Lecture details:
- Title:
- Lecture number:
- Video timestamps:

Explanation:
<short explanation>

Learning steps:
- Step 1
- Step 2

Do NOT combine title and lecture number.
Do NOT invent names.
Do NOT use general programming knowledge.
Use ONLY the lecture content provided, even if it seems incomplete.


Lecture content:
{context_blocks}

Question:
{incoming_query}

    '''
    response = inference(prompt=prompt)
    return response


