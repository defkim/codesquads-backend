# Registration

## Request

**POST `/auth/djoser/users/create/`**

- e.g: http://api.teamof.codes/auth/djoser/users/create/

**Headers**
```
Accept:application/json
Content-Type:application/json
```

**Body**
```json
{
    "phone": 13888888888,
    "email": "test@email.com",
    "password": "hahaha233"
}
```


## Response

**Status Code: 201 CREATED**

```json
{
    "phone": 13888888888,
    "email": "test@email.com",
    "id": 7
}
```


# Login

## Request

**POST `/auth/djoser/token/create/`**

- e.g: http://api.teamof.codes/auth/djoser/token/create/

**Headers**
```
Accept:application/json
Content-Type:application/json
```

**Body**
```json
{
    "password": "hahaha233",
    "email": "test@email.com"
}
```

## Response

**Status Code: 201 CREATED**

```json
{
    "auth_token": "297079653492eded6e88f745aea864edc838586c"
}
```



# Get my profile

## Request

**GET `/auth/djoser/me/`**

- e.g: http://api.teamof.codes/auth/djoser/me/

**Headers:**
```
Accept:application/json
Content-Type:application/json
Authorization:Token 297079653492eded6e88f745aea864edc838586c
```

## Response

**Status Code: 200 OK**

```json
{
    "phone": 13844444444,
    "id": 7,
    "email": "test@email.com"
}
```
