package Java.Now;

public class RecursionJ {

    public static String reverseString(String input) {
        if (input.equals("")) {
            return "";
        }
        return (reverseString(input.substring(1)) + input.charAt(0));
    }

    public static boolean isPalindrome(String input) {
        if (input.length() == 0 || input.length() == 1) {
            return true;
        }
        // Do some work to reduce the problem;
        if (input.charAt(0) == input.charAt(input.length() - 1)) {
            return isPalindrome(input.substring(1, input.length() - 1));
        }
        return false;
    }

    public static String findBinary(int decimal, String result) {
        if (decimal == 0) {
            return result;
        }
        result += decimal % 2;
        return findBinary(decimal/2, result);
    }

    public static int BinarySearch(int[] A, int left, int right, int x) {
        if (left > right) {
            return -1;
        }
        int mid = (left + right) / 2 ;
        if (x == A[mid]) {
            return mid;
        }
        if (x < A[mid]) {
            return BinarySearch(A, left, mid - 1, x);
        } 
        return BinarySearch(A, mid + 1, right, x); //x > A[mid]
    }

    public static int BinarySearch(int[] A, int x) {
        return BinarySearch(A, 0, A.length - 1, x);
    }


    public static void merge(int[] data, int start, int mid, int end) {
        
    }
    public static void main(String[] args) {

        String S1 = "Ultay de beta";
        System.out.println(reverseString(S1));

        String S2 = "racecar";
        System.out.println(isPalindrome(S2));

        System.out.println(findBinary(233, ""));

        int[] A = new int[10];
        for (int i = 0; i < 10; i++) {
            A[i] = 10 * i;
        }
        System.out.println(BinarySearch(A, 30));

    }


}