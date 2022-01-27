# include<stdio.h>
# include<conio.h>
# include<stdbool.h>

//int main(){
//printf("1==1:%d\n",1==1);
//printf("1>=1:%d\n",1>=1);
//printf("1<=2:%d\n",1<=2);	
//	
//	return 0;
//}

//int main(){
//printf("1==1 && 2==2 :%d\n",1==1 && 2==2);
//printf("1==1 && 2!=2 :%d\n",1==1 && 2!=2);
//printf("1==1 || 2==2 :%d\n",1==1 || 2==2);
//printf("1!=1 || 2!=2 :%d\n",1!=1 || 2!=2);
//
//    return 0;
//}

//int main(){
//printf("int:%d\n",sizeof(1));	
//printf("int:%d\n",sizeof(float));	
//printf("int:%d\n",sizeof(int));	
//printf("int:%d\n",sizeof(double));		
//printf("int:%d\n",sizeof(char)); // it will give you bytes value
//printf("operator precedence:%d\n", 0 + 1 - 0 * 3 + 4 / 2);	// bodmas rule is applied here	
//	
//	return 0;
//}

//double getAge(){ //get age func is introduced
//	double age = 0; //initialized double age as 0
//	scanf("%lf",&age); //it will get you the age address entered by user
//	return age; //as it is a function it will have to return soecific data which is age here
//}
//int main(){
//	double age = getAge(); //declared var double age to getAge funcion
//	printf("age is :%lf",age); //printing age
//	return 0;
//}

//int multiply(int x, int y){ //multiply function is introduced with 2 parameters int x and int y
//	return x*y; //it will multiply those int value
//}
//int main(){
//	int x = 2;
//	int y = 2;
//	int product = multiply(x,y);
//	printf("%d\n\n",product);
//	return 0;
//}

//int main(){
//	int n = 0;
//	int sum = 0; // it is necessary to initialize these two vars n and sum at fisrt
//	
//	do{ //do while loop is used
//    printf("num:"); //asks user to enter num
//    scanf("%d",&n);
//    sum += n; //sum will increment in accordance to n
//    printf("sum :%d\n",sum);  
//    }
//    while (sum <= 100); //until the sum entered by user reaches to 100 it will keep user asking to enter
//    printf("done"); //once it reaches 100, it will print statment and loop will be over
//    return 0;
//}

//int main(){
//	int n = 0;
//	int sum = 0; // it is necessary to initialize these two vars n and sum at fisrt
//	
//	for (;sum <= 100;){ #for loop is used instead of do while lop
//		scanf("%d",&n);
//		sum +=n;
//		printf("sum :%d\n",sum);
//	}
//	printf("done"); //once it reaches 100, it will print statment and loop will be over
//    return 0;
//}

//int main(){
//	printf("full name:");
//	char name[20] = {};
//	scanf("%s",name);
//	gets(name);
//	printf("hi %s",name);
////	puts(name);
//	
//	return 0;
//}

//int main(){
//	int First_array[10] = {1,2,3,4,5,6,7,8,9,10};
//	int *ptr;
//	ptr = First_array;
//    for (int i=0; i<5; i++){
//	printf("value of *ptr var is %d\n", *ptr);
//	printf("value of *ptr var is %d\n", ptr);
//	ptr++;
//	}
//	return 0;
//}
