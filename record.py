import os
import time
import subprocess


PARENT_DIR = '/home/shiweiyan/code'
RESULT_DIR = f'{PARENT_DIR}/result'

def parse_sites():
    sites = []
    file_path = f'{PARENT_DIR}/top-1m.csv'
    with open(file_path, 'r') as f:
        for line in f:
            site = line.split(',')[1][:-1]
            sites.append(site)
    return sites


def clear(site):
    os.system(f'rm -rf {RESULT_DIR}/{site}')

def record_site(site):
    clear(site)
    cmd = """
    mm-webrecord {result_dir}/{site} chromium-browser --test-type --ignore-privacy-errors --ignore-certificate-errors --ignore-ssl-errors --user-data-dir=/tmp/nonexistent$(date +%s%N) https://www.{site}
    """.format(**{'result_dir': RESULT_DIR,'site': site}).strip()
    p = subprocess.Popen(cmd,shell=True)
    try:
        p.communicate(timeout=20)
        p.wait()
        p.kill()
    except:
        p.kill()
    return p

def record_site_list(sites):
    subprocess_list = []
    for site in sites:
        subprocess_list.append(record_site(site))
    for sp in subprocess_list:
        pass
#        sp.communicate(timeout=20)
#        sp.kill()

def main():
    sites = parse_sites()
    sites = sites[:10]
    # sites = [site for site in sites if 'baidu' in site]
    record_site_list(sites)

if __name__ == '__main__':
    main()
