from flask import Flask, jsonify, render_template, send_file # import request to parse body for post/put routes
from flask_cors import CORS
import json



# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# read token.json file
with open('tokens.json', 'r') as myfile:
    data=myfile.read()
tokens = json.loads(data)

#get route to token.json file
@app.route('/api/tokens/<search>', methods=['GET'])
def select_token(search):
    res_tokens = {}

    for key in tokens:
        if search in tokens[key]['text']:
            res_tokens[key] = tokens[key]       
    response_object = {'status': 'success'}
    response_object['tokens'] = res_tokens
    return jsonify(response_object)

#get route to image
@app.route('/api/image/<index>', methods=['GET'])
def get_image(index):
    filename = 'image_' + index + '.png'
    return send_file(filename)



@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


if __name__ == '__main__':
    app.run()