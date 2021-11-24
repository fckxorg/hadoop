import sys
import subprocess

def exec(cmd):
    return subprocess.check_output(cmd.split()).decode('utf-8')

exec('dd if=/dev/zero of=test.tmp bs=' + sys.argv[1] +' count=1')
exec('hdfs dfs -put test.tmp /tmp/test.tmp')
exec('rm test.tmp')
raw_block_ids = exec('hdfs fsck /tmp/test.tmp -files -blocks -locations')\
        .split('BP')[1:]

block_ids = []
for block in raw_block_ids:
    bid = block.split(':')[1].split()[0]
    block_ids.append(bid[:bid.rfind('_')])

disk_size = 0

for block in block_ids:
    url = exec('hdfs fsck -blockId ' + block)\
            .split('Block replica on datanode/rack: ')[1]\
            .split()[0]\
            .split('/default')[0]

    path = exec('sudo -u hdfsuser ssh hdfsuser@' + url + ' find /dfs -name ' + block)\
            .split()[0]
    disk_size += int(exec('sudo -u hdfsuser ssh hdfsuser@' + url + ' wc -c ' + path)\
            .split()[0])
exec('hdfs dfs -rm /tmp/test.tmp')
print(disk_size - int(sys.argv[1]))
