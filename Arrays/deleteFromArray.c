#include<stdio.h>

int main()
{
    int arr[] = {1,2,3,4,5};
    int n=5;
    int ele,index;
    for (int i=0; i<5; i++)
    {
        printf("%d ",arr[i]);

    }
    printf("\nEnter the number you want to delete :");
    scanf("%d",&ele);
    
    for (int i=0; i<5; i++)
    {
        if (arr[i] == ele)
        {
            index = i;
            break;
        }
    }
    
    for(int j=index; j<n; j++)
    {
        arr[j] = arr[j+1];
    }
    n--;
    
    for (int k=0; k<n; k++)
    {
        printf("%d ",arr[k]);

    }
}