#ifndef _DFS_OPT_PATH_HPP_
#define _DFS_OPT_PATH_HPP_

#include "./Graph.hpp"
#include <bits/stdc++.h>

double
val(double order_time, vector<edge>& path);

void
opt(MultiDiGraph& G,
    int dep_city,
    int arr_city,
    double order_time,
    double arr_time,
    bool vis[],
    vector<edge>& path,
    double& MIN,
    vector<edge>& OPT,
    int depth_limit);

vector<edge>
opt(MultiDiGraph& G,
    int dep_city,
    int arr_city,
    double order_time,
    int depth_limit = 2)
{
    bool vis[657] = { 0 };
    vector<edge> path;
    double MIN = 999999999;
    vector<edge> OPT;

    opt(G,
        dep_city,
        arr_city,
        order_time,
        order_time,
        vis,
        path,
        MIN,
        OPT,
        depth_limit);

    return OPT;
}

// implement
double
val(double order_time, vector<edge>& path)
{
    double total_cost = 0;
    for (auto& e : path) {
        total_cost += e.cost;
    }
    double total_time = path.back().arr_time - order_time;
    return total_cost * sqrt(total_time);
}

void
opt(MultiDiGraph& G,
    int dep_city,
    int arr_city,
    double order_time,
    double arr_time,
    bool vis[],
    vector<edge>& path,
    double& MIN,
    vector<edge>& OPT,
    int depth_limit)
{
    if (dep_city == arr_city) {
        // find OPT
        if (val(order_time, path) < MIN) {
            MIN = val(order_time, path);
            OPT = path;
        }
        return;
    }
    if (depth_limit == 0)
        return;

    vis[dep_city] = true;
    for (auto& kv : G[dep_city]) {
        int target_city = kv.first;
        auto& e = kv.second;

        // dfs
        if (vis[target_city] == false && e.dep_time >= arr_time) {
            vis[target_city] = true;
            path.push_back(e);
            opt(G,
                target_city,
                arr_city,
                order_time,
                e.arr_time,
                vis,
                path,
                MIN,
                OPT,
                depth_limit - 1);
            path.pop_back();
            vis[target_city] = false;
        }
    }
}

#endif