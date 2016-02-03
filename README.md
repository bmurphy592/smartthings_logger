# SmartThings Logger

## Setup

### Loading the SmartApp

1. Log in to https://graph.api.smartthings.com/
2. Go to 'My SmartApps'
3. Click on 'New SmartApp'
4. Open the 'From Code' tab
5. Copy and paste the code from <code>smartapp/power_meter_api_endpoint.groovy</code> into the text box
6. Click 'Create'

### Obtaining the OAuth token

1. Go to 'My SmartApps'
2. Click on 'Power Meter API Endpoint'
3. If the simulator is not already open, click the 'Simulator' button
4. Click 'Set Location'
5. Choose any device and click install
6. Copy the OAuth Token from the corresponding text box in the simulator
7. Paste the OAuth Token into the 'oauth_token' variable in <code>server/smartthings_logger.py</code>

### Running the SmartApp

1. Go to 'My SmartApps'
2. Click on 'Power Meter API Endpoint'
3. Click on 'Publish'
4. Open the SmartThings app on your mobile device
5. Open the 'Marketplace' tab
6. Select 'SmartApps'
7. Select 'My Apps', at the bottom of the menu
8. Select 'Power Meter API Endpoint'
9. Select the devices that you want to monitor
10. Select 'Done'

### Running the server

1. [Install python](https://www.python.org/downloads/)
2. [Install pip](https://pip.pypa.io/en/stable/installing/)
3. Install bottle: <code>pip install bottle</code>
4. Install ipgetter: <code>pip install ipgetter</code>
5. With the SmartApp already setup, run the server: <code>python power_meter_api_endpoint.py</code>

## Resources

[SmartApp Web Services](http://docs.smartthings.com/en/latest/smartapp-web-services-developers-guide/) <br>
[SmartThings Event Reference](http://docs.smartthings.com/en/latest/ref-docs/event-ref.html#event-ref) <br>
[SmartThings Capabilities Reference](http://docs.smartthings.com/en/latest/capabilities-reference.html#capabilities-taxonomy) <br>
