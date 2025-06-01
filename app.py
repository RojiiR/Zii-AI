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
