import ollama
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def chat():
	return render_template("index.html")

@app.route("/response")
def response():
	message = request.args.get("message")
	response = ollama.chat(
		model="smollm2:135m", # mude de acordo com seu modelo ex:model="gwen3.2:4b"
		messages=[{"role": "user", "content":message}]
	)
	return jsonify({"response":response["message"]["content"]})


if __name__ == "__main__":
	app.run(debug=False)