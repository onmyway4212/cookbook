line = 'nobody:*:-2:-2:unprivileged user:/var/empty:/usr/bin/false'

unname, *files, homedir, sh =line.split(':')

print(unname)
print(*files)
print(homedir)
print(sh)