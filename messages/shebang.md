# shebang

Put a long enough interpreter path in a shebang and the script just breaks, with no useful error. The kernel reads that first line into a fixed-size buffer (128 bytes for most of Linux's history) and silently truncates it. A script explaining how to run itself, cut off mid-word.

_category: ironic_
