#include "./Graph.hpp"
#include "./dfs_opt_path.hpp"
#include <bits/stdc++.h>
using namespace std;

void
construct_graph(MultiDiGraph& G, ifstream& csv);

set<int>
get_hubs(MultiDiGraph& G, int hub_num);

void
construct_out_ways(MultiDiGraph& G,
                   MultiDiGraph& out_ways,
                   set<int>& hubs,
                   double discount);

int
main()
{
    // read tools.csv and construct a multi-directed-graph
    MultiDiGraph G(656 + 1);
    ifstream csv("tools.csv");
    construct_graph(G, csv);
    csv.close();

    // set hubs
    int hub_num;
    cout << "Number of hubs: ";
    cin >> hub_num;
    double discount;
    cout << "traffic cost discount: ";
    cin >> discount;
    set<int> hubs = get_hubs(G, hub_num);

    // the way out of hub
    MultiDiGraph out_ways(656 + 1);
    construct_out_ways(G, out_ways, hubs, discount);

    // orders
    csv = ifstream("orders.csv");
    string row;

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
        auto OPT =
          opt(G, seller_city, buyer_city, order_time, 4, hubs, out_ways);

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

void
construct_graph(MultiDiGraph& G, ifstream& csv)
{
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
}

set<int>
get_hubs(MultiDiGraph& G, int hub_num)
{
    auto cmp = [&G](int a, int b) { return G[a].degree() < G[b].degree(); };
    priority_queue<int, vector<int>, decltype(cmp)> q(cmp);

    for (int i = 1; i <= 656; i++)
        q.push(i);

    set<int> hubs;

    for (int i = 0; i < hub_num; i++) {
        hubs.insert(q.top());
        q.pop();
    }

    return hubs;
}

void
construct_out_ways(MultiDiGraph& G,
                   MultiDiGraph& out_ways,
                   set<int>& hubs,
                   double discount)
{
    for (auto& city : hubs) {
        set<int> reachable;
        for (auto& kv : G[city]) {
            int arr_city = kv.first;
            reachable.insert(arr_city);
        }

        for (int arr : reachable) {
            double MIN = 999999999;
            edge out_way;
            for (auto i = G[city][arr].first; i != G[city][arr].second; i++) {
                if (val(i->second) < MIN) {
                    MIN = val(i->second);
                    out_way = i->second;
                }
            }

            out_way.cost *= (1 - discount); // discount
            out_ways.add_edge(city, arr, out_way);
            out_way.dep_time += 1440;
            out_way.arr_time += 1440;
            out_ways.add_edge(city, arr, out_way);
        }
    }
}