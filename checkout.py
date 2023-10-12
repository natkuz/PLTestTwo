import subprocess

def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def get_hash(cmd):
    res = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8').stdout
    return res