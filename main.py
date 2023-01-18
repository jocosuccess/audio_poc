import sounddevice as sd
import jack
print('*** List of Sound Devices ***')
print(sd.query_devices())
print('*****************************')
client = jack.Client('MainClient', no_start_server=True)
if client.status.server_failed:
    print(f'{jack.Status.server_failed}--------JACK server was failed')
else:
    print('JACK server was already running')
print('*** List of JACK Ports ***')
print(client.get_ports())