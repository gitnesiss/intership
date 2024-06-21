import sys
from PyQt6.QtWidgets import QWidget, QApplication, QComboBox, \
    QFormLayout
from PyQt6.QtGui  import QColor
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.categories = {
            'Животные':['кошка', 'собака', 'попугай', 'слон'],
            'Цветы': ['ромашки', 'тюльпаны', 'нарциссы', 'розы'],
            'Цвета': ['red', 'orange', 'blue', 'purple']
        }
                           
        self.category_combobox  = QComboBox(self)
        
        self.item_combobox = QComboBox(self)

        self.category_combobox.currentTextChanged.connect(self.set_category)
        self.category_combobox.addItems(sorted(self.categories.keys()))
        
        self.item_combobox.currentTextChanged.connect(self.set_item)   

        form_layout = QFormLayout(self)
        form_layout.addRow('Category', self.category_combobox)
        form_layout.addRow('Items', self.item_combobox)

    def set_category(self, text):
        print(f"set_category -> {text}")
        self.item_combobox.clear()
        self.item_combobox.addItems(self.categories.get(text, []))

        if text == 'Цвета':
            for i, color in enumerate( self.categories['Цвета'] ):
                self.item_combobox.setItemData(i, QColor(color), Qt.BackgroundRole)
        
    def set_item(self, text):
        if text:
            print(f"set_item -> {text}")
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.resize(300, 200)
    w.show()
    sys.exit(app.exec())