#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
double reciprocal (int i)
{
   // I should be non-zero.
   assert (i != 0);
   return 1.0/i;
}
int main (int argc, char **argv)
{
   int i;
   i = atoi (argv[1]);
   printf("The reciprocal of %d is %g\n", i, reciprocal (i));
   return 0;
}