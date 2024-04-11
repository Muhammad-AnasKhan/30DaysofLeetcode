// #include <vector>
// #include <string>

// class Solution {
// public:
//     // Generates all combinations of letters by mapping the digits to corresponding letters on a phone keypad
//     std::vector<std::string> letterCombinations(std::string digits) {
//         // If the input string is empty, return an empty vector
//         if (digits.empty()) return {};
      
//         // Create a mapping for the digits to their corresponding letters
//         std::vector<std::string> digitToChars = {
//             "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
//         };
      
//         // Initialize the answer vector with an empty string to start the combinations
//         std::vector<std::string> combinations = {""};
      
//         // Loop through each digit in the input string
//         for (char digit : digits) {
//             // Get the string that corresponds to the current digit
//             std::string chars = digitToChars[digit - '2'];
          
//             // Temporary vector to store the new combinations
//             std::vector<std::string> tempCombinations;
          
//             // Loop through each combination we have so far
//             for (std::string &combination : combinations) {
//                 // Append each character that corresponds to the current digit
//                 for (char ch : chars) {
//                     tempCombinations.push_back(combination + ch);
//                 }
//             }
//             // Replace the combinations with the updated ones
//             combinations = std::move(tempCombinations);
//         }
//         // Return the vector containing all combinations
//         return combinations;
//     }
// };

class Solution {
public:
    void generateCombos(int idx, string& digits, string& temp, vector<string>& sol, vector<string>& charMap){
        if(idx==digits.length()){
            if(temp.length()) sol.push_back(temp);
            return;
        }

        int num=digits[idx]-'0';
        string str=charMap[num];

        for(int i=0;i<str.length();i++){
            temp.push_back(str[i]);
            generateCombos(idx+1, digits, temp, sol, charMap);
            temp.pop_back();
        }
    }

    vector<string> letterCombinations(string digits) {
        string temp;
        vector<string> sol;
        vector<string> charMap={"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

        generateCombos(0, digits, temp, sol, charMap);
        return sol;
    }
};