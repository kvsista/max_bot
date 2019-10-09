import wikipedia as wiki
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize

def get_data():
    topic = input("Enter a topic: ")
    summary = wiki.summary(topic)
    paras = sent_tokenize(summary)
    
    file = "C:/Users/kvsis/Desktop/Learning/Python Scripts/cdQA_project/data/data/data.csv"
    df = pd.read_csv(file)
    
    title = pd.DataFrame([topic.title()], columns=['title'])
    paragraphs = pd.DataFrame([[str(paras)]], columns=['paragraphs'])
    df = df.append(pd.concat([title, paragraphs], axis=1)).reset_index(drop=True)
    df.to_csv(file, index=False)

get_data()