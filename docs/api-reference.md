# API Reference

## POST /resolve
Resolves a chama dispute.

### Request Body
```json
{
  "query": "string",
  "member_id": "string",
  "chama_id": "string",
  "context_files": ["string"]
}
```

### Response
```json
{
  "ruling": "string",
  "references": ["string"],
  "confidence_score": 0.95
}
```
