import os
import urllib.parse
import random
from datetime import datetime, timezone

MESSAGES_DIR = 'messages'

if __name__ == '__main__':
    paths = [
        os.path.join(MESSAGES_DIR, fn)
        for _, _, files in os.walk(MESSAGES_DIR)
        for fn in files]

    with (
        open('README.template.md', 'r') as templf,
        open('README.md', 'w') as f,
        open(random.choice(paths)) as randf):
            f.write(templf.read()
                .replace(r'{message}', randf.read())
                .replace(r'{utcDateTime}', str(datetime.now(timezone.utc)))
