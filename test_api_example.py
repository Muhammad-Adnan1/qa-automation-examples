import requests

def test_get_request():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    
    assert response.status_code == 200
    data = response.json()
    assert "userId" in data
    assert "title" in data
    print("API test passed!")
    
if __name__ == "__main__":
    test_get_request()
