import os


o = os.environ
def h(opt,b):
    o['GIT_GCC'] = 'gcc'
    if os.path.exists('/usr/bin/gcc-4.2'):
        o['GIT_GCC'] = '/usr/bin/gcc-4.2'



