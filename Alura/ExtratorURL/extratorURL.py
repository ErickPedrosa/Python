import re


class Extrator_url:
    
    DOLAR = 5.50
    
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")
        
        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(url)
        if not match:
            raise ValueError("A URL não é válida.")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base
    
    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[(indice_interrogacao + 1):]
        return url_parametros
    
    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)

        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find("&", indice_valor)

        if indice_e_comercial == -1:
            
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
            
        return valor
    
    def converte(self):
        moeda_origem = self.get_valor_parametro('moedaOrigem')
        moeda_destino = self.get_valor_parametro('moedaDestino')
        quantidade = self.get_valor_parametro('quantidade')
        
        if(moeda_origem == 'dolar' and moeda_destino == 'real'):
            return (f"{float(quantidade) * self.DOLAR} {moeda_destino}")
        elif(moeda_origem == 'real'and moeda_destino == 'dolar'):
            return (f"{float(quantidade) / self.DOLAR} {moeda_destino}")
        else:
            raise ValueError("Parâmetros insuficientes para a conversão.")
    
    def __len__(self):
        return len(self.url)
        
    def __str__(self):
        return str(self.url)
    
    def __repr__(self):
        return (f"URL: {self.url}\nBase: {self.get_url_base()}\nParâmetros: {self.get_url_parametros()}")
    
    def __eq__(self, obj):
        return self.url == obj.url
        
url = "https://bytebank.com/cambio?moedaDestino=real&moedaOrigem=dolar&quantidade=100"
extrator_url = Extrator_url(url)
extrator_url2 = Extrator_url(url)

print(f"\nTamanho da url: {len(extrator_url)}")
print(repr(extrator_url))
print(f"\n{extrator_url == extrator_url2}")
print(extrator_url.converte())

# valor_quantidade = extrator_url.get_valor_parametro("quantidade")
# print(valor_quantidade)

