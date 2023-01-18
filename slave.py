import jack_server
import jack

server = jack_server.Server(
    name="SlaveServer",
    sync=True,
    realtime=True,
    driver="net"
)
server.start()

client = jack.Client('SlaveClient', no_start_server=True)
if client.status.server_failed:
    print(f'{jack.Status.server_failed}--------Slave JACK server was failed')
else:
    print('Slave JACK server was already running')
print('*** List of JACK Ports ***')
print(client.get_ports())