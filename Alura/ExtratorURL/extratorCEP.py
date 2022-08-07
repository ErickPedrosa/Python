import re # Regular Expression - RegEx

endereco = "Rua Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

                                                                                # O ? indica uma expressão opcional.
#padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

busca = padrao.search(endereco)
if busca:
    cep = busca.group()

print(cep)
