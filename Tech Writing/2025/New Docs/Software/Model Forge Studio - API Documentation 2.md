# ModelForge Studio – Core API Documentation
Version: 1.0.0  
Status: Prototype  
Last Update: 2025-11-28  

---

## 1. Overview
The **ModelForge Studio Core API** provides programmatic access to core features of the 3D modeling environment.  
This allows external applications and plugins to create, load, modify, and export 3D models without using the graphical interface.

This API is REST-based and communicates using **JSON**.  
All endpoints start with:


`https://api.modelforge.com/v1`

---

## 2. Authentication

### 2.1 API Key  
Every request must include an API Key in the header:
Authorization: Bearer your_api_key_here

Example:

GET /v1/models
Authorization: Bearer 81fa9001-a29d-4503-b210

If authentication fails, the server returns:

```json
{
  "error": "Unauthorized",
  "message": "Missing or invalid API key"
}
```
---
| Category  | Purpose                                   |
| --------- | ----------------------------------------- |
| Models    | Create, load, list, delete models         |
| Mesh      | Modify geometry of existing models        |
| Materials | Apply or update materials                 |
| Export    | Export models into different formats      |
| System    | Check health, version, and service status |
---

## 4. Models API
### 4.1 List Models
**GET/models**
Returns all models stored in the user workspace.
**Response**
```json 
{
  "models": [
    {
      "id": "mdl_101",
      "name": "Spaceship",
      "created_at": "2025-01-05",
      "polygons": 12400
    }
  ]
}
```
---
### 4.2 Create a new model
**POST/models**
Creates an empty model workspace.

**Requestbody**
```json
{
  "name": "NewModel"
}
```
**Response**
```json
{
  "id": "mdl_202",
  "name": "NewModel",
  "message": "Model successfully created"
}
```
---
### 4.3 Load a specific model
**GET/models/{model_id}**
Examples

```bash
GET /models/mdl_202
```
**Response**
```json
{
  "id": "mdl_202",
  "name": "NewModel",
  "polygons": 0,
  "materials": []
}
```
---
### 4.4 Delete a model
**DELETE/model/{model_id}**
**Response**
 ```json
 {
  "status": "deleted",
  "id": "mdl_202"
}
 ```
 ---
 ## Mesh Editing API
 ### 5.1 Add geometry
 **POST/models/{id}/mesh/add**

 Adds primitive objects (cube, sphere, plane).

 ### Body
 ```json
 {
  "primitive": "cube",
  "size": 1
}
```
**Response**
```json
{
  "model_id": "mdl_101",
  "geometry_added": "cube",
  "polygons": 720
}
```
---
### 5.2 Extrude faces
**POST/models/{id}/mesh/extrude**
```json
{
  "face_id": 12,
  "distance": 0.5
}
```
### 5.3 Apply subdivision
**POST /models/{id}/mesh/subdivide**
```json
{
  "iterations": 2
}
``` 
---
## 6. Materials API
### 6.1 List materials
**GET/materials**
## Response
```json
{
  "materials": [
    { "id": "mat_01", "name": "Metal", "type": "PBR" }
  ]
}
```
---
### 6.2 Apply material
**POST /models/{id}/materials/apply**
```json
{
  "material_id": "mat_01"
}
```
---
### 6.3 Create custom material
**POST/materials**
```json
{
  "name": "CustomBlue",
  "color": "#2045FF",
  "roughness": 0.4
}
```
---
## 7. Export
### 7.1 Export model
**POST /models/{id}/export**
### Body
```json
{
  "format": "obj",
  "apply_modifiers": true
}
```


