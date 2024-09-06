import os, platform
 
print('\033[1;37m\u001b[31m>>\033[0m\033[1;37m WAIT SOMETIME...!');os.system('git pull');print('')
bit = platform.architecture()[0]
if bit == '32bit':
    import RxR32
elif bit == '64bit':
    import RxR64
else: print(" YOUR DEVICE DOESN'T SUPPORT MY TOOL");exit()
 
