from graphviz import Digraph
import copy
class Node:
    def __init__(self,indeks):
        self.degisecekIndeks = None
        self.devam = None
        self.move = None
        self.indeks = indeks
        self.parent = None
        self.adres = 0 
class binary_Tree:
    def __init__(self,size):
        self.liste = [None] * size
        self.sayac = 0 
        self.sayac2 = 0
        self.size = size
        self.root = None
        self.root2 = None
        self.anahtar = None
        
    def hashing1(self,anahtar1):
        return (anahtar1 % self.size)

    def hashing2(self,anahtar1,indeks):
        return(indeks + anahtar1 // self.size) % self.size
    
    def elemanEkle(self,anahtar):
        self.sayac2 = 0
        self.anahtar = anahtar
        if(self.sayac == self.size):
            return
        self.sayac += 1   
        indeks = self.hashing1(anahtar)
        if((self.liste[indeks] is None) or (self.liste[indeks] == '*')):
            self.sayac2 += 1
            self.root = Node(indeks) 
            self.root.adres = self.sayac2
            self.root2 = Node(self.anahtar)
            self.root2.move = self.root
            dot = self.visualize()
            dot.render('binary_tree', view=True)
            self.liste[indeks] = anahtar
        else:
            self.sayac2 += 1
            kuyruk = list()
            self.root = Node(indeks)
            self.root.indeks = indeks
            self.root.adres = self.sayac2

            kuyruk.append(self.root)
            tmp = self.root
            
            while(self.liste[kuyruk[0].indeks] is not None):
                if(kuyruk[0].degisecekIndeks is not None):
                    indeks = self.hashing2(self.liste[kuyruk[0].degisecekIndeks],kuyruk[0].indeks)
                    kuyruk[0].devam = Node(indeks)
                    
                else:
                    indeks = self.hashing2(anahtar,kuyruk[0].indeks)
                    kuyruk[0].devam = Node(indeks)
                self.sayac2 += 1
                kuyruk[0].devam.adres = self.sayac2
                tmp =kuyruk[0].devam
                tmp.parent = kuyruk[0]
                tmp.degisecekIndeks = kuyruk[0].degisecekIndeks
                
                
                if((self.liste[tmp.indeks] is None) or self.liste[tmp.indeks] == '*'):
                    self.sayac2 += 1
                    self.root2 = Node(self.anahtar)
                    self.root2.adres = self.sayac2
                    self.root2.move = self.root  

                    dot = self.visualize()
                    dot.render('binary_tree', view=True)
                    while(tmp.parent is not None):
                        if ((tmp.degisecekIndeks is not None) and (tmp.parent.parent is not None)):
                            self.liste[tmp.indeks] = self.liste[tmp.degisecekIndeks]
                            self.liste[tmp.degisecekIndeks] = self.liste[tmp.parent.parent.indeks]
                        else:                            
                            self.liste[tmp.indeks] = anahtar
                        g = tmp.degisecekIndeks
                        while((tmp.indeks != g) and tmp.parent is not None):
                            tmp = tmp.parent
                    break
                kuyruk.append(tmp)
                
                indeks = self.hashing2(self.liste[kuyruk[0].indeks],kuyruk[0].indeks)
                kuyruk[0].move = Node(indeks)
                self.sayac2 += 1
                kuyruk[0].move.adres = self.sayac2
                tmp2 = kuyruk[0].move
                tmp2.parent = kuyruk[0]
                tmp2.degisecekIndeks = kuyruk[0].indeks
                
                
                if((self.liste[tmp2.indeks] is None) or self.liste[tmp2.indeks] == '*'):
                    self.root2 = Node(self.anahtar)
                    self.sayac2 += 1
                    self.root2.adres = self.sayac2
                    self.root2.move = self.root

                    dot = self.visualize()
                    dot.render('binary_tree', view=True)
                    while(tmp2.parent is not None):
                        if ((tmp2.degisecekIndeks is not None) and (tmp2.parent.parent is not None)):
                            self.liste[tmp2.indeks] = self.liste[tmp2.parent.indeks]
                            self.liste[tmp2.parent.indeks] = self.liste[tmp2.parent.parent.indeks]
                        else:
                            if(tmp2.parent is not None and tmp2.parent.parent is None and tmp2.parent.indeks == tmp2.degisecekIndeks):
                                self.liste[tmp2.indeks] = self.liste[tmp2.parent.indeks]
                                self.liste[tmp2.parent.indeks] = anahtar
                            else:
                                self.liste[tmp2.indeks] = anahtar
                        g = tmp2.degisecekIndeks
                        while((tmp2.indeks != g) and tmp2.parent is not None):
                            tmp2 = tmp2.parent
                    break
                kuyruk.append(tmp2)
                kuyruk.pop(0)
                               
    def elemanSil(self,silinecekEleman):
        if(self.sayac <= 0):
            return False
        indeks =self.hashing1(silinecekEleman)
        dizi = list()
        dizi.append(indeks) 
        d = True 
        while(self.liste[indeks] is not None):
            if(self.liste[indeks] == silinecekEleman):
                self.liste[indeks] = '*'
                self.sayac -= 1
                d = False
                return True
                break
            else:
                indeks =self.hashing2(silinecekEleman,indeks)
                dizi.append(indeks)
                 
                i=0
                while i < len(dizi):
                    j = i+1
                    if(dizi[i] != '*'):
                        while j < len(dizi):
                            if dizi[j] != '*' and (dizi[j] == dizi[i]):
                                dizi[i] = None
                            j+=1
                    i+=1
                i=0  
                count = 0
                while i < len(dizi):
                    if dizi[i] is not None:
                        count += 1
                    i+=1
                if count >= self.size:
                    break
                    
        if(d):
            return False
              
    
    def elemanAra(self,eleman):
        indeks = self.hashing1(eleman)
        dizi = list()
        dizi.append(indeks)
        d = True
        while(self.liste[indeks] is not None):
            if(self.liste[indeks] == eleman):
                d = False
                return True
                break 
            else:
                indeks =self.hashing2(eleman,indeks)
                dizi.append(indeks)
                
                i=0
                while i < len(dizi):
                    j = i+1
                    if(dizi[i] != '*'):
                        while j < len(dizi):
                            if dizi[j] != '*' and (dizi[j] == dizi[i]):
                                dizi[i] = None
                            j+=1
                    i+=1
                i=0  
                count = 0
                while i < len(dizi):
                    if dizi[i] is not None:
                        count += 1
                    i+=1
                if count >= self.size:
                    break
        if(d):
            return False

    def visualize(self):
        def add_nodes_edges(node, dot=None):
            if dot is None:
                dot = Digraph()
            if node.devam:
                dot.node(name=str(node.devam.adres), label=f"{node.devam.indeks} ({self.liste[node.devam.indeks]})")
                dot.edge(str(node.adres), str(node.devam.adres))
                dot = add_nodes_edges(node.devam, dot=dot)
            else:
                
                self.sayac2 += 1
                null_devam = str(self.sayac2) + 'null_devam'
                dot.node(null_devam, label='None', style='filled', color='lightgrey')
                dot.edge(str(node.adres), null_devam)
            
            if node.move:
                dot.node(name=str(node.move.adres), label=f"{node.move.indeks} ({self.liste[node.move.indeks]})")
                dot.edge(str(node.adres), str(node.move.adres))
                dot = add_nodes_edges(node.move, dot=dot)
            else:
                
                self.sayac2 += 1
                null_move = str(self.sayac2) + 'null_move'
                dot.node(null_move, label='None', style='filled', color='lightgrey')
                dot.edge(str(node.adres), null_move)

            return dot
        
        dot = Digraph()
        dot.node(name=str(self.root2.adres), label=str(self.root2.indeks))
        dot = add_nodes_edges(self.root2, dot=dot)
        dot.render('binary_tree', format='png', cleanup=True)
        
        return dot


