#include <unordered_set>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        std::array<int, 256> char_index_map;
        std::fill(char_index_map.begin(), char_index_map.end(), -1);
        
        int result = 0;
        int start  = 0;
        
        for(int i = 0; i < s.size(); i++)
        {
            const char& c = s[i];
            
            int idx = char_index_map[c];

            int collision = idx >= start;
			int length = i - start;
			
            int swap = collision * ((i - start) > result);
        
            result = swap * (i - start) + (1 - swap) * result;          
            
            start = collision * (idx + 1) + (1 - collision) * start;
            
            char_index_map[c] = i;
        }
        
        return std::max(result, static_cast<int>(s.size()) - start);
    }
};