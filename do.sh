#! /bin/sh
#export MAKE_NB_JOBS=8
#export DISTCC_HOSTS="@theoden/4 localhost/2"
#export DISTCC_HOSTS="192.168.0.20"
#export CC=distcc
#export FC=distcc
#export DEBUG=1
export COMMON_OPT="-g -O0 -funsafe-math-optimizations -ffast-math"
#export COMMON_OPT="-O3 -funsafe-math-optimizations -ffast-math -fstack-protector-strong"
#export COMMON_OPT="-O0 -g -funsafe-math-optimizations -ffast-math -fsanitize=address -fstack-protector-strong"
#export LDFLAGS="-fsanitize=address -fstack-protector-strong"
export ASAN_OPTIONS="detect_leaks=0:abort_on_error=1"
make
