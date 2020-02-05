#!C:\Users\Hachidori\PycharmProjects\HashTableProject\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'hmac-cli==0.0.0','console_scripts','hmac'
__requires__ = 'hmac-cli==0.0.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('hmac-cli==0.0.0', 'console_scripts', 'hmac')()
    )
