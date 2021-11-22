import sys
import subprocess

create = ['dd', 'if=/dev/zero', 'of=kok.tmp', 'bs=' + sys.argv[1], 'count=1']
subprocess.check_output(create)

put = ['hdfs', 'dfs', '-put', 'kok.tmp', '/tmp/kok.tmp']
subprocess.check_output(put)

delete_local = ['rm', 'kok.tmp']
subprocess.check_output(delete_local)

gather_blocks = ['hdfs', 'fsck', '/tmp/kok.tmp', '-files', '-blocks', '-locations']
blocks_info = subprocess.check_output(gather_blocks).decode('utf-8').split('BP')[1:]
print(blocks_info)

delete_remote = ['hdfs', 'dfs', '-rm', '/tmp/kok.tmp']
subprocess.check_output(delete_remote)
