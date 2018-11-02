
## インフラ
- イメージ作成  
    `docker-compose build`
    
- コンテナ起動  
    `docker-compose -d up`
    
    
## API
- curlでpost叩く  
    `curl http://localhost:5000/reply -X POST -H "Content-Type: application/json" -d '{"keyword": "power"}'
`