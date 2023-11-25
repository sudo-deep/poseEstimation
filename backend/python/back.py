from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'

@app.route('/pose-estimation', methods=['POST'])
def run_python_script():
   try:
     subprocess.run(['python' , './app.py'])
     return jsonify({'message': 'running'}), 200
   except Exception as e:
     return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

