#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
  int i;
  int n = atoi(argv[1]);
  for(i = 1; i <= n; i++) {
    printf("%d\n", i);
  }
  return 0;
}
