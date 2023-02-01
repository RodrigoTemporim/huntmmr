import xml.etree.ElementTree as ET
from tkinter import *
import tkxui

# tree = ET.parse('attributes.xml')
# root = tree.getroot()
# nick = input('Digite seu nick\n')

#screen config
screen = tkxui.Tk()
screen.geometry('570x400')+str(screen.center())


# ico / title
screen.title('Hunt MMR')
screen.iconbitmap('hunticon.ico')

#Background
bgimag = PhotoImage(file='background.png')
my_label = Label(screen, image=bgimag)
my_label.place(x=0, y=0, relwidth=1, relheight=1, )

#texts
label_up = Label(screen, text='Hunt MMR System', font=('Helvetica', 25), fg='white', bg='black')
label_up.pack(pady=0, fill=X)
screen.mainloop()




# NameMMR = ''
# mmr = ''
# NamePlayer = ''


# for child in root:
#     values = child.attrib.get('value')
#     name = child.attrib.get('name')     
#     if nick in (values):          
#         NamePlayer = values  
#         NameMMR = name.replace('blood_line_name', 'mmr')        
#     if name == NameMMR:
#         mmr = child.attrib.get('value')            
# if NamePlayer != '': 
#     print('Nick do Player {} '.format(NamePlayer))           
#     print('MMR Atual : {} \nO MMR atualiza em algumas partidas!!'.format(mmr))
# else: 
#     print("----------------------\nNick não encontrado!")
   
 
       


    

        
    
    
        
            