#! /usr/bin/env python

from subprocess import *

def run(buf, n):
    return call(['./smallscaling'], stdout = PIPE, stderr=PIPE, env={
       'OPENBLAS_ZTRMV_BUF': str(buf),
       'OPENBLAS_PARAM_N': str(n),
       'OPENBLAS_NUM_THREADS': '1'
    }) == 0

prev_buf = 1
for n in xrange(1, 1024):
    buf = prev_buf
    while not run(buf, n):
        buf += 1
    prev_buf = buf
    print n, buf 
