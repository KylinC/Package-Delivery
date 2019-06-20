/*
    Author:
        Ding Fangyu
    Date:
        2019.6.13
    Usage:
        g++ -std=c++17 all_simple_paths.cpp -o all_simple_paths
        ./all_simple_paths
*/

#include "./Graph.hpp"
#include "./dfs_opt_path.hpp"
#include <bits/stdc++.h>
using namespace std;

int
main()
{
    // read tools.csv and construct a multi-directed-graph
    MultiDiGraph G(656 + 1);

    ifstream csv("tools.csv");
    string row;

    getline(csv, row); // Header
    while (getline(csv, row)) {
        istringstream sin(row);
        string field;

        int dep_city, arr_city;
        double dep_time, arr_time, cost;
        int tools_type;
        getline(sin, field, ',');
        dep_city = atoi(field.c_str());
        getline(sin, field, ',');
        arr_city = atoi(field.c_str());
        getline(sin, field, ',');
        dep_time = atof(field.c_str());
        getline(sin, field, ',');
        arr_time = atof(field.c_str());
        getline(sin, field, ',');
        cost = atof(field.c_str());
        getline(sin, field, ',');
        tools_type = atoi(field.c_str());

        G.add_edge(
          dep_city,
          arr_city,
          edge(dep_city, arr_city, dep_time, arr_time, cost, tools_type));
    }
    csv.close();

    // read orders.csv
    csv = ifstream("orders.csv");

    // output
    double total_cost_val = 0;
    ofstream opt_size("opt_size.txt"), sol_cost("sol_cost.txt"),
      sol_time("sol_time.txt"), sol_info("sol_info.txt");

    getline(csv, row); // Header
    int cnt = 0;
    while (getline(csv, row)) {

        istringstream sin(row);
        string field;

        int seller_city, buyer_city;
        double order_time;
        int good_id, good_amount, emergency;
        getline(sin, field, ',');
        seller_city = atoi(field.c_str());
        getline(sin, field, ',');
        buyer_city = atoi(field.c_str());
        getline(sin, field, ',');
        order_time = atof(field.c_str());
        getline(sin, field, ',');
        good_id = atoi(field.c_str());
        getline(sin, field, ',');
        good_amount = atoi(field.c_str());
        getline(sin, field, ',');
        emergency = atoi(field.c_str());

        // deal with an order
        auto OPT = opt(G, seller_city, buyer_city, order_time, 6);

        opt_size << OPT.size() << endl;
        sol_cost << cost_val(OPT) << endl;
        sol_time << time_val(order_time, OPT) << endl;

        for (auto& e : OPT) {
            sol_info << e << ",\t";
        }
        sol_info << endl;
    }

    csv.close();

    opt_size.close();
    sol_cost.close();
    sol_time.close();
    sol_info.close();

    return 0;
}
