import networkx as nx
import random
from matplotlib import pyplot as plt
import numpy as np

Action = {
    'C':0,
    'D':1,
}


class SDRandom(object):
    # agent_list [rl-based,]
    def __init__(self,agent_list = [],edg_num=4):
        self.node_num = sum(agent_list)
        self.edg_num = edg_num

        self.reward_matrix = np.zeros((1,2))

        """generate random undirected graph"""
        self.graph = nx.Graph()
        for i in range(self.node_num):
            self.graph.add_node(i)
        """keep connecting all nodes"""
        for i in range(1,self.node_num):
            self.graph.add_edge(i-1,i)

        """randomly generate remaining edg_num - node_num edges"""
        for e in range(self.node_num,self.edg_num):
            start = random.randint(0,self.node_num-1)
            end = random.randint(0,self.node_num-1)
            self.graph.add_edge(start,end)

    def show_graph(self):
        nx.draw_networkx(self.graph)
        plt.show()

    def take_action(self,action_list=[]):
        reward_list = []
        for i in range(self.node_num):
            for (start,end) in self.graph.edges():
                if start == i or end == i:
                    print(start,end)






if __name__=="__main__":
    sd = SDRandom([10,20,10],100)
    a = np.zeros((5,5))
    sd.take_action([1,2,3])
    sd.show_graph()
