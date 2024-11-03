i = 1
pi = 3.1415927
mile = 5280 # ft
ft = 12 #inch
hour = 3600

while True:
    radius,spin,sec = input().split()
    radius,spin,sec = float(radius), int(spin), float(sec)
    if spin == 0:
        break
    d=radius*pi*spin/ft/mile
    e=d*hour/sec
    print('Trip #'+str(i)+':','{:.2f}'.format(d),'{:.2f}'.format(e))
    i += 1