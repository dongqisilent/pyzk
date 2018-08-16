from zk import ZK, const
from zk.finger import Finger

conn = None
zk = ZK('192.168.0.201', port=4370, timeout=5, password=0, force_udp=False, ommit_ping=False)
zk2 = ZK('192.168.0.202', port=4370, timeout=5, password=0, force_udp=False, ommit_ping=False)


print ('Connecting to device ...')
conn = zk.connect()
conn2 = zk2.connect()
print ('Disabling device ...')
conn.disable_device()
print ('Firmware Version: : {}'.format(conn.get_firmware_version()))
# print '--- Get User ---'
users = conn.get_users()
for user in users:
    privilege = 'User'
    if user.privilege == const.USER_ADMIN:
        privilege = 'Admin'

    print ('- UID '.format(user.uid))
    print ('  Name       : {}'.format(user.name))
    print ('  Privilege  : {}'.format(privilege))
    print ('  Password   : {}'.format(user.password))
    print ('  Group ID   : {}'.format(user.group_id))
    print ('  User  ID   : {}'.format(user.user_id))



templates =  conn.get_templates()
for template in templates:
    if isinstance(template,Finger):
        print(template.template)
        if template.uid == 2:
            user.user_id=1000
            conn2.save_user_template(user,fingers=[template])


print(conn.get_face_version())


print ("Voice Test ...")
conn.test_voice()
print ('Enabling device ...')

conn.enable_device()
