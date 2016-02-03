SmartThings Logger
==================

SmartApp Setup
--------------

### Installation

1. Go to https://graph.api.smartthings.com/
2. Go to 'My SmartApps'
3. Click on 'New SmartApp'
4. Open the 'From Code' tab
5. Copy and paste the code from smartapp/power_meter_api_endpoint into the text box
6. Click 'Create'

### Obtaining the OAuth Token

1. Go to 'My SmartApps'
2. Click on 'Power Meter API Endpoint'
3. If the simulator is not already open, click the 'Simulator' button
4. Click 'Set Location'
5. Choose a device and click install
6. Copy the OAuth Token from the corresponding text box in the simulator
7. Paste the OAuth Token into the 'oauth_token' variable in server/smartthings_logger.py

### Running the SmartApp

Do some stuff

Server Setup
------------

1. Install python https://www.python.org/downloads/
2. Install pip https://pip.pypa.io/en/stable/installing/
3. Install bottle:
<code>pip install bottle</code>
4. Install ipgetter:
<code>pip install ipgetter</code>
5. With the SmartApp already setup, run the server
<code>python power_meter_api_endpoint.py</code>
