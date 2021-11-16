#/bin/python3
import sys
import subprocess

command = ['hdfs', 'fsck', sys.argv[1], '-files', '-blocks', '-locations']
print(subprocess.check_output(command).decode('utf-8').split('\n')[0].split('from')[1].split()[0][1:])

