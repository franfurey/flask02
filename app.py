from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title': 'Data Analyst',
    'location': 'Cordoba, Argentina',
    'salary': 'USD 2.000'
  },
  {
    'id':2,
    'title': 'Data Enginer',
    'location': 'San Francisco, USA',
    'salary': 'USD 3.000'
  },
  {
    'id':3,
    'title': 'Data Science',
    'location': 'Remote'
  },
  {
    'id':4,
    'title': 'Backend Python Developer',
    'location': 'Remote',
    'salary': 'USD 2.500'
  }
]


@app.route('/')
def hello():
  return render_template('home.html',
                         jobs=JOBS,
                        company_name='Jovian')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug = True)
