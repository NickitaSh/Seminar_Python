import subprocess
import chardet
import subprocess

def ping_web_resource(url):
    ping_cmd = ['ping', '-c', '4', '-W', '3', url]
    ping_proc = subprocess.run(ping_cmd, capture_output=True)
    if ping_proc.returncode == 0:

        encoding = chardet.detect(ping_proc.stdout)['encoding']
        output_str = ping_proc.stdout.decode(encoding, errors='replace')
        return output_str
    else:
        return f'Error pinging {url}'


print(ping_web_resource('yandex.ru'))
print(ping_web_resource('youtube.com'))
