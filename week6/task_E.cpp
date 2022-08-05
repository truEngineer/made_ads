#include <iostream>
#include <vector>
 
 
const int INF = int(1e6);
const int COUPON_PRICE = 100;
 
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    int n;
    std::cin >> n;
    if (n == 0) {
        std::cout << 0 << std::endl << 0 << " " << 0;
        return 0;
    }
    int price[n];
    int prev[n][n + 2];
    int money[n][n + 2];
    for (int i = 0; i < n; ++i) {
        std::cin >> price[i];
        money[i][0] = INF;
    }
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n + 2; ++j) {
            money[i][j] = INF;
        }
    }
    if (price[0] > COUPON_PRICE) {
        money[0][2] = price[0];
    } else {
        money[0][1] = price[0];
    }
 
    for (int i = 1; i < n; ++i) {
        for (int j = 1; j < i + 2; ++j) {
            if (price[i] > COUPON_PRICE) {
                if (j == i + 1) {
                    money[i][j + 1] = money[i - 1][j] + price[i];
                    prev[i][j + 1] = j;
                }
                if (money[i - 1][j - 1] + price[i] <= money[i - 1][j + 1]) {
                    money[i][j] = money[i - 1][j - 1] + price[i];
                    prev[i][j] = j - 1;
                } else {
                    money[i][j] = money[i - 1][j + 1];
                    prev[i][j] = j + 1;
                }
            } else {
                if (money[i - 1][j] + price[i] <= money[i - 1][j + 1]) {
                    money[i][j] = money[i - 1][j] + price[i];
                    prev[i][j] = j;
                } else {
                    money[i][j] = money[i - 1][j + 1];
                    prev[i][j] = j + 1;
                }
            }
        }
    }
 
    int answer = money[n - 1][1];
    int last_pos = 1;
    for (int i = 1; i < n + 2; ++i) {
        if (money[n - 1][i] <= answer) {
            answer = money[n - 1][i];
            last_pos = i;
        }
    }
    std::vector<int> result;
    int used = 0;
    int cur_last_pos = last_pos;
    int ind = n - 1;
    while (ind > 0) {
        if (prev[ind][cur_last_pos] > cur_last_pos) {
            used += 1;
            result.push_back(ind + 1);
        }
        cur_last_pos = prev[ind][cur_last_pos];
        ind -= 1;
    }
    last_pos -= 1;
    std::cout << answer << std::endl;
    std::cout << last_pos << " " << used << std::endl;
    for (int i = result.size() - 1; i >= 0; --i) {
        std::cout << result[i] << std::endl;
    }
 
    return 0;
}
