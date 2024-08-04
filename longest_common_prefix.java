class Solution {
    public static String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) {
            return "";
        }

        // Iterate through the characters of the first string
        for (int i = 0; i < strs[0].length(); i++) {
            // Iterate through the rest of the strings
            for (int j = 1; j < strs.length; j++) {
                // If the index exceeds the length of the current string or the characters don't match
                // Return the substring from the beginning up to the current index
                if (i >= strs[j].length() || strs[j].charAt(i) != strs[0].charAt(i)) {
                    return strs[0].substring(0, i);
                }
            }
        }
        return strs[0];
    }
}
