/*

Bubble Sort Simulation in C

*/
#include<stdio.h>
#include<time.h>
#include<stdlib.h>
void swap(int *x,int *y) {
    int temp;
    temp=*x;
    *x=*y;
    *y=temp;
}
void print_star(int n) {
    for(int i=0;i<n;i++) {
        printf("*");
    }
    printf(" %d",n);
    printf("\n");
}
void print(int arr[],int n) {
    for(int i=0;i<n;i++) {
        print_star(arr[i]);
    }
    printf("\n");
}
int main(int argc, char *args[]) {
    int n;
    double time_taken=0;
    srand(time(0));
    clock_t begin=clock();
    scanf("%d",&n);
    int *arr=(int *)malloc(n*sizeof(int));
    for(int i=0;i<n;i++) {
        arr[i]=rand()%100000;
    }
    print(arr,n);
    /*The Bubble Sort starts here --- */
    for(int i=0;i<n-1;i++) {
        for(int j=0;j<n-i-1;j++) {
            if(arr[j]>arr[j+1]) {
                swap(&arr[j],&arr[j+1]);
            }
        }
    }
    print(arr,n);
    free(arr);
    clock_t end=clock();
    time_taken=(double)(end-begin)/CLOCKS_PER_SEC;
    printf("The time taken by the algorithm is %.2f seconds",time_taken);
    return 0;
}