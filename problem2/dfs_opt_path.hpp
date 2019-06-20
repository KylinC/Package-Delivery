#ifndef _DFS_OPT_PATH_HPP_
#define _DFS_OPT_PATH_HPP_

#include "./Graph.hpp"
#include <bits/stdc++.h>

double
cost_val(vector<edge>& path);
double
time_val(double order_time, vector<edge>& path);
double
val(double order_time, vector<edge>& path);
double
val(edge& e);

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
    int depth_limit,
    set<int>& hubs,
    MultiDiGraph& out_ways);

vector<edge>
opt(MultiDiGraph& G,
    int dep_city,
    int arr_city,
    double order_time,
    int depth_limit,
    set<int>& hubs,
    MultiDiGraph& out_ways)
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
        depth_limit,
        hubs,
        out_ways);

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
val(double order_time, vector<edge>& path)
{
    double total_cost = 0;
    for (auto& e : path) {
        total_cost += e.cost;
    }
    double total_time = (path.empty()) ? 0 : path.back().arr_time - order_time;
    return total_cost * sqrt(total_time);
}
double
val(edge& e)
{
    return sqrt(e.arr_time - e.dep_time) * e.cost + (e.dep_time > 1440) ? 1 : 0;
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
    int depth_limit,
    set<int>& hubs,
    MultiDiGraph& out_ways)
{
    if (dep_city == arr_city) {
        // find OPT
        double VAL = val(order_time, path);
        if (VAL < MIN) {
            MIN = VAL;
            OPT = path;
        }
        return;
    }
    if (depth_limit == 0)
        return;

    vis[dep_city] = true;

    // if dep_city is hub
    if (hubs.find(dep_city) != hubs.end()) {
        for (auto& kv : out_ways[dep_city]) {
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
                        depth_limit - 1,
                        hubs,
                        out_ways);

                path.pop_back();
                vis[target_city] = false;
            }
        }
    }
    // if dep_city is not hub
    else {
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
                        depth_limit - 1,
                        hubs,
                        out_ways);

                path.pop_back();
                vis[target_city] = false;
            }
        }
    }
}

#endif