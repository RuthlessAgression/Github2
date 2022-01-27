// import java.util.Scanner;
// public class Cwh {
    // static int sum(int a, int b){
    //     return a+b;
    // }
    // public static void main(String[] args) {
    // String name = "AR RA";
    // String place = "CodeWithAR10";
    // System.out.println(name);
    // System.out.println(name.length()); // it will print 4 as lengtgh of str " AR 10 "
    // System.out.println(name.toUpperCase()); // str name is already in upper case so it will print name as it is
    // System.out.println(name.toLowerCase()); // it will print AR10 to lowercase as ar10
    // System.out.println(name + " from " + place);
    // System.out.println(name + " from\\ " + place);
    // System.out.println(name + " from\t " + place); it will add tab before place
    // System.out.println(name + " from\n " + place); // it will print place in new line

    // System.out.println(name.contains("Aas")); // return true /false accordingly
    // System.out.println(name.charAt(1)); // prints the char at ondex 2 which is 'R'
    // System.out.println(name.endsWith("10")); // returns true/false accordingly
    // System.out.println(name.indexOf("win")); // gives random int like -1 unlike booleans true/false if 'win' is not in name

    // int numb1 = 4, numb2 = 7;
    // System.out.println(Math.max(numb1, numb2)); // gives 7 as max value
    // System.out.println(Math.min(numb1, numb2)); // gives 4 as min value
    // System.out.println(Math.sqrt(36)); // gives 6 as square root of 36
    // System.out.println(Math.abs(-36)); // gives absolute value as 36
    // System.out.println(Math.random()); // it will always give value betn o and 1
    // System.out.println(4+(8-4)*Math.random()); // it will give value between range 4 to 8


    // int a = 45, x=56, y=67;
    // float b = 45.22f;
    // boolean isAdult = false;
    // System.out.println(y);
    // System.out.println(b);
    // System.out.println(isAdult);

// Operators in Java
//     Operand, operator, Operand  =  Result
//     4           +           7   =  11
    // int num1 = 45, num2=78;
    // num1 += 3; // num 1 = num 1 + 3 : 48
    // num2 -= 8; // num 2 = num 2 - 8 :70
    // System.out.print("The value of num1 + num2 is ");
    // System.out.println(num1 + num2); // 48 + 70

    // System.out.print("The value of num1 - num2 is ");
    // System.out.println(num1 - num2); // 48 - 70

    // System.out.print("The value of num1 * num2 is ");
    // System.out.println(num1 * num2);n // 48 *70

    // System.out.print("The value of num1 / num2 is ");
    // System.out.println(num1 / num2); // 48 / 70

    // System.out.print("The value of num1 % num2 is ");
    // System.out.println(num1 % num2); // remainder when num2 divided by num 1
    // System.out.println(num2++); // num 1 is incremented by 1 : 49
    // System.out.println(++num1); // num1++ = ++num1
    // System.out.println(num2--); // num 2 decrement by 1
    // System.out.println(--num2); // num2-- = --num2

    // int j = 0;
    // do{
    //     System.out.println(j);
    //     j += 1;
    // }while(j>100);

//
    // for(int i=0;i<=10;i++){
    //     if(i==2){
    //         continue; // it will skip 2 and continues to 10
    //     } else{
    //         System.out.println(i); // if i dont equals to 2 it will print from o to 10
    //     }
    // }

    // Java Arrays
    // int [] marks = {1,2,3,5}; // array [] named marks is created
    //    marks[3] = 34; // this will update marks on index[3]
    // System.out.println(marks[0]); // prints value on index[0] whcih is 1 in given array
    // System.out.println(marks[3]); // gives value on index[3] which is 34(updated from 5 to 34 in line 214)

    //    // Classical way to iterate an array
    // for(int i=0;i<marks.length;i++){ // comparision to length of marks array which of length 4 or has 4 values in it
    //     System.out.println(marks[i]); // prints all i until the lenth of that array or to the last element
    // }
    //    // For each loop is another type of loop used for iteration in arrays
    // for(int value:marks){ // value var will contain all elements of marks array
    //     System.out.println(value); // it will print var valuw which contains array named marks
    // }

    // int [][] matrix = {{1,2,3}, // 2 [][] as it is 2D array
    //                     {4,5,6}};
    // System.out.println(matrix[0][1]); // [0][1] :2nd item[1] of 1st array [0]
    
    
    
    // String [] cars = {"Maruti Harry", "Maruti", "Suzuki", "Innova", "Ford Titanium"};
    // for(String allCars:cars){
    //     System.out.println(allCars);
    // }

        // Try - Catch
    // String [] cars = {"Maruti Harry", "Maruti", "Suzuki", "Innova", "Ford Titanium"};

    // try{
    //     System.out.println(cars[3]);
    // }
    // catch(Exception e){
    //     System.out.println(e);
    // }

    // System.out.println("Masoom");




        // float number_1, number_2;
        // System.out.println("Enter first number");
        // Scanner scan = new Scanner(System.in);
        // number_1 = scan.nextFloat();

        // System.out.println("Enter second number");
        // // Scanner scan = new Scanner(System.in); // one scanner is enough for another reference
        // number_2 = scan.nextFloat();
        
        // System.out.print("You have Entered ");
        // System.out.print(number_1);
        // System.out.print(" and ");
        // System.out.println(number_2); // print ln prints in a different line print() prints together
        // String prompt = "Enter 0 for addition, 1 for " +
        //                 "subtraction, 2 for multiplication and 3 for division";
        // System.out.println(prompt); // it will print above prompt to user
        // int input = scan.nextInt(); //holds  integer input
        // switch (input){ // input is switched to cases where,
        //     case 0: // case o adds the nums
        //         System.out.println("Adding these numbers");
        //         System.out.print("The result is: ");
        //         System.out.println(number_1 + number_2); // it will print by adding num 1 and num 2
        //         break; // it will break other following cases if 1 is entered by user

        //     case 1: // case 1 will subtract num  and num1
        //         System.out.println("Subtracting these numbers"); 
        //         System.out.print("The result is: ");
        //         System.out.println(number_1 - number_2); // prints the subtracted value
        //         break;

        //     case 2: // case 2 will multiply num 1 and num
        //         System.out.println("Multiplying these numbers");
        //         System.out.print("The result is: ");
        //         System.out.println(number_1 * number_2); // prints the multiplied value
        //         break;

        //     case 3:
        //         System.out.println("Dividing these numbers");
        //         System.out.print("The result is: ");
        //         System.out.println(number_1 / number_2);
        //         break;

        //     default: // it is executed if none of the cases are used
        //         System.out.println("Invalid input");

        // }
    // }
// }