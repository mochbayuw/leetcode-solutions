class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function lengthOfLongestSubstring($s) {
        $set = [];
        $left = 0;
        $maxLength = 0;
        
        for ($right = 0; $right < strlen($s); $right++) {
            $char = $s[$right];
            
            // Jika karakter ada dalam set, geser left sampai karakter itu hilang
            while (isset($set[$char])) {
                unset($set[$s[$left]]);
                $left++;
            }
            
            // Meambahkan karakter baru ke dalam set
            $set[$char] = true;
            
            // Mengitung panjang window
            $maxLength = max($maxLength, $right - $left + 1);
        }
        
        return $maxLength;
    }
}
