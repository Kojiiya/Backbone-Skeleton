from app import app
from flask import render_template, request, jsonify
import requests
from . import aiapi
from openai import OpenAI


chat_messages = []

@app.route('/')
@app.route('/home')
def home():
    return render_template('base.html', title='Home')

@app.route('/account')
def account():
    return render_template('base.html', title='Account')

@app.route('/forum')
def forum():
    return render_template('base.html', title='Forum')

@app.route('/activities')
def activities():
    return render_template('activities.html', title='Activities')

@app.route('/activities/scenarios')
def scenarios():
    return render_template('activities.html', title='Scenarios')

@app.route('/activities/simulations')
def simulations():
    return render_template('activities.html', title='Simulations')

@app.route('/activities/quiz')
def quiz():
    return render_template('activities.html', title='Quiz')


@app.route('/home/connectionTest')
def connectionTest():
    try:
        response = requests.get("http://www.google.com", timeout=5)
        if response.status_code == 200:
            return "Internet connection is working."
        else:
            return "Failed to connect to the internet."
    except requests.ConnectionError:
        return "Failed to connect to the internet. Check your network settings."


@app.route('/generate_chat_response', methods=['POST'])
def generate_chat_response():
    data = request.get_json()
    prompt = data.get('prompt', '')
    res = aiapi.generateChatResponse(prompt)
    return jsonify(res)



