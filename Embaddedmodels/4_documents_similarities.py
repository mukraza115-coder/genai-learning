from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embadding=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001",dimensions=300)

documents=[
    "Babar Azam is a Pakistani cricketer and one of the world's leading batsmen. He has captained Pakistan in all formats and is known for his elegant cover drives and consistency.",

    "Shaheen Shah Afridi is a Pakistani left-arm fast bowler known for his pace, swing, and ability to take wickets with the new ball. He has played a key role in Pakistan's victories across all formats.",

    "Mohammad Rizwan is a Pakistani wicketkeeper-batsman recognized for his hard work, consistency, and match-winning performances in T20 Internationals and One Day Internationals.",

    "Naseem Shah is a young Pakistani fast bowler famous for his raw pace, reverse swing, and impressive performances against top international teams despite his young age.",

    "Shadab Khan is a Pakistani all-rounder and leg-spin bowler. He is known for his economical bowling, aggressive batting, and exceptional fielding abilities in limited-overs cricket."
]

querry="Who is shadab khan?"

doc_embaddings=embadding.embed_documents(documents)
querry_embadding=embadding.embed_query(querry)
socre=cosine_similarity([querry_embadding],doc_embaddings)[0]
index,score=sorted(list(enumerate(socre)),key=lambda x:x[1])[-1]

print(querry)
print(documents[index])
print("similarity score:",score)    
 