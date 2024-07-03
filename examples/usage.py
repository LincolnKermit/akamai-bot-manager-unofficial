import requests as s


headers = {"put some headers"}


# Initial requests to get appropriate cookie on the main page

request_get = s.get("https://google.com/" headers=headers)


# Final requests with the cookies and the payload

payload = {
"user": "joe",
"password": "doe"
}


requests_post = s.post("https://google.com/login" headers=headers, cookie=request_get.cookie)

print(requests_post.text)

# Note that cookies may also be in the headers.
# Note also that cookie may contains date or time and can be rejected if the time doesn't match.
