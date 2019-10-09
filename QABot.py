from cdqa.utils.converters import pdf_converter
import pandas as pd
from ast import literal_eval
from cdqa.pipeline import QAPipeline
from cdqa.utils.filters import filter_paragraphs
from cdqa.utils.download import download_squad, download_model, download_bnpp_data
import speech_recognition as sr
import pyttsx3

# # Downloading data
# download_squad(dir='./data')
# download_bnpp_data(dir='./data/bnpp_newsroom-v1.1')

# # Downloading pre-trained BERT fine-tuned on SQuAD 1.1
# download_model('bert-squad_1.1', dir='./models')

def max_qa_bot(query):
    # df = pdf_converter(directory_path='C:/Users/kvsis/Desktop/Learning/Python Scripts/cdQA_project/data/pdf_files')
    df = pd.read_csv('C:/Users/kvsis/Desktop/Learning/Python Scripts/cdQA_project/data/data/data.csv', converters={'paragraphs': literal_eval})
    # df = filter_paragraphs(df)

    cdqa_pipeline = QAPipeline(reader='C:/Users/kvsis/Desktop/Learning/Python Scripts/cdQA_project/models/bert_qa_vCPU-sklearn.joblib')
    cdqa_pipeline.fit_retriever(df=df)

    # recognizer = sr.Recognizer()
    # # recognizer.pause_threshold = 5.0
    # with sr.Microphone() as source:
    #     # print("[search edureka: search youtube]")
    #     print("Speak Now")
    #     audio = recognizer.listen(source)
    #     query = recognizer.recognize_google(audio).capitalize()
    #     print(query)

    # query = "What is td ameritrade"
    prediction = cdqa_pipeline.predict(query)

    # print('query: {}\n'.format(query))
    # print('answer: {}\n'.format(prediction[0]))
    # print('title: {}\n'.format(prediction[1]))
    # print('paragraph: {}\n'.format(prediction[2]))
    
    # # Initializing the Text-to-Speech engine
    # engine = pyttsx3.init()

    # david = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    # zira = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    # engine.setProperty('rate', 150)
    # engine.setProperty('volume', 1.0)
    # engine.setProperty('voice', david)
    # engine.say(prediction[2])
    # engine.runAndWait()
    # engine.stop()

    # result = ('Question: {}\n'.format(query).capitalize()) + ('Answer: {}\n'.format(prediction[0]).capitalize()) + ('Subject: {}\n'.format(prediction[1]).capitalize()) + ('Paragraph: {}\n'.format(prediction[2]).capitalize())
    result = prediction[2].capitalize()
    return result
    