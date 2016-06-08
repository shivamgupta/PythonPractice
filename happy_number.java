/**
* @author: Thao Bach
* @param n is a positive integer
* Returns true if a number is happy, which is defined by the following
* process: starting with any positive integer, replace the number by the sum of
the squares of its digits, and repeat the process until the number either equals 1
*(where it will stay), or it loops endlessly in a cycle which does not include 1.
*/
public boolean isHappy(int n) {
    HashSet<Integer> set = new HashSet<Integer>();

    while(!set.contains(n)){
        set.add(n);

        n = sum(getDigits(n));
        if (n == 1)
            return true;
    }

    return false;
}

/**
* @param arr is an integer array
* Returns the sum of the squares of the integers in the array
*/
public int sum(int[] arr){
    int sum = 0;
    for(int i: arr){
        sum = sum + i*i;
    }
    return sum;
}

/**
* @param n is an integer
* Returns an integer array of digits in n
*/
public int[] getDigits(int n){
    String s = String.valueOf(n);
    int[] result = new int[s.length()];
    int i=0;

    while(n>0){
        int m = n%10;
        result[i++] = m;
        n = n/10;
    }

    return result;
}
