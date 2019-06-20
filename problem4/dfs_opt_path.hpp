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

void
opt(set<int> big_cities,
    MultiDiGraph& G_only_big,
    MultiDiGraph& G_others,
    int dep_city,
    int arr_city,
    double order_time,
    double arr_time,
    bool vis[],
    vector<edge>& path,
    double& MIN,
    vector<edge>& OPT,
    int depth_limit_search_for_big,
    int depth_limit_among_big,
    int depth_limit_leave_from_big);

vector<edge>
opt(set<int> big_cities,
    MultiDiGraph& G_only_big,
    MultiDiGraph& G_others,
    int dep_city,
    int arr_city,
    double order_time,
    int depth_limit_search_for_big,
    int depth_limit_among_big,
    int depth_limit_leave_from_big)
{
    bool vis[657] = { 0 };
    vector<edge> path;
    double MIN = 999999999;
    vector<edge> OPT;

    opt(big_cities,
        G_only_big,
        G_others,
        dep_city,
        arr_city,
        order_time,
        order_time,
        vis,
        path,
        MIN,
        OPT,
        depth_limit_search_for_big,
        depth_limit_among_big,
        depth_limit_leave_from_big);

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

void
opt(set<int> big_cities,
    MultiDiGraph& G_only_big,
    MultiDiGraph& G_others,
    int dep_city,
    int arr_city,
    double order_time,
    double arr_time,
    bool vis[],
    vector<edge>& path,
    double& MIN,
    vector<edge>& OPT,
    int depth_limit_search_for_big,
    int depth_limit_among_big,
    int depth_limit_leave_from_big)
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
    

    // has not been in big cities
    if (big_cities.find(dep_city) == big_cities.end()) {
        // go to a big city
        if (depth_limit_search_for_big != 0) {
            vis[dep_city] = true;
            for (auto& kv : G_others[dep_city]) {
                int target_city = kv.first;
                auto& e = kv.second;

                if (vis[target_city] == false && e.dep_time >= arr_time) {
                    vis[target_city] = true;
                    path.push_back(e);
                    if (val(order_time, path) < MIN)
                        opt(big_cities,
                            G_only_big,
                            G_others,
                            target_city,
                            arr_city,
                            order_time,
                            e.arr_time,
                            vis,
                            path,
                            MIN,
                            OPT,
                            depth_limit_search_for_big - 1,
                            depth_limit_among_big,
                            depth_limit_leave_from_big);

                    path.pop_back();
                    vis[target_city] = false;
                }
            }
        }
    }
    // has been in big cities
    else {

        if (depth_limit_among_big != 0) {
            // go to another big city
            vis[dep_city] = true;
            for (auto& kv : G_only_big[dep_city]) {
                int target_city = kv.first;
                auto& e = kv.second;

                if (vis[target_city] == false && e.dep_time >= arr_time) {
                    vis[target_city] = true;
                    path.push_back(e);
                    if (val(order_time, path) < MIN) {
                        opt(big_cities,
                            G_only_big,
                            G_others,
                            target_city,
                            arr_city,
                            order_time,
                            e.arr_time,
                            vis,
                            path,
                            MIN,
                            OPT,
                            0,
                            depth_limit_among_big - 1,
                            depth_limit_leave_from_big);
                    }

                    path.pop_back();
                    vis[target_city] = false;
                }
            }
        }

        if (depth_limit_leave_from_big != 0) {
            // directly go to the destination
            for (auto& kv : G_others[dep_city]) {
                int target_city = kv.first;
                auto& e = kv.second;

                if (vis[target_city] == false && e.dep_time >= arr_time) {
                    vis[target_city] = true;
                    path.push_back(e);
                    if (val(order_time, path) < MIN)
                        opt(big_cities,
                            G_only_big,
                            G_others,
                            target_city,
                            arr_city,
                            order_time,
                            e.arr_time,
                            vis,
                            path,
                            MIN,
                            OPT,
                            0,
                            0,
                            depth_limit_leave_from_big - 1);

                    path.pop_back();
                    vis[target_city] = false;
                }
            }
        }
    }
}

#endif