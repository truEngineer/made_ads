#include <iostream>
#include <vector>
#include <map>

std::map<char, int> toktype;
std::vector<std::string> lex;
int cur = 0;

int parse_num(const std::string& s) {
    int ans = 0;
    while (s[cur] >= '0' and s[cur] <= '9') {
        ans = 10 * ans + (s[cur] - '0');
        cur++;
    }
    lex.push_back(std::to_string(ans));
    return ans;
}

int parse_sum(const std::string& s);

int parse_mult(const std::string& s) {
    int ans;
    if (s[cur] == '(') {
        lex.push_back(std::string(1, s[cur]));
        cur++;
        ans = parse_sum(s);
        lex.push_back(std::string(1, s[cur]));
        cur++;
    } else {
        ans = parse_num(s);
    }
    while (s[cur] == '*') {
        lex.push_back(std::string(1, s[cur]));
        cur++;
        int ret;
        if (s[cur] == '(') {
            lex.push_back(std::string(1, s[cur]));
            cur++;
            ret = parse_sum(s);
            lex.push_back(std::string(1, s[cur]));
            cur++;
        } else {
            ret = parse_num(s);
        }
        ans *= ret;
    }
    return ans;
}

int parse_sum(const std::string& s) {
    int ans = parse_mult(s);
    while (s[cur] == '+' or s[cur] == '-') {
        int k = (s[cur] == '+' ? 1 : -1);
        lex.push_back(std::string(1, s[cur]));
        cur++;
        int ret = parse_mult(s);
        ans += k * ret;
    }
    return ans;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);

    std::string s;
    std::cin >> s;
    s.pop_back();
    for (char c = '0'; c <= '9'; ++c) {
        toktype[c] = 1;
    }
    toktype['+'] = 2;
    toktype['-'] = 2;
    toktype['*'] = 2;
    toktype['('] = 3;
    toktype[')'] = 3;
    int ans = parse_sum(s);
    //std::cout << "res:" << ans << '\n';
    for (auto ch : lex) {
        std::cout << ch << '\n';
    }

    return 0;
}
