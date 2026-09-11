# mkdir

`mkdir` used to be a setuid-root binary. Creating a directory meant a `mknod` plus two `link` calls, none of it atomic and all of it root-only, so an entire separate program existed to fake a syscall that didn't exist yet.

_category: trivia_
