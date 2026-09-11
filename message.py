import os
import random
from datetime import datetime, timezone

MESSAGES_DIR = 'messages'

if __name__ == '__main__':
    paths = [os.path.join(root, fn)
             for root, _, files in os.walk(MESSAGES_DIR)
             for fn in files]
    if not paths:
        raise SystemExit(f'no messages in {MESSAGES_DIR}/')

    with (
        open('README.template.md', encoding='utf-8') as templf,
        open(random.choice(paths), encoding='utf-8') as randf,
    ):
        out = (templf.read()
               .replace('{message}', randf.read())
               .replace('{utcDateTime}', datetime.now(timezone.utc).isoformat(timespec='seconds')))

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(out)
