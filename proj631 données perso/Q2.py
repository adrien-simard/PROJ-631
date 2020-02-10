# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:42:03 2020

@author: Adrien Simard
"""
import structure2 as st
import networkx as nx




def place_restante(G,n1):
    """Returns the free memory in a node
    
    Parameters :
    ==========
        G : NetworkX graph
        
        n1 : system node
        
    Returns :
    =========
        place_restante : int
    """
    memo = G.nodes[n1]['memory']
    size = 0
    id_data= G.nodes[n1]['list_id_data']
    for data in st.list_data :
        if data['id_data'] in id_data:
            size = size + data['size']

    return memo - size 

def select_syts_negbour(G,user):
    """Returns all the system nodes which are accesible for the user node
    
    Parameters :
    ===========================================================================
        G : NetworkX graph
        
        user : user node 
        
    Returns :
    ===========================================================================
        voisins : list of node accessible
        
    """
    l =[]
    i = 1
    while G.has_node(i)== True:
        l.append(i)
        i = i+1
    return l


def sort_byID(data_list):
    """Returns the data list sorts by id
    
    Parameters :
    ===========================================================================
        data list : list 
        
    Returns :
    ===========================================================================
        sort_list : list
    
    """
    id_list = []
    sort_data =[]
    for data in data_list:
        id_list.append(data["id_data"])
    id_list.sort()
    for ID in id_list:
        for data in data_list:
            if ID == data['id_data']:
                sort_data.append(data)
    return sort_data

def placement_data(data,G,user):
    """Place a data in a system node
    
    Parameters :
    ===========================================================================
        data: dict 
        G : NetworkX graph
        user : string (user node)
        
        
    Returns :
    ===========================================================================
    
    """
    voisins= select_syts_negbour(G,user)
    l_weight =[]
    for voisin in voisins:
            l_weight.append(nx.dijkstra_path_length(G,user,voisin,weight='weight'))     
    l_weight.sort()
    print("lll",l_weight)
    i = 0
    for voi in voisins:
        pds_min = l_weight[i]
        place = place_restante(G,voi)

        if nx.dijkstra_path_length(G,user,voi,weight='weight') <= pds_min and data['size']<= place:
            G.nodes[user]['list_id_data'].append(data['id_data'])
            return G.nodes[voi]['list_id_data'].append(data['id_data'])
        else:
            i = i + 1

def placement_data_from(data_list,G,user):
    """Place a list of datas by id order
    
     Parameters :
    ===========================================================================
        data list : list
        G : NetworkX graph
        user : string (user node)
        
        
    Returns :
    ===========================================================================
    """
    data_list = sort_byID(data_list)
    for data in data_list:
        placement_data(data,G,user)

#test
placement_data_from(st.dt,st.G,"user1")

for i in [1,2,3,4,5]:
    #print(st.G.nodes['user1']['list_id_data'])
    print(st.G.nodes[i]['list_id_data'])
nx.draw_networkx(st.G)  

