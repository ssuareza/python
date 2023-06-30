# ttsmms

Ttsmms is an API to make text-to-speech using Meta AI MMS. Is using [ttsmms](https://github.com/wannaphong/ttsmms) project.

## Usage

```bash
docker compose up ttsmms
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

### POST /tts

```
Content-Type: application/json
Authorization: Bearer {{api_key}}

{
"text": "this is a long text",
"lang": "eng"
}
```

It returns a wav file (`tmp/speech.wav`) with the speech.
