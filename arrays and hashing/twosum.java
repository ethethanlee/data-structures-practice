import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;


class Solution{
    public int[] twoSum(int[] numbers, int target) {
        int[] output = new int[2];
        Map<Integer, Integer> hasher = new HashMap<Integer, Integer>();
        for (int i = 0; i < numbers.length; i++) {
            if (hasher.containsKey(target - numbers[i])) {
                output[1] = i;
                output[0] = hasher.get(target - numbers[i]);
                return output;
            }
            hasher.put(numbers[i], i);
        }
        return output;
    }

    public static void main(String[] args){
        int[] numbers = new int[]{ 2,7,11,15 };
        int target = 9;
        int sol[] = new Solution().twoSum(numbers, target);
        System.out.println(Arrays.toString(sol));
    }
}