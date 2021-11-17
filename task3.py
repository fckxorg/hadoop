#/bin/python3
import sys
import subprocess

command = ['hdfs', 'fsck', sys.argv[1], '-blocks']
print(subprocess.check_output(command).decode('utf-8')
                                      .split('Total blocks (validated):\t')[1]
                                      .split()[0])
