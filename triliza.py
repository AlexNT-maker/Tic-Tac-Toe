from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QMainWindow, QLineEdit, QPushButton, QLabel, QTextEdit
from PyQt5.QtGui import QFont
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setStyleSheet("background-color:pink")
        self.setWindowTitle("trilling")
        self.setGeometry(500,60,1400,1400)
        self.label=QLabel(self)
        self.label.setText("Play")
        self.label.move(590,610)
        self.label.setStyleSheet("color:green")
       
        self.label_1=QLabel(self)
        self.label_1.setText("Be careful:Only x and o\n are valid options")
        self.label_1.move(10,0)
        self.label_1.setStyleSheet("color:red")
        self.label_1.resize(220,220)
        self.label_1.setFont(QFont("Arial", 8, QFont.Bold))
       
        self.check_button=QPushButton(self,text="Check")
        self.check_button.move(290,850)
        self.check_button.setStyleSheet("color:green")
        
        
        
        self.check_button.setToolTip("Press here to check the result")
        
        
        
        self.check_button.clicked.connect(self.x_or_o)
        
        self.clear_button=QPushButton(self,text="Clear")
        self.clear_button.move(290,890)
        self.clear_button.setStyleSheet("color:red")
        self.clear_button.setToolTip("Clear the board")
        
        self.clear_button.clicked.connect(self.reset)
        
        
        self.textboxes=[]
        positions = [(220, 398), (300, 398), (380, 398),  
                (220, 478), (300, 478), (380, 478), 
                (220, 558), (300, 558), (380, 558)]  


        for pos in positions:
            textbox = QLineEdit(self)
            textbox.move(*pos)  
            textbox.resize(80, 80)
            self.textboxes.append(textbox)

        
     
      
        
        
        
        
    def x_or_o(self):        
        valid_inputs=["x","o",""]
        values=[box.text().strip().lower()for box in self.textboxes]
        
        if any(val not in valid_inputs for val in values):
            self.label.setText("Invalid input")
            return
        
        winning_combinations=[(0,1,2),(3,4,5),(6,7,8), (0,4,8),(1,4,7),(2,4,6),(0,3,6),
                              (2,5,8)]
        
        winner=None
        
        
        
        for a,b,c in winning_combinations:
            if values[a]!="" and values[a]==values[b]==values[c]:
                winner=values[a].strip().upper()
                self.label.setText(f"{winner} WON!")
                print(f"winner detected:{winner}")
                return
            
        if "" in values:
            self.label.setText("In progress...")
            return
        self.label.setText("Draw")
            
     
                
            
            
     
            
    def reset(self):
        for box in self.textboxes:
            box.clear()
        self.label.setText("Play")
        print("Board reset")
            
            
   
    
               
        
        
        
        
    
        
        
        
        
        
        
        self.show()
        

       
        
        

app=QtWidgets.QApplication(sys.argv)

window=MainWindow()

window.show()
sys.exit(app.exec())