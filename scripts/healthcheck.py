import requests

def check_health():
    """
    Automated script executing routine internal checks on pipelines and downstream APIs.
    """
    try:
        response = requests.get("http://localhost:8000/health")
        if response.status_code == 200:
            print("Backend is healthy")
        else:
            print(f"Backend returned status code {response.status_code}")
    except Exception as e:
        print(f"Health check failed: {e}")

if __name__ == "__main__":
    check_health()
