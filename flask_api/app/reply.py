from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"

@app.route('/reply', methods=['POST'])
def reply():
    data = json.loads(request.data)
    answer = "Yes ,it is %s!\n" % data["keyword"]
    result = {
        "Content-Type" : "application/json",
        "Answer":{"Text":answer}
    }

    return jsonify(result)


# Web API The Good Partsの内容を再現

@app.route('/v1/users',methods=['GET'])
def getUsers():
    users = [{"Id":1 , "Name":"テスト太郎","Hobby":"トレーニング"},{"Id":2 ,"Name":"テスト次郎","Hobby":"読書"}]
    result = {
        "Content-Type":"application/json",
        "ReturnValue":{"Users":users}
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)