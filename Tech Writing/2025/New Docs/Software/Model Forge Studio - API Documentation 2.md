# Model Forge Studio – API Documentation  
Version: 2  
Status: Draft  

## Overview
The Model Forge Studio API allows external applications, plugins, and tools to interact with the 3D modeling environment.  
This includes functionalities for **model creation**, **rendering**, **asset management**, and **export operations**.

The API uses **REST principles** and communicates via **JSON**.  
All endpoints are prefixed with:

`https://api.modelforgestudio.com/v1`

---

# 1. Authentication

The API uses **API Keys** for authentication.  
Include your key in all requests using the header:
x-api-key: YOUR_API_KEY


## Error: Missing or invalid key
401 Unauthorized


---

# 2. Endpoints

---

# 2.1. Project Management

## **Create Project**
`POST /projects`

Create a new 3D project inside Model Forge Studio.

### Request Body
```json
{
  "name": "My New Project",
  "description": "First API test project"
}
```
### Response (201)

```json
{
  "projectId": "p_44931",
  "name": "My New Project",
  "createdAt": "2025-02-19T14:22:00Z",
  "status": "created"
}
```
---
### List Projects
`GET /projects`

### Response (200)
 ```json
[
  {
    "projectId": "p_44931",
    "name": "My New Project",
    "lastModified": "2025-02-19T14:22:00Z"
  },
  {
    "projectId": "p_44921",
    "name": "Demo Render",
    "lastModified": "2025-02-14T09:10:32Z"
  }
]
```
---

### Delete Project
`DELETE/projects/{projectId}`
### Response

```json
{
    "deleted": true
}
```
---
## 2.2 Model Operations
### Upload 3D Model
`POST /models/upload`

Used to Import 3D files into a project.

### Request (multipart/form-data)
```makefile
file: model.fbx
projectId: p_44931
```
### Response

```json
{
  "modelId": "m_32891",
  "projectId": "p_44931",
  "filename": "model.fbx",
  "status": "processing"
}
```
---
### List Models
`GET /projects/{projectId}/models`

### Response
```json
[
  {
    "modelId": "m_32891",
    "filename": "model.fbx",
    "status": "ready"
  }
]
```
---

## 2.3 Rendering Engine
### Start Render
`POST/render/start`
### Request Body
```json
{
  "projectId": "p_44931",
  "resolution": "1920x1080",
  "quality": "high"
}
```
### Response
```json
{
    "renderId": "r_12044",
    "status": "queued"
}
```
---
### Get Render Status
`GET /render/{renderId}`

### Response
```json
{
  "renderId": "r_12044",
  "status": "complete",
  "outputUrl": "https://cdn.mfstudio.com/renders/r_12044.png"
}
```
---
## 2.4 Material Library
### List Materials
`GET/materials`
### Response
```json
[
  {
    "materialId": "mat_204",
    "name": "Brushed Metal",
    "category": "metal"
  },
  {
    "materialId": "mat_312",
    "name": "Soft Plastic",
    "category": "plastic"
  }
]
```
---
## Apply Material to Model
`POST/materials/apply`

### Request Body
```json
{
    "modelId" : "m_32891",
    "materialId" : "mat_204"
}
```
### Response
```json
{
  "updated": true,
  "modelId": "m_32891",
  "materialId": "mat_204"
}
```
---
## 2.5 Exporting Models
### Export Model
`POST/export`

### Request Body
```json
{
  "modelId": "m_32891",
  "format": "GLTF"
}
```
### Response
```json
{
  "exportId": "ex_90022",
  "downloadUrl": "https://cdn.mfstudio.com/export/ex_90022.gltf"
}
```
---

## 3. Error Codes
| Code | Meaning                               |
| ---- | ------------------------------------- |
| 400  | Invalid request format                |
| 401  | Missing or invalid API key            |
| 404  | Resource not found                    |
| 409  | Conflict (ex: render already running) |
| 500  | Internal server error                 |

---

### 4. Rate Limits
Each API Key is allowed
*  **500 requests/minute**
*  **15,000 requests/day**

Exceding this returns:
```json
429 Too Many Requests
```