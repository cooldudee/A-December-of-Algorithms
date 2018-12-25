#include<stdio.h>

void main()

{
    int i,a[10],search,n,f,l,mid;
    printf("Enter the number of elements:\n");
    scanf("%d",&n);
    printf("Enter the elements:\n");
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    printf("Enter the search element:\n");
    scanf("%d",&search);
    f=0;
    l=n-1;
    while(f<=l)
    {
        mid=(f+l)/2;
        if(a[mid]>search)
        {
            l=mid-1;
        }
        else if(a[mid]<search)
        {
            f=mid+1;
        }
        else
        {
            printf("The search element is found at location %d",mid+1);
            break;
        }
    }
    if(f>l)
    {
        printf("The search element is not present in the array");
    }
    printf("\n");
    
}
