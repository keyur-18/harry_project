# How to use this RAG assistant
## Step 1:Gather Videos
Move all your videos to videos folder in video_audio folder

## Step 2:Convert to mp3
convert all video files to audio by running process_videos.py

## Step 3:Convert mp3 to json
convert audio files to json by running video_to_json.ipynb
for free gpu use kaggle(you need to create dataset on kaggle to use audio files)

## Step 4: Convert json to vector & llm response
use embeddings.ipnb to convert json to vector
(to run embeddings.ipynb you need to download ollama from : https://ollama.com/download/windows , 
to download ollama model run command ollama pull bge-large-en-v1.5:q4_k_m and ollama pull llama3.2:3b)

## Step 5: imporve output
to improve output we merged chunks 
for this run merge_chunks ans last section of embeddings.ipynb 

## step 6: streamlit
to run this app on localhost run streamlit run app.py in terminal
