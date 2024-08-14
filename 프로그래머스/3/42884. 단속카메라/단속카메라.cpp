#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> routes)
{
    // 진입 지점을 기준으로 내림차순 정렬
    sort(routes.begin(), routes.end(), [](const vector<int> &a, const vector<int> &b) {
        return a[0] > b[0];
    });

    int cnt = 1; // 첫 번째 카메라 설치
    int camera = routes[0][0]; // 첫 번째 카메라의 위치 (진입 지점 기준)

    for (size_t i = 1; i < routes.size(); ++i)
    {
        // 현재 차량의 진입 지점이 이전 차량의 진출 지점보다 뒤에 있으면 겹치지 않음
        if (routes[i][1] < camera)
        {
            cnt++;
            camera = routes[i][0]; // 새로운 카메라 위치 업데이트
        }
    }

    return cnt;
}