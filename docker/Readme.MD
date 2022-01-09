# cURL commands

## Hello endpoint
```shell
curl 'http://localhost:5000'
```

## Predict endpoint
```shell
curl --request POST 'http://localhost:5000/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
    "input": "value"
}'
```
