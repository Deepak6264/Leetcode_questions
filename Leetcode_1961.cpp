class Solution {
public:
    bool isPrefixString(string s, vector<string>& words) {
        string k = "";
        for(string a : words){
            if(k == s){
                return true;
            }
k += a;
        }
        return k == s;
        
    }
};
