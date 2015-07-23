# User `/api/v1/user`


## `POST` - Register User
Registers a user for the Kerbos platform

`POST` body
```
{
  "username": <str>,
  "password": <str:Hashed>,
  "email": <str>
}

```
Response:
```
{
  "user_id": <int>`
}
```
