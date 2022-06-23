#include <complex.h>
#include <stdio.h>

#define __STDC_WANT_LIB_EXT1__ 1

int main() {
    #ifdef __STDC_NO_COMPLEX__
        printf("COMPLEX NOT SUPPORTED\n");
        exit(1);
    #else
        printf("GOOD");

        double complex cx = 1.0 + 3.0*I;
        double complex cy = 1.0 - 4.0*I;

        printf("Starting values: cx = %.2f%+.2fi  cy = %.2f%+.2fi\n", creal(cx), cimag(cx), creal(cy), cimag(cy));
    #endif
}