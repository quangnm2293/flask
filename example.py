class Car:

     # thuộc tính đối tượng
    def __init__(self, tenxe, mausac, nguyenlieu):
        self.tenxe = tenxe
        self.mausac = mausac
        self.nguyenlieu = nguyenlieu

     # phương thức
    def dungxe(self, mucdich):
        return "{} đang dừng xe để {}".format(self.tenxe,mucdich)

    def chayxe(self):
        return "{} đang chạy trên đường".format(self.tenxe)

    def nomay(self): 
        return "{} đang nổ máy".format(self.tenxe)
    
    def chaybang(self):
        return "{} chay bang {}".format(self.tenxe, self.nguyenlieu)

class Lamborghini(Car):
    def __init__(self, tenxe, mausac, nguyenlieu, loaixe):
        super().__init__(tenxe, mausac, nguyenlieu)
        self.loaixe = loaixe
    
    def kieuxe(self):
        return "{} La loai xe {}".format(self.tenxe, self.loaixe)

    def dungxe(self, mucdich):
        return "{} đang dừng xe để mua {}".format(self.tenxe, mucdich)

# instantiate the Car class
toyota = Car("Toyota", "Đỏ", "Điện")
lamborghini = Car("Lamborghini", "Vàng", "Deisel")
porsche = Car("Porsche", "Xanh", "Gas")
v1 = Lamborghini("lamborghini", "vang", "deisel", "5 ngua")
d1 = Lamborghini("lamborghini", "do", "deisel", "15 ngua")
# call our instance methods
print(toyota.dungxe("nạp điện"))
print(lamborghini.chayxe())
print(porsche.nomay())
print(porsche.dungxe("say hello"))
print(lamborghini.chaybang())
print(toyota.chaybang())
print(porsche.chaybang())
print(v1.chayxe())
print(v1.dungxe("snack"))
print(v1.kieuxe())
print(d1.kieuxe())