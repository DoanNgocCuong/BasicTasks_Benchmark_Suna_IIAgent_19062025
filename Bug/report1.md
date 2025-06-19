[II AGENT BUG LÚC 10H45]
Trước đó em vẫn dùng bình thường, đến khoảng 10h45 thì bị bug. 

1. Ban đầu là lỗi: 

```bash
Error running agent: Error code: 400 - {'error': {'message': 'Provider returned error', 'code': 400, 'metadata': {'raw': '{"type":"error","error":{"type":"invalid_request_error","message":"messages.1.content.0.text.text: Input should be a valid string"}}', 'provider_name': 'Anthropic'}}, 'user_id': 'user_2xg091Oyl2aXabutYXFRr5ArDR5'}
```
Link Video bug: https://drive.google.com/file/d/1dpnwacpTgi1OWpMIQcLtYNM2ej056Nv9/view?usp=sharing

----
Đến khoảng 11h thì lỗi: 
```bash
❗ Error initializing agent: filedescriptor out of range in select()
❗ Agent not initialized for this session
```