from zk import ZK, const
from zk.finger import Finger

conn = None
zk = ZK('192.168.0.201', port=4370, timeout=5, password=0, force_udp=False, ommit_ping=False)


print ('Connecting to device ...')
conn = zk.connect()
print ('Disabling device ...')
conn.disable_device()
print ('Firmware Version: : {}'.format(conn.get_firmware_version()))


templates = []
for finger in range(10):
    print('finger'+str(finger))
    tmp = conn.get_user_template(2, finger)
    if tmp: #it's None if empty
        print(finger)
        print(tmp)
        templates.append(tmp)

  


print ('Enabling device ...')

conn.enable_device()
