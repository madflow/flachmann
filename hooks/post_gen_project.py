import subprocess
import sys


def execute(command):
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

    while True:
        nextline = process.stdout.readline()
        if nextline == b'' and process.poll() is not None:
            break

        sys.stdout.write(nextline.decode('utf-8'))
        sys.stdout.flush()

    output = process.communicate()[0]
    exit_code = process.returncode

    if exit_code == 0:
        return output
    else:
        raise Exception(command, exit_code, output)

execute('bower install')
