class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> rMap = new HashMap<>();
        rMap.put('I', 1);
        rMap.put('V', 5);
        rMap.put('X', 10);
        rMap.put('L', 50);
        rMap.put('C', 100);
        rMap.put('D', 500);
        rMap.put('M', 1000);

        int result = 0;
        int sLen = s.length() - 1;
        for (int i = 0; i < sLen; i++) {
            if (rMap.get(s.charAt(i)) >= rMap.get(s.charAt(i + 1))) {
                result += rMap.get(s.charAt(i));
            } else {
                result -= rMap.get(s.charAt(i));
            }
        }
        result += rMap.get(s.charAt(sLen));

        return result;
    }
}
