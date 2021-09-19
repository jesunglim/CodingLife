#include<stdio.h>
#include <limits.h>

int main()
{
	//unsigned long long int num = 1844674407370955161;
	
	unsigned long long int amount = 0;
	amount = 523;
	char str[18];
	
	if (amount < 100000000) // if less 1 satoshi
	{
		sprintf(str, "0.%07llu", amount);
	}
	else
	{
			sprintf(str, "%llu", amount);			
			for (int i=17; i == 10; i--) // insert .
			{
				str[i] = str[i-1];
			}
			str[10] = '.';

	}
	printf("amount :%s", str);
}
