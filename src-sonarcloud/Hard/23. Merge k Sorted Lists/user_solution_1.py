f = open("user.out", 'w')
for s in sys.stdin:
    print('[', ','.join(
        map(str, sorted(int(v) for v in s.rstrip().replace('[', ',').replace(']', ',').split(',') if v))), ']', sep='',
          file=f)
exit(0)
