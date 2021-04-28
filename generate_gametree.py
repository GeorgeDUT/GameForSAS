import networkx as nx
import random
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import gambit



def get_graph_networkx(node_list, edge_list):         # CUSTOM-CODED FUNCTION
    G = nx.DiGraph()                                # Empty directional graph
    G.add_nodes_from(node_list)                     # Adding nodes (components)
    G.add_edges_from(edge_list)                     # Adding edges (connections)
    return G


def find_root(mygame_tree, mynode):
    while len(list(mygame_tree.predecessors(mynode)))!=0:
        mynode = list(mygame_tree.predecessors(mynode))[0]
    return mynode


# Middle Right Left (DLR)
def dfs(my_game_tree,start_node):
    game_nodes = []
    visited_nodes = []
    helper = []
    helper.append(start_node)
    visited_nodes.append(start_node)
    game_nodes.append(start_node)

    while len(helper)!=0:
        start_node = helper[-1]
        next_nodes = list(my_game_tree.successors(start_node))
        # remove visited nodes.
        for node in list(my_game_tree.successors(start_node)):
            if node in visited_nodes:
                next_nodes.remove(node)
        # find the left node.
        if len(next_nodes)!=0:
            max_node = next_nodes[0]
            for node in next_nodes:
                if max_node > node:
                    max_node = node
            game_nodes.append(max_node)
            visited_nodes.append(max_node)
            helper.append(max_node)
        else:
            helper.pop()
    return game_nodes


if __name__=="__main__":
    # with open('data/edge_list_to_Send-1.txt','r') as f1:
    #     edge_list_read = f1.readlines()
    # with open('data/node_list_to_Send-1.txt', 'r') as f2:
    #     node_list_read = f2.readlines()

    node_list_read = pd.read_csv('data/node_list_to_Send-1.txt', sep=' ', header=None)
    edge_list_read = pd.read_csv('data/test_edge.txt',sep=' ', header = None)
    node_list = []
    edge_list = []
    for i in range(len(node_list_read[0])):
        node = node_list_read[0][i]
        node_list.append(node)
    for i in range(len(edge_list_read[0])):
        start = edge_list_read[0][i]
        end = edge_list_read[1][i]
        edge_list.append([start,end])

    """this is test node list"""
    """
    mv has two actions: open, close
    pump has two actions: on, off
    uv has two actions: on, off
    """
    # player = ['MV_101','P_101','MV_201','P_301','MV_301','MV_302','P_401','UV_401','P_501',
    #           'MV_501','MV_503','MV_502','MV_504','P_601','P_602']

    # player = ['MV_101','P_101','MV_201','P_301','MV_301','MV_302','P_401','UV_401','P_501','MV_500','P_600','END_0']
    # player = ['MV_101', 'P_101', 'MV_201', 'P_301', 'MV_301', 'MV_302', 'P_401', 'UV_401', 'P_501','END_0']
    # player = ['MV_101', 'P_101', 'MV_201', 'P_301', 'MV_301', 'MV_302', 'P_401', 'END_0']
    player = ['MV_101', 'P_101', 'MV_201', 'P_302', 'MV_302', 'P_402','P_501','MV_501', 'END_0']
    bad_player = ['P_101','P_501']
    # player = ['MV_101', 'P_101', 'MV_201', 'P_301', 'MV_302', 'END_0']
    # establish tree from architecture graph


    # start  = 'MV_101'
    # new_edge_list= []
    # while 1:
    #     if list(game_tree.successors(start)):
    #         for i in range(list(game_tree.successors(start))):
    #             if game_tree.successors(start)[i] in player:
    #                 new_edge_list.append(start,game_tree.successors(start)[i])
    #             else:
    #                 node = game_tree.successors(start)[i]
    #                 while node not in player:
    #                     node = list(game_tree.successors(node))[0]
    #                 new_edge_list.append(start,node)

    new_edge_list = []
    new_node_list = []
    for i in range(0,len(player)):
        for j in range(pow(2,i)):
            node_name = player[i]+'_'+str(j)
            new_node_list.append(node_name)

    for i in range(pow(2,len(player)-1)-1):
        new_edge_list.append([new_node_list[i],new_node_list[2*i+1]])
        new_edge_list.append([new_node_list[i], new_node_list[2 * i + 2]])

    print(new_edge_list)
    print(len(new_edge_list))

    node_action = ["close","open","off","on"]

    game_tree = get_graph_networkx(new_node_list, new_edge_list)
    new_node_list = dfs(game_tree,'MV_101_0')

    # game_nodes = dfs(game_tree,1)
    # print(game_nodes)
    cnt = 0
    info_set = [0]*len(player)
    # read the utility file
    data = pd.read_csv("data/utility_source_new_version", delim_whitespace=True)
    for i in range(int(len(data))):
        r = data['value'][i]
    utility_item = 0

    for node in new_node_list:
        # print(node,list(game_tree.predecessors(node)))
        if list(game_tree.successors(node)):
            player_name = node[0:node.index('_')+4]
            """player type is MV,P,UV"""
            player_type = node[0:node.index('_')]
            if player_type == 'MV':
                action1,action2='close','open'
            elif player_type == 'P':
                action1,action2='off','on'
            else:
                action1,action2='off','on'
            player_id = player.index(player_name)
            info_set[player_id] = info_set[player_id] + 1
            print 'p','\"',node,'\"',\
                player_id+1, info_set[player_id], \
                '\"\"', \
                '{','\"',action1,'\"','\"',action2,'\"','}',\
                0
        else:
            u = data['value'][utility_item]
            utility_item = utility_item + 1
            cnt = cnt + 1
            print 't', '\"', node, '\"', \
            cnt, \
            '\"\"', \
                '{', u/6, ',', u/6, ',', u/6, ',', u/6, ',', -u/2, ',', -u/2, ',',u/6, ',',u/6,'}'
                # '{', 0, ',', 0, ',', 0, ',', 0, ',', 0, ',', 0, ',', 0, ',', 0, ',', 0, '}'
            # '{', 0, ',', 0, ',', 0, ',', 0, ',', 0, ',', 0, ',', 0, ',', 0, ',', 0, ',', 0, ',', 0, '}'
            # '{', 0, ',', 0, ',', 0, ',', 0, ',', 0, '}'
    # nx.draw_networkx(game_tree)
    pos = nx.circular_layout(game_tree)
    nx.draw(game_tree,with_labels=True,pos=pos)
    # plt.show()

