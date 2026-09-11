`:x` does what `:wq` does, except it skips the write if nothing changed, so it won't bump the mtime and wake up your file watcher. Almost nobody uses it.
