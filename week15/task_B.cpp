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
    
    int parse_mult() {
        int ans;
        if (s[cur] == '(') {
            cur++;
            ans = parse_sum();
            cur++;
        } else {
            ans = parse_num();
        }
        while (s[cur] == '*') {
            cur++;
            int ret;
            if (s[cur] == '(') {
                cur++;
                ret = parse_sum();
                cur++;
            } else {
                ret = parse_num();
            }
            ans *= ret;
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
    Parser(std::string s): cur(0), s(s) {
        for (char c = '0'; c <= '9'; ++c) {
            toktype[c] = 1;
        }
        toktype['+'] = 2;
        toktype['-'] = 2;
        toktype['*'] = 2;
        toktype['('] = 3;
        toktype[')'] = 3;
    }

    void parse() {
        int ans = parse_sum();
        if (cur != s.size() - 1) {
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

    std::string s;
    std::cin >> s;
    Parser p = Parser(s);
    p.parse();

    return 0;
}
