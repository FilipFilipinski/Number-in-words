
# Number in words

This site was created to convert numbers from numeric form to written numbers. In the future I plan to expand it
        to more languages than English.




## API Reference

#### Get

```http
  GET /api/${value}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Input can only contain digits|

#### Example
```http
GET /api/1202
```

Result 
```json
{
  "1202": "one thousand two hundred two"
}
```



