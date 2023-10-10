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

"""
When i send a request POST/submit
with arguments name = Dana and message ='Hello'
I expect the status code to be 200 OK
And the response to be 'Thanks Dana, you sent this message:'Hello"
"""

def test_post_name_augment_with_message_(web_client):
    response = web_client.post('/submit',data={
        'name':'Dana',
        'message':'Hello'
        })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Thanks Dana, you sent this message:Hello"

# File: tests/test_app.py

"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'