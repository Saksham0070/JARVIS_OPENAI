import win32com.client
import speech_recognition as sr
import webbrowser as web
import openai
from apikeys import apikey
import os

def prompt_naming(prompt):
   words_to_remove = ['using','artificial','intelligence']

   words = prompt.split()
   filter_words = []
   
   for word in words:
      if word not in words_to_remove:
         filter_words.append(word)
   
   sentence = " ".join(filter_words)
   return sentence

chatStr = ""
def chatai(prompt_text):
   global chatStr

   openai.api_key = apikey
   
   chatStr += f"Me: {prompt_text}\nJarvis: "
   query = chatStr

   print(chatStr)
   response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt = chatStr,
    temperature=1,
    max_tokens=512,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
   print(response["choices"][0]["text"])
   
   chatStr += f"{response['choices'][0]['text']}\n"
   
   if(not os.path.exists("Openai_chat")):
      os.mkdir("Openai_chat")
   with open("Openai_chat/chat_with","a") as f:
      f.write(query)
      f.write(chatStr)
   
   read(response["choices"][0]["text"])

   return response["choices"][0]["text"]

def arti_intell(prompt_text):
   message = ""
   openai.api_key = apikey

   response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt = prompt_text,
    temperature=1,
    max_tokens=512,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
   message = message + response["choices"][0]["text"]
   message = message.strip()  # to remove the spaces

   print(response["choices"][0]["text"])
   # read(response["choices"][0]["text"])
   if( not os.path.exists("Openai")):
      os.mkdir("Openai")
   
   prompt_name = prompt_naming(prompt_text)
   print(prompt_name)
   message = prompt_name + "\n\n*******************************************************************\n\n" + message 
   with open(f"Openai/{prompt_name}","w") as f:
      f.write(message)


def takeCommand():
   path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
   recognizer=sr.Recognizer()
   with sr.Microphone() as source:
         
         print("Say something")
         recognizer.adjust_for_ambient_noise(source)

         audio = recognizer.listen(source)
         
         print("Recognizing.....")
         try:
           text = recognizer.recognize_google(audio,language="en-in")
         except sr.UnknownValueError:
            text = "Sorry, I could not understand what you said."
            read(text)
         except sr.RequestError as e:
            text = "Could not request results from the GoogleWeb Speech API "
            read(text)
         
         # print("You said :" + text)
         return text

def read(text):
  speaker = win32com.client.Dispatch("SAPI.SpVoice")
  s = text
  if(s=="exit"):
     return
  speaker.Speak(s)

read("Hello Sir!!, I am Jarvis!!How can I help you??")

while True:
   text = takeCommand()
   sites=[["youtube","https://youtube.com"],["google","https://google.com"],["wikipedia","https://www.wikipedia.org/"]]
   for site in sites:
      if f"Open {site[0]}".lower() in text.lower():
         read(f"Opening {site[0]} Sir....")
         web.open(site[1])
   
   if(f"Open Brave".lower() in text.lower()):
      os.system("C:\Program Files\BraveSoftware\Brave-Browser\Application")
   
   elif("using artificial intelligence".lower() in text.lower()):
      text_filter = prompt_naming(text)
      arti_intell(text_filter)

   elif("Thankyou".lower() in text.lower() or "Thank you".lower() in text.lower() ):
      read("Its an honour for me , Sir !!")
      read("Any Further Query Sir??")
      if(text.lower()=="No".lower() or text=="No jarvis".lower()):
         break
   elif("switch off".lower() in text.lower() or "turn off".lower() in text.lower()):
      read("Turning off Sir!!")
      exit()
   elif("clear chat".lower() in text.lower() or "reset chat".lower() in text.lower()):
      chatStr = ""
   else:
      chatai(text)