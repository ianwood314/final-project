# api.py

from flask import Flask

app = Flask(__name__)

@app.route('/jobs', methods=['POST'])
def jobs_api():
      """
      API route for creating a new job to do some analysis. This route accepts a JSON payload
      describing the job to be created.
      """
      try:
          job = request.get_json(force=True)
      except Exception as e:
          return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
      return json.dumps(jobs.add_job(job['start'], job['end']))

@app.route('/test', methods=['GET'])
def hello_world():
    return 'Hello World\n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
