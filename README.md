Consulta de Países - API RestCountries (Tkinter)

Este projeto é um sistema de consulta de países em Python com interface gráfica Tkinter, utilizando a API RestCountries v3.1.
Permite pesquisar informações sobre qualquer país de forma rápida e visual.

🚀 Funcionalidades

Pesquisa por nome ou parte do nome do país.

Exibe informações detalhadas:

Nome

Capital

Moeda(s)

Idioma(s)

Continente

População

Sigla (CCA2)

Botões de ação:

Listar Países → lista todos os países encontrados.

Capitais → mostra as capitais.

Moedas → mostra as moedas.

Idiomas → mostra os idiomas oficiais.

Contar Países → quantidade de países encontrados.

Validação de entrada: avisa se o campo estiver vazio.

Trata países sem capital, moeda ou idioma registrado.

💻 Tecnologias

Python 3

Tkinter (interface gráfica)

Requests (requisições HTTP)

🔗 API utilizada

RestCountries v3.1

Endpoint principal usado:

https://restcountries.com/v3.1/all?fields=name,capital,currencies,languages,region,population,cca2

📝 Como usar

Clone o repositório:

git clone https://github.com/Gabrielpalhanogomes2803/API-de-pa-ses.git
cd API-de-pa-ses


Instale a dependência:

pip install requests


Execute o programa:

python paises.py


Na interface:

Digite parte do nome do país.

Clique nos botões para consultar as informações desejadas.

📌 Observações

O programa carrega a lista de países uma vez para otimizar requisições.

A pesquisa é case-insensitive e aceita qualquer substring do nome do país.

Trata automaticamente países sem capital, moeda ou idioma registrado.
