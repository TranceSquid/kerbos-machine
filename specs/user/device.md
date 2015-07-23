# Device `/api/v1/users/{user_id}/device`

## `GET` - Get a users device
Gets the latest used device of the user

Response:
```
{
  "device_name": <int>`,
  "public_key": <str>
}
```

## `POST` - Register a users device
Registers a device into the Kerbos platform. This allows a user to register a device with the public key to communicate to this device.

`POST` body`:
```
{
  "device_name": <str>,
  "public_key": <str>
}
```

Response:
```
{
  "device_id": <int>,
}
```
