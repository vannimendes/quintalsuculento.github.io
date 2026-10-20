# CSS do site (Tailwind enxuto)

O site usa o **Tailwind 2.2.19**, mas em vez de carregar o arquivo completo (cerca de 2,8 MB),
carrega `tailwind.purged.css` (cerca de 14 KB), que contém só as classes que o `index.html` usa.

## Quando precisa gerar de novo

Sempre que o `index.html` passar a usar uma **classe do Tailwind nova** (por exemplo `bg-green-300`
ou `md:grid-cols-4`) que ainda não existia na página. Sem isso, a classe nova não terá efeito.
Mudar textos, imagens ou classes que já existem não exige nada.

## Como gerar de novo

1. Baixe o CSS completo e salve como `tailwind.min.css`:
   https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css
2. Na pasta do site, rode:

```
python3 tools/purge_tailwind.py caminho/para/tailwind.min.css index.html -o tailwind.purged.css
```

3. Troque o número em `tailwind.purged.css?v=...` no `index.html` (por exemplo, a data de hoje)
   para os navegadores baixarem a versão nova.
