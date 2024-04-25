def hashing1(anahtar1):
    return (anahtar1 % size)

def hashing2(anahtar1,indeks):
    return(indeks + anahtar1 // size) % size
  
class Node:
    def __init__(self,indeks):
        self.degisecekIndeks = None
        self.devam = None
        self.move = None
        self.indeks = indeks
        self.parent = None

class binary_Tree:
    def __init__(self,size):
        self.liste = [None] * size
        self.sayac = 0 
    def elemanEkle(self,anahtar):
        if(self.sayac == size):
            print("Daha yer yok!!")
            return
        self.sayac += 1
        indeks = hashing1(anahtar)
        if((self.liste[indeks] is None) or (self.liste[indeks] == '*')):
            self.liste[indeks] = anahtar            
        else:
            kuyruk = list()
            root = Node(indeks)
            root.indeks = indeks
            kuyruk.append(root)
            tmp = root
            
            while(self.liste[kuyruk[0].indeks] is not None):
                if(kuyruk[0].degisecekIndeks is not None):
                    indeks = hashing2(self.liste[kuyruk[0].degisecekIndeks],kuyruk[0].indeks)
                    kuyruk[0].devam = Node(indeks)
                else:
                    indeks = hashing2(anahtar,kuyruk[0].indeks)
                    kuyruk[0].devam = Node(indeks)
                tmp =kuyruk[0].devam
                tmp.parent = kuyruk[0]
                tmp.degisecekIndeks = kuyruk[0].degisecekIndeks
                
                if((self.liste[tmp.indeks] is None) or self.liste[tmp.indeks] == '*'):
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
                
                indeks = hashing2(self.liste[kuyruk[0].indeks],kuyruk[0].indeks)
                kuyruk[0].move = Node(indeks)
                tmp2 = kuyruk[0].move
                tmp2.parent = kuyruk[0]
                tmp2.degisecekIndeks = kuyruk[0].indeks
                
                if((self.liste[tmp2.indeks] is None) or self.liste[tmp2.indeks] == '*'):
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
        self.sayac -= 1
        indeks = hashing1(silinecekEleman)
        d = True
        while(self.liste[indeks] is not None):
            if(self.liste[indeks] == silinecekEleman):
                self.liste[indeks] = '*'
                print("{} elemanı başarılı bir şekilde silindi..".format(silinecekEleman))
                d = False
                break
            else:
                indeks =hashing2(silinecekEleman,indeks)
        if(d):
            print("Eleman bulunamadı!!!")                    
    
    def elemanAra(self,eleman):
        indeks = hashing1(eleman)
        d = True
        while(self.liste[indeks] is not None):
            if(self.liste[indeks] == eleman):
                print("{} elemanı tabloda bulunmaktadir..".format(eleman))
                d = False
                break 
            else:
                indeks =hashing2(eleman,indeks)
        if(d):
            print("Eleman bulunamadı!!!") 
     
size = None
tercih = True

while(type(size) != int):
    size = eval(input("Tablonun büyüklüğünü giriniz:"))
b = binary_Tree(size)
while(tercih):
    print("1-Eleman ekle")
    print("2-Eleman ara")
    print("3-Eleman sil")
    print("Çıkmak için 0 tuşuna basınız.")
    
    cevap = eval(input("Tericihinizi giriniz:"))
    if(cevap == 0):
        tercih = False
    elif(type(cevap) != int or (cevap < 1) or (cevap > 3)):
        print("Geçersiz bir ifade girdiniz!!")
    else:
        if(cevap == 1):
            eklenecekEleman = eval(input("Eklemek istediğiniz elemanı giriniz:"))
            b.elemanEkle(eklenecekEleman)
        elif(cevap == 2):
            aranacakEleman = eval(input("Sorgulamak istediğiniz elemanı giriniz:"))
            b.elemanAra(aranacakEleman)
        elif(cevap == 3):
            silinecekEleman = eval(input("Silmek istediğiniz elemanı giriniz:"))
            b.elemanSil(silinecekEleman)
        print("\n*********TABLO**************")
        i = 0
        while(i < size):
            if(b.liste[i] is not None):
                print("liste[{}] = {}".format(i, b.liste[i]))
            i = i + 1
        print("\n",end = "")