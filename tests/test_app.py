# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===

"""
When I send a request GET /wave?name=Dana
I expect the status code to be 200 OK
And the response to be "I am wavng at Dana
"""

def test_get_wave_with_argument(web_client):
    response = web_client.get("/wave?name=Dana")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "I am waving at Dana"
