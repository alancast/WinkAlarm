import httplib
import pywink
import json

def main():
    infile = open('inputs.txt', 'r')

    # Wasting first 7 lines because that's how I formatted it
    for x in range(0,7):
        infile.readline()

    # Read in client secrets and the like
    clientId = infile.readline().rstrip('\n')
    clientSecret = infile.readline().rstrip('\n')
    authUrl = infile.readline().rstrip('\n')
    accessTokenUrl = infile.readline().rstrip('\n')
    refreshToken = infile.readline().rstrip('\n')
    # print clientId, clientSecret, authUrl, accessTokenUrl, refreshToken

    accessToken = AcquireAccessToken(clientId, clientSecret, refreshToken)
    # print accessToken

    pywink.set_bearer_token(accessToken)

    DimLights()
    ToggleSwitches()
    
    return 0;

def AcquireAccessToken(clientId, clientSecret, refreshToken):
    # Populate information needed for request
    url = "https://api.wink.com/oauth2/token"
    headers = {"Content-type": "application/json"}
    body = dict(
        client_id=clientId,
        client_secret=clientSecret,
        refresh_token=refreshToken,
        grant_type="refresh_token"
    )

    # Send the request and get the response
    conn = httplib.HTTPSConnection("api.wink.com")
    conn.request("POST", url = "/oauth2/token" , headers = headers, body = json.dumps(body))
    response = conn.getresponse()
    if response.status != 200:
        print response.status, response.reason
        exit(1)
    
    responseStr = response.read().decode('utf-8')
    responseJson = json.loads(responseStr)
    # print responseJson

    return responseJson['access_token']

def ToggleSwitches():
    for switch in pywink.get_switches():
        print "-------------------------------"
        name = switch.name()
        state = switch.state()
        print name, state
        print "-------------------------------"
        switch.set_state(not state)

def DimLights():
    for bulb in pywink.get_light_bulbs():
        print "-------------------------------"
        print(bulb.name(), bulb.state())
        currentBrightness = bulb.brightness()
        print currentBrightness
        bulb.set_state(True, brightness = .6)
        print "-------------------------------"

if __name__ == "__main__":
    main()