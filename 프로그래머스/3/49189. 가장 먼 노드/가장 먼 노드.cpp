#include <string>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

void dfs(int index, vector<vector<int>> &node, vector<int> &visit_and_cnt, int count)
{
    if (visit_and_cnt[index] <= count)
    {
        return;
    }

    visit_and_cnt[index] = count;

    for (int i : node[index])
    {
        dfs(i, node, visit_and_cnt, count + 1);
    }
}

int solution(int n, vector<vector<int>> edge)
{
    vector<vector<int>> node(n + 1);

    for (const auto& e : edge)
    {
        node[e[0]].push_back(e[1]);
        node[e[1]].push_back(e[0]);
    }

    vector<int> visit_and_cnt(n + 1, numeric_limits<int>::max());

    dfs(1, node, visit_and_cnt, 0);

    int max_value = *max_element(visit_and_cnt.begin() + 1, visit_and_cnt.end());
    int answer = count(visit_and_cnt.begin() + 1, visit_and_cnt.end(), max_value);

    return answer;
}