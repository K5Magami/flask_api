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

# ユーザー一覧取得
@app.route('/v1/users',methods=['GET'])
def getUsers():
    users = [{"id":1 , "name":"テスト太郎","hobby":"トレーニング"},{"id":2 ,"name":"テスト次郎","hobby":"読書"}]
    result = {
        "Content-Type":"application/json",
        "ReturnValue":{"Users":users}
    }
    return jsonify(result)

# ユーザーの新規登録
@app.route('/v1/users', methods=['POST'])
def signUpUser():
    data = json.loads(request.data)
    id = 3  # ロジック的には何かを呼び出して自動採番
    # パラメータ有無によってresponseにエラーコードを渡す
    name = data["name"]
    hobby = data["hobby"]

    # 成功時はHTTPステータス200にして、登録したUser情報を返す？？
    user = {"id":str(id), "name":name, "hobby":hobby}
    result = {
        "status":200,
        "Content-Type":"application/json",
        "result":True,
        "user":user,
        "error":""
    }
    return jsonify(result)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)