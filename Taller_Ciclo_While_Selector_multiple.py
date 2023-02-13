'''

TALLER: CICLO MIENTRAS Y SELECTOR MÚLTIPLE

El Fondo de empleados del ITM ha decidido subsidiar una póliza de salud a sus asociados. El valor de la póliza es
el equivalente al 5% del Salario Básico del asociado. El valor subsidiado por el Fondo dependerá del estrato del
asociado así:
Estrato:
1. 50%
2. 40%
3. 30%
4. 20%
Otro. 10%
El programa debe mostrar a cada asociado:
a. El valor de la póliza
b. El valor que debe cubrir el asociado
c. El valor subsidiado por el Fondo
El programa debe mostrar un resumen al final indicando:
a. Cuantos subsidios se entregaron por cada estrato
d. El monto total por subsidios que debe desembolsar el Fondo
e. El promedio subsidiado por asociado (promedio general)


Datos de prueba

Asociado    Estrato     Salario     Valor Póliza    Valor Subsidio      Valor asociado

1               1     $ 1.200.000     $ 60.000          $ 30.000            $ 30.000
2               2     $ 1.500.000     $ 75.000          $ 30.000            $ 45.000
3               1     $ 1.300.000     $ 65.000          $ 32.500            $ 32.500
4               4     $ 2.800.000     $ 140.000         $ 28.000            $ 112.000
5               3     $ 2.100.000     $ 105.000         $ 31.500            $ 73.500
6               5     $ 3.200.000     $ 160.000         $ 16.000            $ 144.000
7               6     $ 3.800.000     $ 190.000         $ 19.000            $ 171.000
8               2     $ 2.000.000     $ 100.000         $ 40.000            $ 60.000

RESUMEN (Si el programa está bien deberá mostrar estor resultados al final)
Subsidios entregados por estrato:

1. 2
2. 2
3. 1
4. 1
Otro. 2

Total a desembolsar por subsidio: $227.000 
Promedio subsidiado por asociado: $28.375

'''

class Resultados:
    def __init__(self, Datos_suministrados):
        self.Datos_suministrados = Datos_suministrados

    def conteo_subsidios(self):

        cont_estrato_1 = 0
        cont_estrato_2 = 0
        cont_estrato_3 = 0
        cont_estrato_4 = 0
        cont_otros = 0
        j = 0

        while j < len(self.Datos_suministrados):
            if self.Datos_suministrados[j]["Estrato"] == 1:
                cont_estrato_1 += 1
            elif self.Datos_suministrados[j]["Estrato"] == 2:
                cont_estrato_2 += 1
            elif self.Datos_suministrados[j]["Estrato"] == 3:
                cont_estrato_3 += 1
            elif self.Datos_suministrados[j]["Estrato"] == 4:
                cont_estrato_4 += 1
            else:
                cont_otros += 1
            j+=1

        print("-------------------------------------------")
        print("\tSubsidios entregados por estrato".upper())
        print("-------------------------------------------")
        print(f"Estrato 1 = {cont_estrato_1}")
        print(f"Estrato 2 = {cont_estrato_2}")
        print(f"Estrato 3 = {cont_estrato_3}")
        print(f"Estrato 4 = {cont_estrato_4}")
        print(f"Otros = {cont_otros}")
        print("-------------------------------------------")




    def ValorPoliza(self):

        Valor_Poliza = 0.05
        estrato_1 = 0.5
        estrato_2 = 0.4
        estrato_3 = 0.3
        estrato_4 = 0.2
        otros_estratos = 0.1
        suma_desembolso=0
        promedio_subsidiado= 0
        i=0

        while i < len(self.Datos_suministrados):
            self.Datos_suministrados[i]["Valor Póliza"] = self.Datos_suministrados[i]['Salario'] * Valor_Poliza
            if self.Datos_suministrados[i]["Estrato"] == 1:
                self.Datos_suministrados[i]["Valor Subsidio"] = self.Datos_suministrados[i]["Valor Póliza"] * estrato_1
                self.Datos_suministrados[i]["Valor Asociado"] = self.Datos_suministrados[i]["Valor Subsidio"] - self.Datos_suministrados[i]["Valor Póliza"]
                if self.Datos_suministrados[i]["Valor Asociado"] < 0:
                    self.Datos_suministrados[i]["Valor Asociado"] *= -1
            elif self.Datos_suministrados[i]["Estrato"] == 2:
                self.Datos_suministrados[i]["Valor Subsidio"] = self.Datos_suministrados[i]["Valor Póliza"] * estrato_2
                self.Datos_suministrados[i]["Valor Asociado"] = self.Datos_suministrados[i]["Valor Subsidio"] - self.Datos_suministrados[i]["Valor Póliza"]
                if self.Datos_suministrados[i]["Valor Asociado"] < 0:
                    self.Datos_suministrados[i]["Valor Asociado"] *= -1
            elif self.Datos_suministrados[i]["Estrato"] == 3:
                self.Datos_suministrados[i]["Valor Subsidio"] = self.Datos_suministrados[i]["Valor Póliza"] * estrato_3
                self.Datos_suministrados[i]["Valor Asociado"] = self.Datos_suministrados[i]["Valor Subsidio"] - self.Datos_suministrados[i]["Valor Póliza"]
                if self.Datos_suministrados[i]["Valor Asociado"] < 0:
                    self.Datos_suministrados[i]["Valor Asociado"] *= -1
            elif self.Datos_suministrados[i]["Estrato"] == 4:
                self.Datos_suministrados[i]["Valor Subsidio"] = self.Datos_suministrados[i]["Valor Póliza"] * estrato_4
                self.Datos_suministrados[i]["Valor Asociado"] = self.Datos_suministrados[i]["Valor Subsidio"] - self.Datos_suministrados[i]["Valor Póliza"]
                if self.Datos_suministrados[i]["Valor Asociado"] < 0:
                    self.Datos_suministrados[i]["Valor Asociado"] *= -1
            else:
                self.Datos_suministrados[i]["Valor Subsidio"] = self.Datos_suministrados[i]["Valor Póliza"] * otros_estratos
                self.Datos_suministrados[i]["Valor Asociado"] = self.Datos_suministrados[i]["Valor Subsidio"] - self.Datos_suministrados[i]["Valor Póliza"]
                if self.Datos_suministrados[i]["Valor Asociado"] < 0:
                    self.Datos_suministrados[i]["Valor Asociado"] *= -1

            suma_desembolso+= self.Datos_suministrados[i]["Valor Subsidio"]
            i+=1

        promedio_subsidiado = suma_desembolso/(len(self.Datos_suministrados))

        k=0

        print("-------------------------------------------")
        print("\ttabla general".upper())
        print("-------------------------------------------")
        while k < len(self.Datos_suministrados):
            print("-------------------------------------------")
            print(f"\tasociado {k+1}".upper())
            print("-------------------------------------------")
            print("Estrato : ", self.Datos_suministrados[k]["Estrato"])
            print("Salario : $", self.Datos_suministrados[k]["Salario"])
            print("Valor Póliza : ", self.Datos_suministrados[k]["Valor Póliza"])
            print("Valor Subsidio : ", self.Datos_suministrados[k]["Valor Subsidio"])
            print("Valor Asociado : ", self.Datos_suministrados[k]["Valor Asociado"])
            print("-------------------------------------------")

            k+=1

        #print(self.Datos_suministrados)
        print()
        print(f"Total a desembolsar por subsidio: $ {suma_desembolso}")
        print(f"Promedio subsidiado por asociado: $ {promedio_subsidiado}")

Datos_suministrados =[

    {
        "Estrato": 1,
        "Salario": 1200000
    },

    {
        "Estrato": 2,
        "Salario": 1500000
    },

    {
        "Estrato": 1,
        "Salario": 1300000
    },

    {
        "Estrato": 4,
        "Salario": 2800000
    },

    {
        "Estrato": 3,
        "Salario": 2100000
    },

    {
        "Estrato": 5,
        "Salario": 3200000
    },

    {
        "Estrato": 6,
        "Salario": 3800000
    },

    {
        "Estrato": 2,
        "Salario": 2000000
    }

]

datos = Resultados(Datos_suministrados)
datos.conteo_subsidios()
datos.ValorPoliza()

