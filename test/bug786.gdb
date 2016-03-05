!rm -f *.SUMM
break ztrmv.c:265 if (n == 63) && (incx == 2)
run  < ./zblat2.dat
watch &stack_check
