#/bin/python3
import sys
import subprocess

command = ['hdfs', 'fsck', sys.argv[1], '-files', '-blocks', '-locations']
"""
HDFS output looks like the following:

```
0. BP-1135830572-93.175.29.106-1493426010892:blk_1074209870_469301 len=1914 Live_repl=2 [DatanodeInfoWithStorage[93.175.29.111:50010,DS-0618707d-c00c-4563-b7d8-ec217f4c972c,DISK], DatanodeInfoWithStorage[93.175.29.109:50010,DS-3b63d425-0f0e-45be-b954-f090a313119d,DISK]]
```
"""
print(subprocess.check_output(command).decode('utf-8')
                                      .split('\n')[2]
                                      .split('DatanodeInfoWithStorage')[1]
                                      .split(':')[0][1:])
