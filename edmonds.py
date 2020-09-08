import sys

class Node:
    def __init__(self,label):
        self.label=label
        self.miu=None
        self.phi=None
        self.rho=None
        self.scanned=False
        self.neighbours=[]

    def is_outer(self):

        #Check if node is an outer node. Criteria prop. 10.29 korte-vygen
        
        if self.miu==self or self.miu.phi!=self.miu:
            return True
        else:
            return False

    def is_inner(self):

        #Check if node is an inner node. Criteria prop. 10.29 korte-vygen
        
        if self.miu.phi==self.miu and self.phi!=self:
            return True
        else:
            return False

    def is_out_of_forest(self):

        #Check if node is out of forest. Criteria prop. 10.29 korte-vygen
        
        if self.miu!=self and self.phi==self and self.miu.phi==self.miu:
            return True
        else:
            return False


class Edge:
    def __init__(self,label,nodes):
        self.label=label
        self.nodes=nodes #this is a list consisting of 2 object from class Node


def extract(input_file):
    '''
    Extracts data from input file
    
    Input: 
    * input_file: name of input file including extension
        - type: str

    Output: 
    * [Nodes,Edges_dict]: A list containing a list of nodes and a dictionary of edges.
                          The dictionary gives the label of the connected nodes for each edge
        - type: list(list(Node),dict)
    '''
    
    #Extract the data
    
    Edges_name=[]
    Edges_component=[]
    edgelist=[]
    content=[]
    file=open(input_file,'r')
    lines=file.readlines()
    file.close()
     
    for i in lines:
        i=i.replace('\n','')
        i=i.replace(' ','')
        content.append(i)

    for i in content:
        if i=='' or i[0]=='#':
            continue
        if i[0]=='n':
            Nodes=[j for j in range(1,int(i[2:])+1)]
            continue
        if i[0]=='m':
            Edges_name=[j for j in range(1,int(i[2:])+1)]
            break
        
    for v in Nodes:
        for line in content:
            num=str(v)
            digit=len(num)
            if line[:digit]==num:
                incident=line[digit+1:]
                splitted=incident.split(',')
                if splitted==['']:
                    #Handles the case where a node has no incident edges
                    edgelist.append([])
                    break
                else:
                    adj=[int(i) for i in splitted]
                    edgelist.append(adj)
                    break
                
    for e in Edges_name:
        A=[]
        for i in range(len(edgelist)):
            if e in edgelist[i]:
                A.append(i+1)
        Edges_component.append(A)

    Edges_dict=dict(zip(Edges_name,Edges_component))

    return [Nodes,Edges_dict]



def create_nodelist(V):
    '''
    Creates node list
    
    Input: 
    * V: list of node labels 1,2,..,|V|
        - type: list

    Output: 
    * [Node(i) for i in V]: A list containing nodes with the label 1,2,...,|V|
        - type: list(Node)
    '''
    return [Node(i) for i in V]


def create_edgelist(E,V):
    '''
    Creates an edge list. For each edge update the 'nodes' attribute
    
    Input: 
    * E: dictionary obtained from the routine 'extract'
        - type: dict
    * V: list containing nodes
        - type: list(Node)

    Output: 
    * E2: A list containing edges with the label 1,2,...,|E|.
          Each edge has attribute 'nodes', which contains the two nodes that they connect.
        - type: list(Edge)
    '''
    E2=[]
    for i in E.keys():
        L=E[i]
        v=L[0]
        w=L[1]
        e=Edge(i,[V[v-1],V[w-1]])
        E2.append(e)
    return E2
        
        
def find_edge(v,w,E):
    '''
    Finds an edge that connects the nodes v and w or determine that none exists
    
    Input: 
    * v: a node 
        - type: Node
    * w: another node
        - type: Node
    * E: list of edges obtained by the routine 'create_edgelist'
        - type: list(Edge)

    Output: 
    * If there is no edge that connects v and w, or v==w, then output None 
        - type: NoneType
    * If such an edge exists, then output the edge e
        - type: Edge
    '''
    for e in E:
        #handles the case if v==w
        if v==w:
            return None
        if v in e.nodes and w in e.nodes:
            return e
    return None
    


def find_neighbours(E):
    '''
    For each node v in the node list V, update the neighbours attribute
    
    Input: 
    * E: Edge list obtained from the routine 'create_edgelist'
        - type: list(Edge)
    '''
    for e in E:
        v=e.nodes[0]
        w=e.nodes[1]
        v.neighbours.append(w)
        w.neighbours.append(v)


def are_paths_disjoint(P1,P2):
    '''
    Check if two paths are vertex-disjoint

    Input: 
    * P1: List of nodes that describe a path
        - type: list(Node)
    * P2: List of nodes that describe a path
        - type: list(Node)

    Output:
    * If the paths are disjoint then output True
        - type: bool
    * If the paths are not disjoint then output False
        - type: bool
    '''
    
    for i in P1:
        if i in P2:
            return False
    return True

  
def max_path(v):
    '''
    Find path from v to its root P(v)

    Input:
    * v: A node
        - type: Node

    Output:
    * P: A list of nodes depicting the path from v to its root
        - type: list(Node)
    '''
    P=[v]
    counter=0
    while True:
        counter+=1
        if counter%2==1:
            #odd -> miu
            if P[-1].miu!=P[-1]:
                P.append(P[-1].miu)
                continue
            else:
                break
        if counter%2==0:
            #even -> phi
            if P[-1].phi!=P[-1]:
                P.append(P[-1].phi)
                continue
            else:
                break
            
    #changes here
            
    r=P[-1]
    if r.miu==r:
        return P
    else:
        z=r.miu
        P.append(z)
        P.append(z.phi)
        return P
    
     #changes here


def is_dist_x_odd(v,P):
    '''
    Determines whether a given node v in P(x) has odd distance to x

    Input:
    * v: A node
        - type: Node
    * P: A list of nodes depicting a path
        - type: list(Node) 

    Output:
    * If v has odd distance to x then output True
        - type: bool
    * Else output False
        - type: bool
    '''
    v_pos=P.index(v)
    return (v_pos)%2==1


def find_r(P1,P2):
    '''
    Finds the first node r in P1 ⋂ P2 for which r.rho==r

    Input:
    * P1: A list of nodes depicting a path
        - type: list(Node)
    * P2: A list of nodes depicting a path
        - type: list(Node)

    Output:
    *  v: First node in P1 ⋂ P2 with v.rho==v
        - type: Node
    '''
    for v in P1:
        if v in P2:
            if v.rho==v:
                return v
            

def subpath(P,r):
    '''
    For a given path P(x) and a node r in P(x), output the subpath P(x)|[x,r]

    Input:
    * P: A list of nodes depicting a path
        - type: list(Node)

    Output:
    * P[:i+1]: The subpath P(x)|[x,r]
        - type: list(Node)
    '''
    i=P.index(r)
    return P[:i+1]
            

def update_unscanned(V):
    '''
    Gives a list containing unscanned outer nodes

    Input:
    * V: list of nodes
        - type: list(Node)

    Output:
    * unscanned: list of unscanned outer nodes
        - type: list(Node)


    '''
    unscanned=[]
    for v in V:
        if v.is_outer()==True:
            if v.scanned==False:
                unscanned.append(v)
    return unscanned

def update_neighbours(x,V):
    eligible=[y for y in x.neighbours if (y.is_out_of_forest()==True) or (y.is_outer()==True and y.rho!=x.rho)]
    return eligible


def find_max_match(V,E):
    '''
    Finds the maximum matching for the graph G=(V,E)

    Input:
    * V: node list
        - type: list(Node)
    * E: edge list
        - type: list(Edge)

    Output:
    * Matching: the matching edges
        - type: list(Edge)
    '''
    
    find_neighbours(E)
    
    #Step 1
    for v in V:
        v.miu=v
        v.phi=v
        v.rho=v
        v.scanned=False

    #Step 2
    unscanned=update_unscanned(V)
    while unscanned!=[]:
        v=unscanned[0]
        progress(v,V)
        unscanned=update_unscanned(V)
    
    Matching=[]
    
    for v in V:
        e=find_edge(v,v.miu,E)
        if e!=None:
            Matching.append(e)

    return Matching
            


def progress(x,V):
    '''
    Represents step 4,5,and 6 in the algorithm presented in Korte-Vygen

    Input:
    * x: a node
        - type: Node

    * V: node list
        - type: list(Node)

    Output:
    * If step 5 is done, outputs None, ending the loop
        - type: NoneType
    '''
    #Step 3
    eligible=update_neighbours(x,V)
    while eligible!=[]:
        y=eligible[0]
        if y.is_out_of_forest()==True:
            #Step 4
            y.phi=x
            #laufzeit verbessern moglich - 'rausnimmt'
            eligible=update_neighbours(x,V)
            continue
        
        if y.is_outer()==True and y.rho!=x.rho:
            P_x=max_path(x)
            P_y=max_path(y)
            if are_paths_disjoint(P_x,P_y)==True:
                #Step 5
                for v in P_x:
                    if is_dist_x_odd(v,P_x)==True:
                        v.phi.miu=v
                        v.miu=v.phi
                for v in P_y:
                    if is_dist_x_odd(v,P_y)==True:
                        v.phi.miu=v
                        v.miu=v.phi
                x.miu=y
                y.miu=x
                for v in V:
                    v.phi=v
                    v.rho=v
                    v.scanned=False
                return None

            else:
                #Step 6
                r=find_r(P_x,P_y)
                P_xr=subpath(P_x,r)
                P_yr=subpath(P_y,r)
                for v in P_xr:
                    if is_dist_x_odd(v,P_xr) and v.phi.rho!=r:
                        v.phi.phi=v
                for v in P_yr:
                    if is_dist_x_odd(v,P_yr) and v.phi.rho!=r:
                        v.phi.phi=v
                if x.rho!=r:
                    x.phi=y
                if y.rho!=r:
                    y.phi=x
                for v in V:
                    if v.rho in P_xr or v.rho in P_yr:
                        v.rho=r
                eligible=update_neighbours(x,V)
                continue
            
    x.scanned=True


def remove_duplicates(L):
    '''
    Remove multiple occurences of items in a given list

    Input:
    * L: a list
        - type: list

    Output:
    * list(set(L)): a list with multiple instances eliminated
        - type: list
    '''
    return list(set(L))


def edmonds(input_file,output_file):
    '''
    Edmonds' Matching Algorithm

    Input:
    * input_file: name of input file with extension
        - type: str
    * output_file: name of output file with extension
        - type: str
    '''
    V,E=extract(input_file)
    V2=create_nodelist(V)
    E2=create_edgelist(E,V2)
    M=find_max_match(V2,E2)
    M2=[e.label for e in M]
    M3=remove_duplicates(M2)
    M4=[str(i) for i in M3]
    X=[str(v.label) for v in V2 if v.is_inner()==True]
    f=open(output_file,'w+')
    f.write('M: '+(',').join(M4))
    f.write('\n')
    f.write('X: '+(',').join(X))
    f.close()

#Run the algorithm from Terminal:
    
edmonds(sys.argv[1],sys.argv[2])




    
    

                                       




