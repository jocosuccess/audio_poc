import sounddevice as sd
import jack
print('*** List of Sound Devices ***')
print(sd.query_devices())
print('*****************************')
#client = jack.Client('PocClient')
#print('*** List of JACK Ports ***')
#print(client.get_ports())