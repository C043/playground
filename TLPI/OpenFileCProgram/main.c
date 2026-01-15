#include <fcntl.h>
#include <stdio.h>

int main(void) {
  int fd = open("./test.txt", O_RDONLY);
  if (fd == -1) {
    printf("There was an error trying to open test.txt\n");
  } else {
    printf("The file test.txt was opened correctly!\n");
    printf("status code: %d\n", fd);
  }
}
