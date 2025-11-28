# Model Forge Studio API Documentation
API Version: 1.0  
Base URL: `https://api.modelforge.studio/v1`

The Model Forge Studio API allows developers to integrate 3D model generation, rendering, asset management, and user automation directly into external applications.  
This document provides all endpoints, authentication rules, examples, parameters, and error structures.

---

# 1. Authentication

## 1.1 API Key
All requests require an API key passed in the header:

```
Authorization: Bearer YOUR_API_KEY
```

## 1.2 Example Request Using API Key

```
curl -X GET "https://api.modelforge.studio/v1/models" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

---

# 2. Models

Endpoints responsible for creating, listing, generating and deleting 3D models inside Model Forge Studio.

---

## 2.1 Create a Model
`POST /models/create`

### Description
Creates a new 3D model based on parameters such as name, category, size and rendering detail.

### Request Body
```
{
  "name": "SciFi Helmet",
  "category": "Armor",
  "detailLevel": "high",
  "texture": true
}
```

### Successful Response
```
{
  "id": "mdl_8932asd01",
  "name": "SciFi Helmet",
  "status": "created",
  "createdAt": "2025-02-01T14:22:00Z"
}
```

---

## 2.2 List Models
`GET /models`

### Description
Returns a list of all models created by the authenticated user.

### Successful Response
```
[
  {
    "id": "mdl_8932asd01",
    "name": "SciFi Helmet",
    "status": "rendered"
  },
  {
    "id": "mdl_4002asb55",
    "name": "Wooden Chair",
    "status": "draft"
  }
]
```

---

## 2.3 Generate Render
`POST /models/{id}/render`

### Description
Generates a high-resolution render of a selected model.

### Request Body
```
{
  "resolution": "4k",
  "lighting": "studio",
  "background": "white"
}
```

### Successful Response
```
{
  "renderId": "rndr_23893asd",
  "modelId": "mdl_8932asd01",
  "status": "processing"
}
```

---

## 2.4 Delete Model
`DELETE /models/{id}`

### Description
Deletes a model permanently.

### Successful Response
```
{
  "deleted": true,
  "id": "mdl_8932asd01"
}
```

---

# 3. Assets

Asset endpoints manage textures, materials, and downloadable files linked to models.

---

## 3.1 Upload Asset
`POST /assets/upload`

### Request Body
```
{
  "name": "metal_texture",
  "type": "texture",
  "fileUrl": "https://fileserver.com/metal.jpg"
}
```

### Successful Response
```
{
  "assetId": "ast_82293asd",
  "status": "uploaded"
}
```

---

## 3.2 List Assets
`GET /assets`

### Successful Response
```
[
  {
    "assetId": "ast_82293asd",
    "name": "metal_texture",
    "type": "texture"
  }
]
```

---

# 4. Users

---

## 4.1 Get User Profile
`GET /user`

### Successful Response
```
{
  "id": "usr_9901asdd",
  "email": "user@example.com",
  "plan": "pro",
  "modelsCreated": 42
}
```

---

# 5. Errors

All errors follow the same structure:

```
{
  "error": {
    "code": "MODEL_NOT_FOUND",
    "message": "The requested model does not exist.",
    "status": 404
  }
}
```

## Common Error Codes

| Code | Meaning |
|------|---------|
| INVALID_API_KEY | Your API key is incorrect or missing |
| MODEL_NOT_FOUND | The model ID does not exist |
| ASSET_UPLOAD_FAILED | File format invalid or corrupted |
| RATE_LIMIT_EXCEEDED | Too many requests in a short time |

---

# 6. Rate Limits

| Plan | Limit |
|------|--------|
| Free | 100 requests/day |
| Pro | 10,000 requests/day |
| Enterprise | Unlimited |

---

# 7. Webhooks

## 7.1 Render Completed
Triggered when a render finishes processing.

**Endpoint you must provide:**
```
POST /webhook/renderCompleted
```

**Payload sent to your endpoint:**
```
{
  "renderId": "rndr_23893asd",
  "modelId": "mdl_8932asd01",
  "status": "completed",
  "renderUrl": "https://cdn.modelforge.com/renders/rndr_23893asd.png"
}
```

---

# End of Documentation
