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
    clock_t start = clock();

    MultiDiGraph G(656 + 1);

    ifstream csv("tools.csv");
    string row;

    getline(csv, row); // Header
    while (getline(csv, row)) {
        istringstream sin(row);
        string field;

        int dep_city, arr_city;
        double dep_time, arr_time, cost;
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

        G.add_edge(dep_city,
                   arr_city,
                   edge(dep_city, arr_city, dep_time, arr_time, cost));
    }
    csv.close();
    cout << "Execution time of reading tools.csv & constructing a "
            "multi-directed-graph: "
         << (double)(clock() - start) / CLOCKS_PER_SEC << "s" << endl;

    // read orders.csv
    start = clock();

    csv = ifstream("orders.csv");

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

        auto OPT = opt(G, seller_city, buyer_city, order_time, 2);
        cnt++;

        if (cnt % 300 == 0) {
            cout << "order: " << row << endl;
            cout << "solution: ";
            for (auto& e : OPT) {
                cout << e << ", ";
            }
            cout << endl;
            cout << "val: " << val(order_time, OPT) << endl;
            cout << "time: " << cnt << ", "
                 << (double)(clock() - start) / CLOCKS_PER_SEC << "s" << endl
                 << endl;
            // break;
        }
    }

    csv.close();

    cout << (double)(clock() - start) / CLOCKS_PER_SEC << "s" << endl;

    return 0;
}