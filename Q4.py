# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 11:37:06 2020

@author: 33699
"""
data1 = {"id_data":1001,'size':20}
data2 = {"id_data":1002,'size':20}
data3 = {"id_data":1003,'size':20}
data4 = {"id_data":1004,'size':80}
data5 = {"id_data":1005,'size':20}
data6 = {"id_data":1006,'size':40}
data7 = {"id_data":1007,'size':40}
data8 = {"id_data":1008,'size':20}
list_data =[data1,data2,data3,data4,data5,data6,data7,data8]
dt = [data6,data7,data8]

#We use the library Networkx to build a graph with the users nodes and the system nodes
import networkx as nx
# Create an empty graph with no nodes and no edges
G = nx.Graph()
#comme dans une représentation ensembliste on construit l'arbre à partir de liste

#user node
G.add_node('user1',ID=1234,list_id_data=[data1["id_data"]],id_nodes=[])
G.add_node('user4',ID=1234,list_id_data=[data2["id_data"]],id_nodes=[])

G.add_node(1,memory=50,ID=1234,list_id_data=[data1["id_data"]])
G.add_node(2,memory=80,ID=1111,list_id_data=[data2["id_data"]],id_nodes=[])
G.add_node(3,memory=80,ID=1112,list_id_data=[data3["id_data"]],id_nodes=[])
G.add_node(4,memory=80,ID=1113,list_id_data=[data4["id_data"]],id_nodes=[])

G.add_edge(1,'user1',weight=1)
G.add_edge(1,2,weight=3)
G.add_edge(2,3,weight=2)
G.add_edge(3,4,weight=4)
G.add_edge(4,'user4',weight=1)

G.number_of_nodes()

def place_nodes(G):
    G.number_of_nodes()
    
