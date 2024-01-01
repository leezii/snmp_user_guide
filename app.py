from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        output = firstname + lastname
        if firstname and lastname:
            return jsonify({'output':'Your Name is ' + output + ', right?'})
        return jsonify({'error' : 'Missing data!'})
    return render_template('index.html')

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == "POST":
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        output = firstname + lastname
        print('get post request')
        print(output)
        if firstname and lastname:
            return jsonify({'output':'Your Name is ' + output + ', right?'})
        return jsonify({'error' : 'Missing data!'})
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(debug=True)
