#/bin/python3
import sys
import subprocess

command = ['hdfs', 'fsck', '-blockId', sys.argv[1]]
node = subprocess.check_output(command).decode('utf-8')
                                       .split('Block replica on datanode/rack: ')[1]
                                       .split()[0]
                                       .split('/default')[0]
ssh_host = 'hdfsuser@' + node

ssh_command = ['sudo', '-u', 'hdfsuser', 'ssh', ssh_host, "'locate ' + sys.argv[1]"]

path = subprocess.check_output(ssh_command).decode('utf-8').split()[0]
print(node + ':' + path)

