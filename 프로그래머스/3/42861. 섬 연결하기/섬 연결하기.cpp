#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int find(int *parent, int node)
{
    if (parent[node] == node)
        return node;
    return parent[node] = find(parent, parent[node]);
}

int solution(int n, vector<vector<int>> costs)
{

    sort(costs.begin(), costs.end(), [](const vector<int> &a, const vector<int> &b)
         { return a[2] < b[2]; });

    int *parent = new int[n]();

    for (int j = 0; j < n; j++)
    {
        parent[j] = j;
    }

    int j = 0;
    int answer = 0;
    for (vector<int> i : costs)
    {
        int root1 = find(parent, i[0]);
        int root2 = find(parent, i[1]);

        if (root1 != root2)
        {
            parent[root2] = root1;
            answer += i[2];
        }
    }
    delete[] parent;
    return answer;
}