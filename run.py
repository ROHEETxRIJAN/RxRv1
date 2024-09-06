import os, platform
 os.system('git pull')
bit = platform.architecture()[0]
if bit == '32bit':
    import RxR32
elif bit == '64bit':
    import RxR64
else: print(" YOUR DEVICE DOESN'T SUPPORT MY TOOL");exit()
 
