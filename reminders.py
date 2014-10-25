from flask import (abort, flash, Flask, redirect, render_template, request,
                   session, url_for)

app = Flask(__name__)

# To use sessions, you need to specify
# a secret key which will be used to sign
# session data
app.config['SECRET_KEY'] = 'secret'

@app.route('/', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    if 'items' not in session:
      session['items'] = []

    if 'todelete' in request.form:
      app.logger.debug("Will delete: " + request.form['todelete'])
      if request.form['todelete'] in session['items']:
        session['items'].remove(request.form['todelete'])
    else:
      app.logger.debug("Will add: " + request.form['item'])
      session['items'].append(request.form['item'])

  if 'items' not in session or len(session['items']) < 1:
    items = ['No reminders set.']
  else:
    items = session['items']

  return render_template(
    'reminders.html',
    items=items,
  )

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
