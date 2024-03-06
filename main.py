from flask import Flask, render_template, request
from openai import OpenAI, chat
from openai import OpenAI
import os
os.environ["OPENAI_API_KEY"] = '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'


client = OpenAI()

app = Flask(__name__)

conversations = []



@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    if request.form['question']:
        question = 'Yo: ' + request.form['question']

        completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Eres un profesor de matemáticas, no puedes dar respuestas diferentes a las matemáticas, no puedes dar respuestas de español, ni de historia, si te preguntan algo que no esté relacionado con la matemáticas, diles que solo puedes contestar acerca de temas relacionados con las matemáticas"},
    {"role": "user", "content": question}
  ]
)
        
        response = completion.choices[0].message.content
        

        answer = 'Ai: ' + response

        conversations.append(question)
        conversations.append(answer)




        return render_template('index.html', chat = conversations)
    
    else: 
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=4000)