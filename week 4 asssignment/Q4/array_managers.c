#include <stdlib.h>

int* init_array(int size) {
return (int*)calloc(size, sizeof(int));
}

void set_value(int* arr, int index, int value) {
arr[index] = value;
}

int get_value(int* arr, int index) {
return arr[index];
}

void free_array(int* arr) {
free(arr);
}