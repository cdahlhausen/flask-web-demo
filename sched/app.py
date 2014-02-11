from flask import Flask
from flask import url_for

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World!'

@app.route('/', subdomain='<eggo>')
def eggo_hello():
	return 'Hello EGGO World!'


if __name__ == '__main__':
	app.run(debug=True)

@app.route('/appointments/')
def appointment_list():
  return 'Listing of all appointments we have.'

@app.route('/appointments/<int:appointment_id>/')
def appointment_detail(appointment_id):
 # edit_url =  url_for('noel', appointment_id=appointment_id)
#  return edit_url
  #return the URL string just for demonstration
  return ' Detail of appointment        #{}.'.format(appointment_id)

@app.route('/appointments/<int:appointment_id>/edit/', methods=['GET', 'POST'])

#@app.route(...) and def appointment_edit(...).

def appointment_edit(appointment_id):
  return 'Form to edit appointment #.'.format(appointment_id)

@app.route('/appointments/create/', methods=['GET', 'POST'])
def appointment_create():
  return 'Form to create a new appointment.'

@app.route('/appointments/<int:appointment_id>/delete/', methods=['DELETE'])
def appointment_delete(appointment_id):
  raise NotImlementedError('DELETE')
