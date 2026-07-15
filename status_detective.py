import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(f"=" * 40)
print(f"GET /posts/1")
print(f"Status: {response.status_code} (Success)")
print(f"Description: Request succeeded - resource returned.")
print(f"=" * 40)


response = requests.get("https://jsonplaceholder.typicode.com/posts/99999")
print(f"=" * 40)
print(f"GET /posts/99999")
print(f"Status: {response.status_code} (Failure)")
print(f"Description: Resource Not Found.")
print(f"=" * 40)


response = requests.post("https://jsonplaceholder.typicode.com/posts")
print(f"=" * 40)
print(f"POST /posts")
print(f"Status: {response.status_code} (Created)")
print(f"Description: New Resource Created.")
print(f"=" * 40)


response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(f"=" * 40)
print(f"DELETE /posts/1")
print(f"Status: {response.status_code} (Success)")
print(f"Description: Resource Deleted.")
print(f"=" * 40)


response = requests.get("https://jsonplaceholder.typicode.com/invalideendpoint")
print(f"=" * 40)
print(f"GET /invalidendpoint")
print(f"Status: {response.status_code} (Failure)")
print(f"Description: Invalid Endpoint.")
print(f"=" * 40)


response = requests.get("https://jsonplaceholder.typicode.com/users/1/todos")
print(f"=" * 40)
print(f"GET /users/1/todos")
print(f"Status: {response.status_code} (Success)")
print(f"Description: Requst succeeded - resource returned.")
print(f"=" * 40)
