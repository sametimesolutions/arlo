from arlo import Arlo
import base64

USERNAME = 'sametimesolutions@yahoo.com'
pw = 'Nosoup4u2!'
PASSWORD = str(base64.b64encode(pw.encode("utf-8")), "utf-8")

try:

    # Instantiating the Arlo object automatically calls Login(),
    # which returns an oAuth token that gets cached.
    # Subsequent successful calls to login will update the oAuth token.
    arlo = Arlo(USERNAME, pw)
    # At this point you're logged into Arlo.
    print(arlo)
    # Get the list of devices and filter on device type to only get the basestation.
    # This will return an array which includes all of the basestation's associated metadata.
    basestations = arlo.GetDevices('basestation')

    # Define a callback function that will get called once for each motion event.
    def callback(arlo, event):
        # Here you will have access to self, the basestation JSON object, and the event schema.
        print("motion event detected!")
        #print(basestation)
	#print(event)
	#print(arlo)

    # Subscribe to motion events. This method blocks until the event stream is closed.
    # (You can close the event stream in the callback if you no longer want to listen for events.)
    arlo.SubscribeToMotionEvents(basestations[0], callback)
except Exception as e:
    print(e)
