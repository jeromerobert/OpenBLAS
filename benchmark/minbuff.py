#! /usr/bin/env python

from subprocess import *

def run(buf, n, nthread, incx):
    return call(['./smallscaling'], stdout = PIPE, stderr=PIPE, env={
       'OPENBLAS_ZTRMV_BUF': str(buf),
       'OPENBLAS_PARAM_N': str(n),
       'OPENBLAS_NUM_THREADS': str(nthread),
       'OPENBLAS_INCX': str(incx),
    }) == 0

for nthread in xrange(1,5):
    for incx in [1,2]:
        print "nthread", nthread, "incx", incx
        prev_buf = 1
        for n in xrange(1, 1024):
            buf = prev_buf
            while not run(buf, n, nthread, incx):
                buf += 1
            prev_buf = buf
            print n, buf
