# grammar

Grammar is an API to correct grammar errors.

## Usage

```bash
docker compose up grammar
```

## Endpoints

### GET /healthz

Returns the health of the API.

### GET /auth

To test the auth middleware.

```
Content-Type: application/json
Authorization: Bearer {{api_key}}
```

The `API_KEY` is defined in the `env.dev` file.

### POST /

```
Content-Type: application/json
Authorization: Bearer {{api_key}}

{
"text": "He are moving here",
}
```
