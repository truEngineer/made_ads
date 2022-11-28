#include <iostream>
#include <map>

class Parser {
private:
    int cur;
    std::string s;
    std::map<char, int> toktype;

    int parse_num() {
        int ans = 0;
        bool correct = 0;
        while (s[cur] >= '0' and s[cur] <= '9') {
            ans = 10 * ans + (s[cur] - '0');
            cur++;
            correct = 1;
        }
        if (!correct) {
            wrong();
        }
        return ans;
    }
    
    int parse_xor() {
        int ans;
        if (s[cur] == '^') {
            if (s[cur + 1] != '(') {
                wrong();
            }
            cur += 2;
            ans = parse_sum();
            if (s[cur] != ')') {
                wrong();
            }
            cur++;
            if (ans > 0) {
                ans += 5;
            } else {
                ans *= -1;
            }
        } else if (s[cur] == '(') {
            cur++;
            ans = parse_sum();
            if (s[cur] != ')') {
                wrong();
            }
            cur++;
        } else {
            ans = parse_num();
        }
        return ans;
    }
    
    int parse_mult() {
        int ans = parse_xor();
        while (s[cur] == '*') {
            cur++;
            ans *= parse_xor();
        }
        return ans;
    }
    
    int parse_sum() {
        int ans = parse_mult();
        while (s[cur] == '+' or s[cur] == '-') {
            int k = (s[cur] == '+' ? 1 : -1);
            cur++;
            int ret = parse_mult();
            ans += k * ret;
        }
        return ans;
    }

    void wrong() {
        std::cout << "WRONG";
        std::exit(0);
    }

public:
    Parser(std::string in): cur(0), s(in) {
        for (char c = '0'; c <= '9'; ++c) {
            toktype[c] = 1;
        }
        toktype['+'] = 2;
        toktype['-'] = 2;
        toktype['*'] = 2;
        toktype['^'] = 3;
        toktype['('] = 3;
        toktype[')'] = 3;
        s.pop_back();
        std::string s1 = "DedMoroz";
        std::string s2 = "Moroz";
        std::string s3 = "Podarok";
        std::string s4 = "Snegurochka";
        for (int i = 0; i < s.size(); ++i) {
            if (s.substr(i, s1.size()) == s1) {
                s = s.substr(0, i) + "(2020+0)" + 
                    s.substr(i + s1.size(), s.size() - i - s1.size());
            }
        }
        for (int i = 0; i < s.size(); ++i) {
            if (s.substr(i, s2.size()) == s2) {
                s = s.substr(0, i) + "(0-30)" + 
                    s.substr(i + s2.size(), s.size() - i - s2.size());
            }
        }
        for (int i = 0; i < s.size(); ++i) {
            if (s.substr(i, s3.size()) == s3) {
                s = s.substr(0, i) + "^" + 
                    s.substr(i + s3.size(), s.size() - i - s3.size());
            }
        }
        for (int i = 0; i < s.size(); ++i) {
            if (s.substr(i, s4.size()) == s4) {
                s = s.substr(0, i) + "(0+10)" + 
                    s.substr(i + s4.size(), s.size() - i - s4.size());
            }
        }
    }

    void parse() {
        int ans = parse_sum();
        if (cur != s.size()) {
            wrong();
        } else {
            std::cout << ans;
        }
    }
};

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);

    std::string s, tmp;
    while (std::cin >> tmp) {
        s += tmp;
        if (s.back() == '.') {
            break;
        }
    }
    Parser p = Parser(s);
    p.parse();

    return 0;
}
