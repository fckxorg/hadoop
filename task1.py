#/bin/python3
import sys
import subprocess

command = ['hdfs', 'fsck', sys.argv[1], '-files', '-blocks', '-locations']
"""
HDFS output looks like the following:

```
FSCK started by pd2021006 (auth:SIMPLE) from /93.175.29.107 for path /datasets/stop_words_en.txt at Tue Nov 16 22:17:49 UTC 2021
/datasets/stop_words_en.txt 1914 bytes, 1 block(s):  OK
```
"""
print(subprocess.check_output(command).decode('utf-8')
                                      .split('\n')[0]
                                      .split('from')[1]
                                      .split()[0][1:])

