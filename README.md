
## インフラ
- イメージ作成  
    `docker-compose build`
    
- コンテナ起動  
    `docker-compose -d up`
    
    
## API
- curlでpost叩く  
    `curl http://localhost:5000/reply -X POST -H "Content-Type: application/json" -d '{"keyword": "power"}'

### The Web API Good Partsの例で組む

ユーザー一覧取得
- URL構成：http://localhost:5000/v1/users
- HTTPメソッド：GET
- curl: `curl http://localhost:5000/v1/users -X GET`

文字コード対応は別途考える

ユーザーの新規登録  

- URL構成：http://localhost:5000/v1/users
- HTTPメソッド：POST
- curl:``

特定ユーザーの情報取得  

- URL構成：http://localhost:5000/v1/userts/:id
- HTTPメソッド：GET
- curl:``

ユーザー情報の更新  

- URL構成：http://localhost:5000/v1/users/:id
- HTTPメソッド：PUT
- curl:``

ユーザー情報の削除  

- URL構成：http://localhost:5000/v1/users/:id
- HTTPメソッド：DELETE
- curl:``