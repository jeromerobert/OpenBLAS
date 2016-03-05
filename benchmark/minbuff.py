#! /usr/bin/env python

from subprocess import *
import sys
import os
def run(buf, n, nthread, incx):
    my_env = os.environ.copy()
    my_env['OPENBLAS_ZTRMV_BUF'] = str(buf)
    my_env['OPENBLAS_PARAM_N'] = str(n)
    my_env['OPENBLAS_NUM_THREADS'] = str(nthread)
    my_env['OPENBLAS_INCX'] = str(incx)
    return call(['./zsmallscaling'], stdout = PIPE, stderr=PIPE, env=my_env) == 0

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
            sys.stdout.flush()
