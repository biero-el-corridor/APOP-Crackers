# l'objectif et de brute force un hash md5 
#on doit additioner le contenue de la ligne 3 avec 
#un mdp pour optenie le ash de la ligne 5
#<1755.1.5f403625.BcWGgpKzUPRC8vscWn0wuA==@vps-7e2f5a72>
#4ddd4137b84ff2db7291b568289717f0
#test avec le fichier text 

#le probléme vien de ce putain de retour chariot de merde 

import hashlib
m = hashlib.md5()
import sys
import tkinter as tk


class TK():
    def __init__(self):
        
        
        self.conteur = 0
        
        self.Tab = tk.Tk()
        self.Tab.geometry("300x100")
        
        #imput Label 
        self.Label_POP3 = tk.Label(self.Tab, text="put OK POP3 server ready data here")
        self.Label_HASH = tk.Label(self.Tab, text="put Hash recover from pcap file")
        
        
        
        #imput Text_Area
        self.Text_Area_POP3ok = tk.Text(self.Tab,  height = 1)
        self.Text_Area_HASH = tk.Text(self.Tab,  height = 1)
        
        #imput Button
        self.Button_OK = tk.Button(self.Tab ,
                                   text = 'hello world', pady = 10, 
                                   command=lambda:[self.Get_Text_Input()])#, self.end()])
        #pack
        self.Label_POP3.pack()
        self.Text_Area_POP3ok.pack(side = tk.TOP)
        self.Label_HASH.pack()
        self.Text_Area_HASH.pack()
        self.Button_OK.pack(side = tk.BOTTOM)       
        #end of the Tk 
        
        self.Tab.mainloop()
        
        
    def end(self):
        self.Tab.destroy()
        
        
    def Get_Text_Input(self):
        self.result_POP3 = self.Text_Area_POP3ok.get(1.0, "end-1c")
        self.result_HASH = self.Text_Area_HASH.get(1.0, "end-1c")

        
    
    def Brute_Fore(self):
        
        #hash récupérer dans la tramme réseaux 
        #e3fc9b24b24a8ec4c68f5865763e553d
        #HashFinal = "4ddd4137b84ff2db7291b568289717f0"
        self.result_HASH
        
        #Part1 = "<1755.1.5f403625.BcWGgpKzUPRC8vscWn0wuA==@vps-7e2f5a72>"
        self.result_POP3
        
        
        #ouverture du fichier (test puis rockyou)
        with open("C:/Users/USER/Documents/challenge/rootme/réseaux/rockyou.txt", encoding='latin-1') as test:
            #lignes seras egal a une ligne du fichier
            #on fais atentions a virer les retour chariot 
            self.lignes = test.read().splitlines()
            
            
            for self.ligne in self.lignes:
                self.conteur += 1

                #concatenations de la poart1 et du mdp 
                self.AshIntermédiaire = self.result_POP3 + self.ligne
                
                self.aventRes = hashlib.md5(self.AshIntermédiaire.encode('utf-8')).hexdigest()
                
                #print(self.aventRes)
                if self.aventRes == self.result_HASH: 
                    self.final =  self.ligne
                    print("le mot de passe et :", self.ligne)
                    sys.exit
                    break
            
               

result = TK()
result.Brute_Fore()

