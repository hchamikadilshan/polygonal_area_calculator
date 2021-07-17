class Rectangle:
    
    def __init__(self,width,height):
        self.width=width
        self.height=height
        
    def set_width(self,width):
        self.width=width
        
    def set_height(self,height):
        self.height=height
        
    def get_area(self):
        return (self.width*self.height)
    
    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture=""
            for i in range(self.height):
                for j in range(self.width):
                    picture += "*"
                picture+= "\n"
            return picture
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def get_amount_inside(self,polygon):
        area_of_outer=self.get_area()
        area_of_inner=polygon.get_area()
        polygons_inside=area_of_outer//area_of_inner
        return polygons_inside
        
class Square(Rectangle):
    
    def __init__(self,length):
        super().__init__(length,length)
        
    def set_side(self,new_length):
        super().set_height(new_length)
        super().set_width(new_length)
    
    def __str__(self):
        return f"Square(side={self.width})"