

def Introducao():
    idade1 = 39;
    idade2 = 30;
    idade3 = 27;
    idade4 = 18;

    print(idade1);
    print(idade2);
    print(idade3);
    print(idade4);

    idades = [idade1, idade2, idade3, idade4];

    print(f"Tamanho da lista: {len(idades)}");

    idades.append(27);
    idades.append(32);
    idades.remove(27);
    idades.pop(1);
    idades.insert(1, 99);

    for i in idades:
        print(i);

    idadesAnoQueVem = [(i+1) for i in idades];

    print(idadesAnoQueVem);
    

class ContaCorrente:

    def __init__(self, codigo) :
        self.codigo = codigo;
        self.saldo = 0;

    def deposita(self, valor):
        self.saldo += valor;

    def __str__(self) -> str:
        return "[>>Código: {}; Saldo: {}<<]".format(self.codigo, self.saldo)

    def __repr__(self) -> str:
        return " ( >>Código: {}; Saldo: {}<< ) ".format(self.codigo, self.saldo)



