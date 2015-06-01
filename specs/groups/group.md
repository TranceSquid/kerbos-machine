# Groups `/api/v1/group/`


## Create Group `POST`
Creates a group for inviting members and sending messages

`POST` body
```
{
  "name": GROUP_NAME <Str>
}
```
Response:
```
{
  "group_id": GROUP_ID <int>`
}
```
