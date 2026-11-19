# Como publicar o portal (GitHub Pages)

Copie estes arquivos para a raiz do repositório `pi_fisica_extensiva`, mantendo a estrutura:

```
index.html                  <- portal (substitui o atual)
ADO_01/web/index.html + app.py
ADO_02/web/index.html + app.py
ADO_03/web/index.html + app.py
```

As pastas `ADO_0X` já existem no repositório; basta adicionar a subpasta `web/` dentro de cada uma.
Os seus arquivos originais (.py, notebooks, relatórios) não são alterados.

Depois: Settings -> Pages -> Branch `main`, pasta `/ (root)` -> Save.
Endereços finais:

- Portal: https://gustavfreitas.github.io/pi_fisica_extensiva/
- ADO 01: .../pi_fisica_extensiva/ADO_01/web/
- ADO 02: .../pi_fisica_extensiva/ADO_02/web/
- ADO 03: .../pi_fisica_extensiva/ADO_03/web/

## Testar no seu computador antes de publicar

Os apps usam fetch() para carregar o app.py, então não abra o HTML com duplo clique.
Na pasta do repositório rode:

    python -m http.server 8000

e abra http://localhost:8000/ no navegador.

Para rodar um app como Streamlit comum (sem stlite):

    pip install streamlit matplotlib numpy
    streamlit run ADO_01/web/app.py
