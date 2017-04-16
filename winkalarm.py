import httplib
import urllib
import pywink
import cgi
import json

def main():
    infile = open('inputs.txt', 'r')

    # Wasting first 6 lines because that's how I formatted it
    for x in range(0,6):
        infile.readline()

    # Read in client secrets and the like
    clientId = infile.readline().rstrip('\n')
    clientSecret = infile.readline().rstrip('\n')
    authUrl = infile.readline().rstrip('\n')
    accessTokenUrl = infile.readline().rstrip('\n')
    # print clientId, clientSecret, authUrl, accessTokenUrl

    url = "https://api.wink.com/oauth2/token"
    headers = {"Content-type": "application/json"}
    password = ""
    username = "alanc3939+wink@gmail.com"
    body = dict(
        client_id=clientId,
        client_secret=clientSecret,
        password=password,
        username=username,
        grant_type="password"
    )

    conn = httplib.HTTPSConnection("api.wink.com")
    url = "https://api.wink.com/oauth2/token"
    print json.dumps(body)
    conn.request("POST", url = "/oauth2/token" , headers = headers, body = json.dumps(body))
    response = conn.getresponse()
    print response.status, response.reason

    # pywink.set_bearer_token('YOUR_BEARER_TOKEN')
    # for switch in pywink.get_switches():
    #     print(switch.name(), switch.state())
    #     switch.set_state(not switch.state())
    
    return 0;

if __name__ == "__main__":
    main()