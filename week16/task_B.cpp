#include <iostream>
#include <cmath>
 
typedef long long ll;
 
int sgn(ll n) {
    return (n > 0) - (n < 0);
}
 
int RectanglesIntersects(ll x1, ll y1, ll x2, ll y2, ll x3, ll y3, ll x4, ll y4) {
    if (sgn(x3 - x2) * sgn(x4 - x1) > 0) return 0;
    if (sgn(y3 - y2) * sgn(y4 - y1) > 0) return 0;
    return 1;
}
 
int intersect(ll x1, ll y1, ll x2, ll y2, ll x3, ll y3, ll x4, ll y4) {
    ll ABx, ABy, ACx, ACy, ADx, ADy;
    ll CAx, CAy, CBx, CBy, CDx, CDy;
    ll ACxAB, ADxAB, CAxCD, CBxCD;
    if (!RectanglesIntersects(std::min(x1, x2), std::min(y1, y2), 
                              std::max(x1, x2), std::max(y1, y2), 
                              std::min(x3, x4), std::min(y3, y4), 
                              std::max(x3, x4), std::max(y3, y4))) return 0;
    ACx = x3 - x1; ACy = y3 - y1; 
    ABx = x2 - x1; ABy = y2 - y1;
    ADx = x4 - x1; ADy = y4 - y1;
    CAx = x1 - x3; CAy = y1 - y3; 
    CBx = x2 - x3; CBy = y2 - y3;
    CDx = x4 - x3; CDy = y4 - y3;
    ACxAB = ACx * ABy - ACy * ABx;
    ADxAB = ADx * ABy - ADy * ABx;
    CAxCD = CAx * CDy - CAy * CDx;
    CBxCD = CBx * CDy - CBy * CDx;
    if ((sgn(ACxAB) * sgn(ADxAB) > 0) || (sgn(CAxCD) * sgn(CBxCD) > 0)) return 0;
    
    return 1;
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    ll x1, y1, x2, y2, x3, y3, x4, y4;
    std::cin >> x1 >> y1 >> x2 >> y2;
    std::cin >> x3 >> y3 >> x4 >> y4;
    std::cout << (intersect(x1, y1, x2, y2, x3, y3, x4, y4) ? "YES" : "NO");
    
    return 0;
}
