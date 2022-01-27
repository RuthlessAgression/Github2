// public class DayThree {
//     public static void main(String[] args) {
//         int x = 0; // x and y are supposed to be score
//         int y = 0;
//
//         for (int i=1  ; i <= 6 ; i++) {
//             double b = 1 + 6*Math.random(); // random double no. is created which is multiplied by 6 then added to 1
//             int a = (int) b; // int a has now double b as int a
//             System.out.println(a); // it will print that random double b converted as int a
//           
//             if (a%2 == 0) { // if that random int a leaves no remainder when divided by 2 or is even
//                 x++; // then increment value of score x
//             } else { // if above if condition fails
//                 y++; // then increment score y
//             }
//         }
//     System.out.println("your points: " + x); // it will print score x
//     System.out.println("computer point: " + y); // it will print score y
//
//     if (x > y) { // if score x is more than score y
//         System.out.println(" you win"); // then print you win
//     } else { // if above if condition fails
//         System.out.println("computer win"); // then print computer win
//         }
//     }
// }