import sys

w,h,v=map(int,sys.stdin.readline().strip().split())

uline=('Q'*w + '\n')
dline=('Q'*(w+v) + '\n')

up=uline*h
down=dline*w

L=(up+down).strip()

sys.stdout.write(L)

##for j in range(int(h)):
##    for i in range(int(w)):
##        print('Q',end='')
##    print()
##for i in range(int(w)):
##    for i in range(int(v)+int(w)):
##        print('Q',end='')
##    print()
