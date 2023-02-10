from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QGraphicsLineItem
from PyQt5.QtGui import QBrush, QColor, QPainter, QPen
from PyQt5.QtCore import QRectF, QLineF



class MusicNotesApp(QMainWindow):
   
    FA=200
    SOL=175
    LA=150
    SI=125
    DO=100
    RE=75
    MI=50
    FA2=25

    def Noire(self,note_size):
        note1 = QGraphicsEllipseItem(QRectF(100, self.DO, note_size, note_size))
        note1.setBrush(QBrush(QColor(0, 0, 0)))
        self.scene.addItem(note1)
        
        line_note = QGraphicsLineItem(QLineF(100+50, self.SOL+30, 150, 50))
        line_note.setPen(QPen(QColor(0, 0, 0)))
        self.scene.addItem(line_note)
        
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 500)

        # Initialise la scène
        self.scene = QGraphicsScene()

        # Définit la couleur du fond de la fenêtre
        background_color = QColor(255, 255, 255)
        self.scene.setBackgroundBrush(QBrush(background_color))

        # Définit la couleur des notes
        note_color = QColor(0, 0, 0)

        # Définit la taille des notes
        note_size = 50

        # Dessine les notes 
        note1 = QGraphicsEllipseItem(QRectF(100, self.SOL, note_size, note_size))
        note1.setBrush(QBrush(note_color))
        self.scene.addItem(note1)
        line_note = QGraphicsLineItem(QLineF(100+50, self.SOL+30, 150, 50))
        line_note.setPen(QPen(QColor(0, 0, 0)))
        self.scene.addItem(line_note)

        note2 = QGraphicsEllipseItem(QRectF(200, self.RE, note_size, note_size))
        note2.setBrush(QBrush(note_color))
        self.scene.addItem(note2)

        note3 = QGraphicsEllipseItem(QRectF(300, self.FA , note_size, note_size))
        note3.setBrush(QBrush(note_color))
        self.scene.addItem(note3)
        
        
        # Définit la couleur des lignes
        line_color = QColor(0, 0, 0)

        # Définit l'épaisseur des lignes
        line_width = 1
        
        # Dessine les lignes
        line_pen = QPen(line_color)
        line_pen.setWidth(line_width)

        line1 = QGraphicsLineItem(QLineF(0, 50, 500, 50))
        line1.setPen(line_pen)
        self.scene.addItem(line1)

        line2 = QGraphicsLineItem(QLineF(0, 100, 500, 100))
        line2.setPen(line_pen)
        self.scene.addItem(line2)

        line3 = QGraphicsLineItem(QLineF(0, 150, 500, 150))
        line3.setPen(line_pen)
        self.scene.addItem(line3)
        
        line4 = QGraphicsLineItem(QLineF(0, 200, 500, 200))
        line4.setPen(line_pen)
        self.scene.addItem(line4)
        
        line5 = QGraphicsLineItem(QLineF(0, 250, 500, 250))
        line5.setPen(line_pen)
        self.scene.addItem(line5)

        # Initialise la vue
        self.view = QGraphicsView(self.scene)
        self.view.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(self.view)
        self.show()


app = MusicNotesApp()
