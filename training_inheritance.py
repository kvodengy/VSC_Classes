class Widget():
    #властивості класа (в конструкторі)
    def __init__(self,title,x_num,y_num):
        self.title = title
        self.x_num = x_num
        self.y_num = y_num
    #методи
    def print_info(self):
        print("Напис: ", self.title)
        print("Розташування: ", self.x_num, self.y_num)

class Button(Widget):
    def __init__(self,title,x_num,y_num, is_clicked):
        super().__init__(title,x_num,y_num)
        self.is_clicked = is_clicked
    #доповнені властивості класа (в конструкторі)
    def click(self):
        self.clicked = True
        print("Ви зареєстровані")
    #нові методи

#створи екземпляр класа Button
button = Button("Брати участь", 100, 100, False)
button.print_info()
answer = input("Хочете зареєструватися? (так/ні): ")
if answer == "так":
    button.click()
if answer == "ні":
    print("А шкода!")

#якщо на питання «Хочете зареєструватися?» користувач відповів «так», то застосуйте метод click