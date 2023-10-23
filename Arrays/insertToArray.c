#include<stdio.h>
int main()
{
    int a[] = {1,2,3,4,5,6};
    int element, index, number_of_elements; 
    printf("Enter the element and index you want to place the number at : ");
    scanf("%d %d", &element, &index);
    
    number_of_elements = sizeof(a)/sizeof(a[0]);
    
  for (int i=number_of_elements; i>index; i--)
    {
        a[i]=a[i-1];
    }
    a[index]=element;  
    
    for (int i=0; i<=(number_of_elements-1);i++)
    {
        printf("%d", a[i]);
    }
    
    return 0;
}
