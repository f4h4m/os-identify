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
            return ('mostly linux - ttl = %s ' % ttl)
        elif ttl >= 65 and ttl <= 128:
            return('mostly Windows - ttl = %s ' % ttl)
        elif ttl >= 129 and ttl <= 254:
            return ('mostly Solaris/AIX - ttl = %s ' % ttl)
        else:
            return ('unknown = %s' % ttl)
    else:
        pass


while True:
    print('Enter :',end='')
    addr = input()
    ttl = return_ttl_number(addr)
    print(return_ttl_os_name(ttl))
