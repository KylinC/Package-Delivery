#ifndef _ANALYSIS_DFS_OPT_PATH_HPP_
#define _ANALYSIS_DFS_OPT_PATH_HPP_

#include "./Graph.hpp"
#include <bits/stdc++.h>

double
cost_val(vector<edge>& path);

double
time_val(double order_time, vector<edge>& path);

double
val(double order_time, vector<edge>& path, double exp = 1);

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
    double val_exp,
    int depth_limit);

vector<edge>
opt(MultiDiGraph& G,
    int dep_city,
    int arr_city,
    double order_time,
    double val_exp,
    int depth_limit)
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
        val_exp,
        depth_limit);

    return OPT;
}

// implement
double
cost_val(vector<edge>& path)
{
    double total_cost = 0;
    for (auto& e : path) {
        total_cost += e.cost;
    }
    return total_cost;
}
double
time_val(double order_time, vector<edge>& path)
{
    return (path.empty()) ? 0 : path.back().arr_time - order_time;
}

double
val(double order_time, vector<edge>& path, double exp)
{
    double total_cost = 0;
    for (auto& e : path) {
        total_cost += e.cost;
    }
    double total_time = (path.empty()) ? 0 : path.back().arr_time - order_time;
    return total_time * pow(total_cost, exp);
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
    double val_exp,
    int depth_limit)
{
    if (dep_city == arr_city) {
        // find OPT
        double VAL = val(order_time, path, val_exp);
        if (VAL < MIN) {
            MIN = VAL;
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
            if (val(order_time, path) < MIN)
                opt(G,
                    target_city,
                    arr_city,
                    order_time,
                    e.arr_time,
                    vis,
                    path,
                    MIN,
                    OPT,
                    val_exp,
                    depth_limit - 1);

            path.pop_back();
            vis[target_city] = false;
        }
    }
}

#endif