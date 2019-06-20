
#include "./Graph.hpp"
#include "./dfs_opt_path.hpp"
#include <bits/stdc++.h>
using namespace std;

set<int>
get_big_cities(ifstream& plane_csv);

void
construct_graphs(set<int> big_cities,
                 ifstream& tools_csv,
                 MultiDiGraph& G_only_big,
                 MultiDiGraph& G_others);

int
main()
{
    // get big cities
    ifstream plane_csv("plane.csv");
    set<int> big_cities = get_big_cities(plane_csv);
    plane_csv.close();

    // 2 graphs
    ifstream tools_csv("tools.csv");
    MultiDiGraph G_only_big(656 + 1);
    MultiDiGraph G_others(656 + 1);
    construct_graphs(big_cities, tools_csv, G_only_big, G_others);
    tools_csv.close();

    // orders
    ifstream orders("orders.csv");
    string row;
    getline(orders, row); // Header

    // output
    ofstream opt_size("opt_size.txt"), sol_cost("sol_cost.txt"),
      sol_time("sol_time.txt"), sol_info("sol_info.txt");

    while (getline(orders, row)) {

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
        auto OPT = opt(big_cities,
                       G_only_big,
                       G_others,
                       seller_city,
                       buyer_city,
                       order_time,
                       1,
                       4,
                       2);

        opt_size << OPT.size() << endl;
        sol_cost << cost_val(OPT) << endl;
        sol_time << time_val(order_time, OPT) << endl;

        for (auto& e : OPT) {
            sol_info << e << ",\t";
        }
        sol_info << endl;
    }

    orders.close();

    opt_size.close();
    sol_cost.close();
    sol_time.close();
    sol_info.close();

    return 0;
}

set<int>
get_big_cities(ifstream& plane_csv)
{
    set<int> big_cities;
    string row;

    getline(plane_csv, row); // Header
    while (getline(plane_csv, row)) {
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

        big_cities.insert(dep_city);
        big_cities.insert(arr_city);
    }

    return big_cities;
}

void
construct_graphs(set<int> big_cities,
                 ifstream& tools_csv,
                 MultiDiGraph& G_only_big,
                 MultiDiGraph& G_others)
{
    string row;

    getline(tools_csv, row); // Header
    while (getline(tools_csv, row)) {
        istringstream sin(row);
        string field;

        int dep_city, arr_city;
        double dep_time, arr_time, cost;
        int tool_type;
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
        tool_type = atof(field.c_str());

        if (big_cities.find(dep_city) == big_cities.end() ||
            big_cities.find(arr_city) ==
              big_cities.end()) // one of the two is not big city
            G_others.add_edge(
              dep_city,
              arr_city,
              edge(dep_city, arr_city, dep_time, arr_time, cost, tool_type));

        else // big city discount
            G_only_big.add_edge(
              dep_city,
              arr_city,
              edge(dep_city, arr_city, dep_time, arr_time, cost, tool_type));
    }
}