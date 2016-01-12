#! /usr/bin/env python

DTB_ENTRIES = 64

def read_data(file_name):
    db = {}
    with open(file_name) as f:
        while True:
            h = f.readline().split()
            if not h:
                break
            nthread = int(h[1])
            incx = int(h[3])
            values = []
            for i in xrange(1,1024):
                values.append(int(f.readline().split()[1]))
            db[(nthread, incx)] = [values, None]
    return db

def test_data(db):
    for k, v in db.viewitems():
        nthread, incx = k
        values, formula = v
        print "nthread=", nthread, "incx=", incx
        if formula:
            for i in xrange(1, 17 if nthread > 1 else 1024):
                fv = (formula(i) + 3) & ~3
                print i, values[i-1], fv, fv - values[i-1]

zdb = read_data('ztrmv_min_buff.log')
cdb = read_data('ctrmv_min_buff.log')

# multi threaded up to n=16 only
cdb[(1, 1)][1] = lambda n: ((n - 1) / DTB_ENTRIES) * DTB_ENTRIES * 2 + 4
cdb[(1, 2)][1] = lambda n: ((n - 1) / DTB_ENTRIES) * DTB_ENTRIES * 2 + 4 + 2 * n
zdb[(1, 1)][1] = lambda n: ((n - 1) / DTB_ENTRIES) * DTB_ENTRIES * 2 - 6
zdb[(1, 2)][1] = lambda n: ((n - 1) / DTB_ENTRIES) * DTB_ENTRIES * 2 - 6 + 2 * n

cdb[(2, 1)][1] = lambda n:  n + 1
cdb[(3, 1)][1] = lambda n:  n + 1
cdb[(4, 1)][1] = lambda n:  n + 1

cdb[(2, 2)][1] = lambda n:  (n - 4) * 4 + 40
cdb[(3, 2)][1] = lambda n:  (n - 4) * 4 + 40
cdb[(4, 2)][1] = lambda n:  (n - 4) * 4 + 40

zdb[(2, 1)][1] = lambda n:  (n - 3) * 2
zdb[(3, 1)][1] = lambda n:  (n - 3) * 2
zdb[(4, 1)][1] = lambda n:  (n - 3) * 2

zdb[(2, 2)][1] = lambda n:  (n - 2) * 4 + 40
zdb[(3, 2)][1] = lambda n:  (n - 2) * 4 + 40
zdb[(4, 2)][1] = lambda n:  (n - 2) * 4 + 40

print "ctrmv"
test_data(cdb)
print "ztrmv"
test_data(zdb)
