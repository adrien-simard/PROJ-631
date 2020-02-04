# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 17:51:04 2020

@author: 33699
"""
"""calculer le noeud syst`eme
a recevoir la donn´ee pour le premier utilisateur puis calculer le plus court chemin
entre ce noeud et le second utilisateur. Il faudra alors choisir le noeud de
ce chemin qui minimise le temps d’acc`es pour les deux utilisateurs.
"""


import Q2 as q2
import networkx as nx
import structureQ3 as st3




def receive_node(data,G,user):
    """Return le noeud syst`eme a recevoir la donn´ee pour le premier utilisateur
    
    Parameters :
    ===========================================================================
        data: dict 
        G : NetworkX graph
        user : string (user node)
        
        
    Returns :
    ===========================================================================
    
    """
    voisins= q2.select_syts_negbour(G,user)
    l_weight =[]
    for voisin in voisins:
            l_weight.append(nx.dijkstra_path_length(G,user,voisin,weight='weight'))     
    l_weight.sort()

    i = 0
    for voi in voisins:
        pds_min = l_weight[i]
        place = q2.place_restante(G,voi)
        
        if nx.dijkstra_path_length(G,user,voi,weight='weight') <= pds_min and data['size']<= place:
    
            return voi
        else:
            i = i + 1
            
def short_path(node,G,user):
    return nx.dijkstra_path(G,node,user,weight='weight')
def mediane(l):
    return l[int(len(l)/2)]

def placement_Q3(data,G,user1,user2):
    n1 = receive_node(st3.data8,st3.G,user1)
    path = short_path(n1,st3.G,user2)
    med = mediane(path)
    place = q2.place_restante(G,med)
    if data['size']<= place:
        G.nodes[user1]['list_id_data'].append(data['id_data'])
        G.nodes[med]['list_id_data'].append(data['id_data'])
        G.nodes[user2]['list_id_data'].append(data['id_data'])
    else: 
        i=1
        while i<=len(path)/2:
            
            if data['size']<= q2.place_restante(st3.G,med-i):
                G.nodes[user1]['list_id_data'].append(data['id_data'])
                G.nodes[med-i]['list_id_data'].append(data['id_data'])
                return G.nodes[user2]['list_id_data'].append(data['id_data'])
            elif data['size']<= q2.place_restante(st3.G,med-i):
                G.nodes[user1]['list_id_data'].append(data['id_data'])
                G.nodes[med-i]['list_id_data'].append(data['id_data'])
                return G.nodes[user2]['list_id_data'].append(data['id_data'])
            else:
                i=i+1
        print("plus de place pour",data)
        
                
        
        
    
placement_Q3(st3.data8,st3.G,'user1','user4')
placement_Q3(st3.data7,st3.G,'user1','user4')  

for i in [1,2,3,4]:
    #print(st.G.nodes['user1']['list_id_data'])
    print(st3.G.nodes[i]['list_id_data'])
    




    