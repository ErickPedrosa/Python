from Introducao import ContaCorrente, Introducao;

print();

#Introducao();

c = ContaCorrente(15);
print(c);

c.deposita(500);
print(c);

c2 = ContaCorrente(47685);
c2.deposita(1000);
print(c2);

contas = (c, c2);
print(contas);



print();
