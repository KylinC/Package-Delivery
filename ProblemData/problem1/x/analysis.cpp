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
#include "./analysis_dfs_opt_path.hpp"
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

        G.add_edge(dep_city,
                   arr_city,
                   edge(dep_city, arr_city, dep_time, arr_time, cost, tools_type));
    }
    csv.close();

    // output
    ofstream opt_size, sol_cost, sol_time, sol_info, exe_time;

    vector<double> exps;
    for (int i = 0; i < 100; i++)
        exps.push_back(i / 10.0);

    for (int i = 0; i < exps.size(); i++) {

        // read orders.csv
        csv = ifstream("orders.csv");
        getline(csv, row); // Header

        cout << i << endl;

        const int buffer_size = 30;
        char opt_size_name[buffer_size], sol_cost_name[buffer_size],
          sol_time_name[buffer_size], sol_info_name[buffer_size],
          exe_time_name[buffer_size];

        sprintf(opt_size_name, "./data/opt_size_%d.txt", (i + 1));
        sprintf(sol_cost_name, "./data/sol_cost_%d.txt", (i + 1));
        sprintf(sol_time_name, "./data/sol_time_%d.txt", (i + 1));
        sprintf(sol_info_name, "./data/sol_info_%d.txt", (i + 1));
        sprintf(exe_time_name, "./data/exe_time_%d.txt", (i + 1));

        opt_size.open(opt_size_name);
        sol_cost.open(sol_cost_name);
        sol_time.open(sol_time_name);
        sol_info.open(sol_info_name);
        exe_time.open(exe_time_name);

        int cnt = 0;
        auto start = clock();
        int opt_sz_cnter[5] = { 0 };
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
            auto OPT = opt(G, seller_city, buyer_city, order_time, exps[i], 4);

            opt_sz_cnter[OPT.size()]++;
            sol_cost << cost_val(OPT) << endl;
            sol_time << time_val(order_time, OPT) << endl;

            for (auto& e : OPT) {
                sol_info << e << ", ";
            }
            sol_info << endl;

            cnt++;
            if (cnt == 100)
                break;
        }

        for (int i = 0; i < 5; i++) {
            opt_size << opt_sz_cnter[i] << endl;
        }
        exe_time << ((double)(clock() - start) / CLOCKS_PER_SEC) << endl;

        opt_size.close();
        sol_cost.close();
        sol_time.close();
        sol_info.close();
        exe_time.close();

        csv.close();
    }

    return 0;
}