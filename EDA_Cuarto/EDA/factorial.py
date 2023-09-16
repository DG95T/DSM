
import flet as ft

class Calculadora:
    def __init__(self) -> None:
        pass

    def Factorial(self, n):
        if(n<=1):
            return 1
        if(n>1):
            return n*self.Factorial(n-1)

    def Fib(self, n):
        result=0
        if(n==1):
            result= 1
        if(n>1):
            result= self.Fib(n-1)+ self.Fib(n-2)
        return result

    def MCD(self, a, b):
        if (b==0):
            return a
        return self.MCD(b, a % b)

def main(page: ft.Page):

    def Eventoclick(e):
        page.controls.pop(2)
        fac= str(calculadora.Factorial(float(textFact.value)))
        fib= str(calculadora.Fib(float(textFib.value)))
        mcd= str(calculadora.MCD(float(textMCD.value), float(textMCDA.value)))

        page.add(
            ft.Column([
                ft.Text(f"el factorial es de: {fac}"),
                ft.Text(f"el resultado de la serie fibonacci es de: {fib}"),
                ft.Text(f"el Maximo comun divisor es de: {mcd}")
            ])
        )
    
    calculadora=Calculadora()

    Tfact = ft.Text("inserta un numero")
    Tdef = ft.Text("inserta un numero")
    TMCD = ft.Text("inserta dos numeros")
    textFact = ft.TextField(label="factorial")
    textFib = ft.TextField(label="fibonacci")
    textMCD = ft.TextField(label="numero A")
    textMCDA = ft.TextField(label="numero B")
    boton = ft.ElevatedButton("calcular", on_click=Eventoclick)
    page.add(ft.Row([ft.Column([Tfact, textFact],width=300), ft.Column([Tdef, textFib],width=300), ft.Column([TMCD, textMCD, textMCDA],width=300)], height=200), boton, ft.Text())

ft.app(target=main)