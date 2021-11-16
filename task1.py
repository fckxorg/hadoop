#/bin/python3
import sys
import subprocess

command = ['hdfs', 'fsck', None, '-files', '-blocks', '-locations']
command[2] = sys.argv[1]
print(subprocess.check_output(command).decode('utf-8').split('\n')[1].split('from')[1].split()[0])

