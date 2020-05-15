import os
import time

#Openstack server list
source = ". /root/creds && "

openstack_server_list = "openstack server list"
openstack_server_delete = "openstack server delete "

#openstack server list
server_list_display = os.popen(source + openstack_server_list).read()
print "openstack server list",server_list_display

#openstack stack list
stack_name = "clearwater-demo"
openstack_stack_delete = "openstack stack delete "
openstack_stack_list = "openstack stack list" 
openstack_stack_list_output = os.popen(source + openstack_stack_list).read()
print "openstack stack list", openstack_stack_list_output

#openstack stack deletion

if "clearwater-demo" in openstack_stack_list_output:
    print "Clearwater-demo stack found, deletion in progress"
    stdin,stdout = os.popen2(source + openstack_stack_delete + stack_name)
    stdin.write("y\n")
    stdin.close()
    stdout.close()
    while True:
        time.sleep (5)
        openstack_stack_list_output = os.popen(source + openstack_stack_list).read()
        if "clearwater-demo" not in openstack_stack_list_output:
            break
    print "Stack deletion success"

else:
    print "Clearwater stack is not found"

#openstack server delete 

#openstack_server_list_cut = "openstack server list | sed '1,3d;$d' | awk '{print $2}'"
#server_list=os.popen(source + openstack_server_list_cut).read().split()
#print "Openstack Server List", server_list
#server_list_length = len(server_list)

#if server_list_length==0:
#   print "No server available to delete"
#else:
#   for id in server_list:
#       print "Servers are available to delete"
#      os.popen(source + openstack_server_delete + "%s" %id)
#   server_list_display = os.popen(source + openstack_server_list).read()
#   print "servers are deleted",server_list_display

#VNF onboarding using heat stack command

dnskey = "head -c 64 /dev/random | base64 -w 0"
dnskey_output = os.popen(dnskey).read()

#heat_command = 'heat --debug stack-create clearwater-demo -f /root/clearwater_folder/clearwater.yaml -P "public_mgmt_net_id=d779595b-4d59-44c1-a310-cae87f247aa7;public_sig_net_id=d779595b-4d59-44c1-a310-cae87f247aa7;dnssec_key=' + dnskey_output + ';image=dba6451d-ef91-4296-89d9-6ca77bc34ac5;flavor=clearwater-flavor;key_name=clearwater-kp"'

heat_command = 'openstack stack create -t /root/clearwater_folder/clearwater.yaml --parameter "public_mgmt_net_id=d779595b-4d59-44c1-a310-cae87f247aa7;public_sig_net_id=d779595b-4d59-44c1-a310-cae87f247aa7;dnssec_key=' + dnskey_output + ';image=dba6451d-ef91-4296-89d9-6ca77bc34ac5;flavor=clearwater-flavor;key_name=clearwaterkeypair" clearwater-demo'


openstack_heat_exection = os.popen(source + heat_command)
time.sleep (5)

#checking heat stack status

def status_checking_function():
    openstack_stack_show = "openstack stack show clearwater-demo | grep 'stack_status ' | awk '{print $2,$4}' "
    print "\n\n\n Clearwater stack create in progress"
    while True:
        time.sleep (5)
        Stack_status = os.popen(source + openstack_stack_show).read().split()
        if "CREATE_COMPLETE" in Stack_status:
            break

    print "\n\n\n Clearwater stack creation successful",Stack_status

status_checking_function()
#Openstack server status

server_status = os.popen(source + openstack_server_list).read()

if "BUILD" not in server_status:
    print "\n\n All openstack servers are in ACTIVE state\n",server_status
else:
    print "All openstack servers are not in ACTIVE state"

#Scale out VM

scaleout_command = "openstack stack update  --parameter homer_cluster_size=2 --existing clearwater-demo"
scaleout_command_output = os.popen(source + scaleout_command)

openstack_stack_show = "openstack stack show clearwater-demo | grep 'stack_status ' | awk '{print $2,$4}' "
print "\n\n\n Clearwater stack update, Scale-out in progress"
while True:
    time.sleep (5)
    Stack_status = os.popen(source + openstack_stack_show).read().split()
    if "UPDATE_COMPLETE" in Stack_status:
        break

print "\n\n\n Clearwater stack updation successful",Stack_status

scaleout_status = os.popen(source + openstack_server_list).read()

if "homer-1.example.com" in scaleout_status:
    print "\n\n Scale out server is in ACTIVE state\n",scaleout_status
else:
    print "Scale out server is  not in ACTIVE state"


#Scale in VM

scalein_command = "openstack stack update  --parameter homer_cluster_size=1 --existing clearwater-demo"
scalein_command_output = os.popen(source + scalein_command)

openstack_stack_show = "openstack stack show clearwater-demo | grep 'stack_status ' | awk '{print $2,$4}' "
print "\n\n\n Clearwater stack update, Scale-in  in progress"
while True:
    time.sleep (5)
    Stack_status = os.popen(source + openstack_stack_show).read().split()
    if "UPDATE_COMPLETE" in Stack_status:
        break

print "\n\n\n Clearwater stack updation successful",Stack_status


scalein_status = os.popen(source + openstack_server_list).read()
if "homer-1.example.com" not in scalein_status:
    print "\n\n Scale in server process successful\n",scalein_status
else:
    print "Scale in server failed"
