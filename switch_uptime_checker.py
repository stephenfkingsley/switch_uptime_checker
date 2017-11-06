import paramiko

#This script is to make a dynamic list of switches that user enters and run a command to them all and print the output after.

uname = 'username'   #put your tacacs username in between quotes
p = 'password'     #put your tacacs password in between quotes

switchlist = []
def obtain_switch_name(): #function to create list of switches to run command on
    while True:
        sw = input("Enter Switch Name: ")
        if sw == 'done':
            break
        switchlist.append(sw)

obtain_switch_name()

for switch in switchlist:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect( switch, username = uname, password = p )
    except:
        print('ERROR: Not valid Switchname, Username, or Password!\n\nSwitch name used: ', switch, '\n\nUsername: ', uname, '\n\nIf username and switch are correct, check password.\n')
        continue
    stdin, stdout, stderr = ssh.exec_command( 'show version | i uptime|reset|Reason' )
    output = stdout.readlines()
    print('\n'.join(output))
