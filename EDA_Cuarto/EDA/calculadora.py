import flet as ft
import math

class Circulo:
    def __init__(self) -> None:
        pass
    def CalcularArea(self, radio):
        return 3.1416*math.pow(radio,2)
    def CalcularPerimetro(self, radio):
        return 3.1416*(radio+radio)
    
class Cuadrado:
    def __init__(self) -> None:
        pass
    def CalcularArea(self, lado):
        return lado*lado
    def CalcularPerimetro(self, lado):
        return lado*4
    
class Rectangulo:
    def __init__(self) -> None:
        pass
    def CalcularArea(self, base, altura):
        return base*altura
    def CalcularPerimetro(self, base, altura):
        return (base*2)+(altura*2)

class Triangulo:
    def __init__(self) -> None:
        pass
    def CalcularPerimetro(self, ladoA, ladoB, ladoC):
        return ladoA+ladoB+ladoC
    def CalcularArea(self, ladoA,ladoB, ladoC):
        semiP= self.CalcularPerimetro(ladoA, ladoB, ladoC)/2
        return math.sqrt(semiP*(semiP-ladoA)*(semiP-ladoB)*(semiP-ladoC))
         

def main(page: ft.Page):
    # add/update controls on Page
    def EventoClick(e):
        page.controls.pop(2)
        areaCirculo= str(circulo.CalcularArea(float(textRadio.value)))
        perimetriCirculo= str(circulo.CalcularPerimetro(float(textRadio.value)))
        areaCuadrado= str(cuadrado.CalcularArea(float(textLado.value)))
        perimetroCuadrado=str(cuadrado.CalcularPerimetro(float(textLado.value)))
        areaRectangulo= str(rectangulo.CalcularArea(float(textBase.value), float(textAltura.value)))
        perimetroRectangulo= str(rectangulo.CalcularPerimetro(float(textBase.value), float(textAltura.value)))
        areaTriangulo= str(triangulo.CalcularArea(float(textLadoA.value), float(textLadoB.value), float(textLadoC.value)))
        perimetroTriangulo= str(triangulo.CalcularPerimetro(float(textLadoA.value), float(textLadoB.value), float(textLadoC.value)))

        page.add(
            ft.Column([
                ft.Text(f"area del circulo: {areaCirculo}"),
                ft.Text(f"perimetro del circulo: {perimetriCirculo}"),
                ft.Text(f"area del cuadrado: {areaCuadrado}"),
                ft.Text(f"perimetro del cuadrado: {perimetroCuadrado}"),
                ft.Text(f"area del rectangulo: {areaRectangulo}"),
                ft.Text(f"perimetro del rectangulo: {perimetroRectangulo}"),
                ft.Text(f"area del triangulo: {areaTriangulo}"),
                ft.Text(f"perimetro del triangulo: {perimetroTriangulo}")
            ])
        )
        
    circulo=Circulo()
    cuadrado=Cuadrado()
    rectangulo=Rectangulo()
    triangulo=Triangulo()


    TCirculo= ft.Text("datos del circulo")
    TCadrado= ft.Text("datos del cuadrado")
    TRectangulo= ft.Text("datos del rectangulo")
    TTriangulo= ft.Text("datos del triangulo")
    textRadio = ft.TextField(label="radio", bgcolor='#808080')
    textLado = ft.TextField(label="lado", bgcolor='#808080')
    textBase= ft.TextField(label="base", bgcolor='#808080')
    textAltura= ft.TextField(label="altura", bgcolor='#808080')
    textLadoA= ft.TextField(label="lado a", bgcolor='#808080')
    textLadoB= ft.TextField(label="lado b", bgcolor='#808080')
    textLadoC= ft.TextField(label="lado c", bgcolor='#808080')
    Button = ft.ElevatedButton("calcular", on_click=EventoClick, bgcolor=ft.colors.AMBER)
    page.add(ft.Row ([ft.Column ([TCirculo, textRadio],width=300),ft.Column ([TCadrado ,textLado],width=300),ft.Column ([TRectangulo,textBase, textAltura],width=300),ft.Column ([TTriangulo, textLadoA, textLadoB, textLadoC],width=300)], height=300), Button, ft.Text())



ft.app(target=main)