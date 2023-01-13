from typing import Any

class Product1:
    def __init__(self) -> None:
        self.parts = []
        
    def add(self,part:Any) -> None:
        self.parts.append(part)
        
    def list_parts(self)->None:
        print(f"Części produktu(Product1): {', '.join(self.parts)}",end="")
