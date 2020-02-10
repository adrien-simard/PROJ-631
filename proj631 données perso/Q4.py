# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 11:37:06 2020

@author: 33699
"""
import Q2 as q2

data1 = {"id_data":1001,'size':20}
data2 = {"id_data":1002,'size':20}
data3 = {"id_data":1003,'size':40}
data4 = {"id_data":1004,'size':80}
data5 = {"id_data":1005,'size':20}
data6 = {"id_data":1006,'size':40}
data7 = {"id_data":1007,'size':40}
data8 = {"id_data":1008,'size':20}
list_data =[data1,data2,data3,data4,data5,data6,data7,data8]


dt = [data6,data7,data8]
list_node =[1,2,3,4,'user1','user4']
#We use the library Networkx to build a graph with the users nodes and the system nodes
import networkx as nx
# Create an empty graph with no nodes and no edges
G = nx.Graph()


#user node
G.add_node('user1',ID=1234,list_id_data=[],id_nodes=[])
G.add_node('user4',ID=1234,list_id_data=[],id_nodes=[])

G.add_node(1,memory=50,ID=1234,list_id_data=[])
G.add_node(2,memory=80,ID=1111,list_id_data=[],id_nodes=[])
G.add_node(3,memory=160,ID=1112,list_id_data=[],id_nodes=[])
G.add_node(4,memory=120,ID=1113,list_id_data=[],id_nodes=[])

G.add_edge(1,'user1',weight=1)
G.add_edge(1,2,weight=3)
G.add_edge(2,3,weight=2)
G.add_edge(3,4,weight=4)
G.add_edge(4,'user4',weight=1)

G.number_of_nodes()
G.nodes[1]
def list_nodes(G):
    n = G.number_of_nodes()
    list_node =[]
    for i in range(1,n):
        list_node.append(G.nodes[i])

def sort_bysize(data_list):
    """Returns the data list sorts by id
    
    Parameters :
    ===========================================================================
        data list : list 
        
    Returns :
    ===========================================================================
        sort_list : list
    
    """
    size_list = []
    sort_data =[]
    for data in data_list:
        size_list.append(data["size"])
    size_list =list(set(size_list))
    size_list.sort()
    
    for size in size_list:
        for data in data_list:
            if size == data['size']:
                sort_data.append(data)
    return sort_data





def KS(n,C,list_data):
    
    """Returns the list of data that will fill the node. The filling is optimized
    
    Parameters :
    ===========================================================================
    n : list size

    C : node capacity    
    
    list_data : list of data list of dict
        
    Returns :
    ===========================================================================
        list : list of dict 
    
    """
    
    if n<0 :#stop condition
        result = [{'id_data': 0, 'size': 0}]
    elif list_data[n]['size']>C:#capacity too small,change node
        result = KS(n-1,C,list_data)
    else:
        
        tmp1 = KS(n-1,C,list_data)#don't select the node,change node
        tmp2 = [list_data[n]] + KS(n-1,C-list_data[n]['size'],list_data)#select the node
        l1=[]
        l2=[]
        for i in range(len(tmp2)-1):
            a = tmp2[i]['size']
            #create a list with the data of tmp2
            l2.append(a)
        for i in range(len(tmp1)-1):
            a = tmp1[i]['size']
            #create a list with the data of tmp1
            l1.append(a)
            
        if sum(l2)>sum(l1):#chose the biggest list
            result = tmp2
        else:
            result=tmp1
            
        for i in range(len(result)-1):
            b = result[i]['size']
            if b == 0:
                result.remove(result[i])
    return result


    
def remove_dataById(l,list_data):
    
    """Delete the data in list_data which are in the other list of data (l)
    
    Parameters :
    ===========================================================================

    l : list of data list of dict   
    
    list_data : list of data list of dict
        
    Returns :
    ===========================================================================
        data_list : list of dict 
    
    """
    
        
    lid = []
    for data in l:
        lid.append(data['id_data'])
    for data in list_data:
        
        for Id in lid :
            if Id == data['id_data'] and (data in list_data):
                list_data.remove(data)
    return list_data

    


def list_dist(G,list_data,user,list_nodes):
    """Returns the list of distance between the user node and the other system nodes
    
    Parameters :
    ===========================================================================

    list_nodes :list of node object
    
    G : NetworkX graph
    
    user : string (user node label)
        
    Returns :
    ===========================================================================
        data_list : list of int 
    
    """
    l_dist=[]
    path = nx.dijkstra_predecessor_and_distance(G, user)[1]
    l_node = []
    
    if user in list_nodes:
        list_nodes.remove(user)
    for node in list_nodes:
        
        l_dist.append(path[node])
    l_dist.sort()
    for dist in l_dist:
        for node in list_node:
            if path[node]== dist:
                l_node.append(node)
   
    return l_node
        
list_dist(G,list_data,'user4',list_node)

def MKP(G,list_data,list_nodes,user):
    """Puts a list of data that will fill the nodes. The nodes are closer to the user. 
    The filling is optimized
    
    Parameters :
    ===========================================================================

    list_node :list of node object
    
    G : NetworkX graph
    
    user : string (user node label)
        
    Returns :
    ===========================================================================
        
    
    """
    l_node = list_dist(G,list_data,user,list_nodes)
    
    for i in range(len(l_node)):
        
        if type(l_node[i])== type('user'):
            l_node.remove(l_node[i])
           
    for node in l_node:
        s = sort_bysize(list_data)
        p = KS(len(list_data)-1,q2.place_restante(G,node),s)
        p.remove(p[-1])
        list_data= remove_dataById(p,list_data)
        
        for data in p:
            
                G.nodes[user]['list_id_data'].append(data['id_data'])
                G.nodes[node]['list_id_data'].append(data['id_data'])
        list_data= remove_dataById(p,list_data)
       
        
        
        

        

MKP(G,dt,list_node,'user1') 
MKP(G,list_data,list_node,'user4') 
for i in [1,2,3,4]:
    #print(st.G.nodes['user1']['list_id_data'])
    print(G.nodes[i]['list_id_data'])        
nx.draw_networkx(G) 
    


















    
    
