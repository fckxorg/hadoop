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

for block in blocks_info:
    blk_id = block.split(':')[1].split()[0]
    blk_id = blk_id[:blk_id.rfind('_')]
    get_node_list = ['hdfs', 'fsck', '-blockId', blk_id]
    node = subprocess.check_output(get_node_list).decode('utf-8')\
                                       .split('Block replica on datanode/rack: ')[1]\
                                       .split()[0]\
                                       .split('/default')[0]
    ssh_host = 'hdfsuser@' + node
    ssh_command = ['sudo', '-u', 'hdfsuser', 'ssh', ssh_host, 'locate', blk_id]
    path = subprocess.check_output(ssh_command).decode('utf-8').split()[0]
    print(blk_id + ':' + path)

delete_remote = ['hdfs', 'dfs', '-rm', '/tmp/kok.tmp']
subprocess.check_output(delete_remote)
