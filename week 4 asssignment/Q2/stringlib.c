#include <string.h>
#include <stdlib.h>

char* reverse_string(const char* input) {
int len = strlen(input);
char* result = (char*)malloc(len + 1);

for (int i = 0; i < len; i++) {
result[i] = input[len - i - 1];
}
result[len] = '\0';
return result;
}