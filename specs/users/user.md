# Groups `/api/v1/users/{user_id}`


## Create User `POST`
Creates a user for the Kerbos platform

`POST` body
```
{
  "username": <Str>,
  "password": <Str:Hashed>,
  "email": <Str>
}

```
Response:
```
{
  "user_id": <int>`
}
```
