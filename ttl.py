import subprocess
import re


def return_ttl_number(address):
    try:
        proc = subprocess.Popen(["ping %s -c 1" % address, ""], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        out = out.decode("utf-8").split()
        out[13] = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", out[13])
        return float(out[13][0])
    except Exception:
        pass


def return_ttl_os_name(ttl_number):
    ttl = ttl_number
    if ttl:
        if ttl >= 0 and ttl <= 64:
            return ('linux-ttl=%s' % ttl)
        elif ttl >= 65 and ttl <= 128:
            return('Windows-ttl=%s' % ttl)
        elif ttl >= 129 and ttl <= 254:
            return ('Solaris/AIX-ttl=%s' % ttl)
        else:
            return ('unknown=%s' % ttl)
    else:
        pass


f = open('data')
newF = open('newData','w')
for addr in f.readlines():
    addr = addr.strip()
    ttl = return_ttl_number(addr)

    newF.write('%s -> %s \n' % (addr,return_ttl_os_name(ttl)))
    print('%s -> %s' % (addr,return_ttl_os_name(ttl)))

