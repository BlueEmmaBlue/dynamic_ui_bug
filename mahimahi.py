import os
import time
import subprocess


PARENT_DIR = '/home/zhangwei/code'
RESULT_DIR = f'{PARENT_DIR}/result'
COMPLETE_COUNT = 0

def parse_sites():
    sites = []
    file_path = f'{PARENT_DIR}/top-1m.csv'
    with open(file_path, 'r') as f:
        for line in f:
            site = line.split(',')[1][:-1]
            sites.append(site)
    return sites


def reset_dir(site):
    os.system(f'rm -rf {RESULT_DIR}/{site}')
    os.system(f'mkdir {RESULT_DIR}/{site}')

def record_site(site):
    global COMPLETE_COUNT
    reset_dir(site)
    cmd = f'mm-webrecord {RESULT_DIR}/{site}/webrecord python3 {PARENT_DIR}/screen_shot.py {site} screenshot'
    p = subprocess.Popen(cmd,shell=True)
    p.wait()
    COMPLETE_COUNT += 1
    print(f'complete {site} {COMPLETE_COUNT}')

def replay_site(site):
    cmd = f'mm-webreplay {RESULT_DIR}/{site}/webrecord mm-deplay 100 mm-loss uplink 0.1 python3 {PARENT_DIR}/screen_shot.py {site}'

def clear_process():
    clear_cmd = '''
    ps -aux | grep mm-webrecord | grep -v grep | awk '{print $2}' | xargs kill
    '''
    subprocess.run(clear_cmd,shell=True)

import os

def getFileSize(filePath, size=0):
    for root, dirs, files in os.walk(filePath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
            # print(f)
    return size/1024


def record_site_list(sites):
    subprocess_list = []
    for site in sites:
        size = getFileSize('result/' + site)
        if size < 100:
            subprocess_list.append(record_site(site))

def main():
    sites = parse_sites()
    sites = sites[:20000]
    record_site_list(sites)

if __name__ == '__main__':
    main()
