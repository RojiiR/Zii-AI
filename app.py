from flask import Flask, request, jsonify, render_template
import openai

openai.api_key = "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"


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    try:
        completion = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": user_message}]
        )
        bot_reply = completion.choices[0].message.content
        return jsonify({"reply": bot_reply})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
