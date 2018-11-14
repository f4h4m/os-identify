import subprocess
import re


def return_ttl(address):
    proc = subprocess.Popen(["ping %s -c 1" % address, ""], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    out = out.decode("utf-8")
    out = out.split()

    out[13] = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", out[13])
    return int(out[13][0])

while True:
    print('Enter :')
    addr = input()
    ttl = return_ttl(addr)
    if ttl>=0 and ttl<=64:
        print('mostly linux - %s ' % ttl)
    elif ttl>=65 and ttl<=128:
        print('mostly Windows - %s ' % ttl)
    elif ttl>=129 and ttl<=254:
        print('mostly Solaris/AIX - %s ' % ttl)
    else:
        print('unknown = %s' % ttl)



