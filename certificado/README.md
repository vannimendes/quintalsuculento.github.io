# Emissão de certificados — Quintal Suculento

Página independente em `/certificado/`, preparada para a Oficina **Mãos à Terra de 16/11/2026**.

## Como usar

1. Publicar o PR no ramo `main` do repositório do site (GitHub Pages).
2. Distribuir **depois da oficina** o endereço `https://quintalsuculento.com.br/certificado/` e o código de acesso aos participantes.
3. Cada participante digita o código, confere seu nome na prévia e salva o certificado como PDF A4 horizontal.
4. Não são solicitados e-mail, telefone, cadastro ou dados de crianças além do nome que constará no certificado. O nome é processado no navegador e não é enviado a um servidor.

## Segurança e limites

- Esta é uma **emissão autodeclarada com código compartilhado**, não um sistema de validação individual de presença.
- O arquivo HTML é público. Mesmo com a comparação SHA-256, o bloqueio no navegador **não é autenticação** nem impede reutilização ou compartilhamento do código.
- Não há banco de dados, logs de emissão, verificação por CPF, número serial individual ou revogação de certificados.
- Se o evento exigir comprovação nominal, registrar os presentes previamente e usar códigos únicos validados em servidor, com política adequada de dados pessoais.

## Como adaptar para outra oficina

- Atualizar a data e o título na página (cabeçalho, composição do certificado e metadados).
- Definir um novo código aleatório (ex.: `QSC-XXXXX-XXXXX`).
- Atualizar a constante `EVENT` e o hash `DIGEST` calculado como SHA-256 da string `EVENT + ':' + codigo_normalizado`, sendo `codigo_normalizado` o código em maiúsculas, sem espaços e sem hífens.
- Conferir a arte e testar código incorreto/correto, nome com acentos, nome longo e PDF em iPhone/Android.
- Caso seja necessário manter históricos, criar páginas distintas por evento em vez de sobrescrever o certificado antigo.

## Implementação

- HTML, CSS e JavaScript nativos, sem serviços externos ou bibliotecas CDN.
- Preview A4 desenhado em Canvas de 2480 × 1754 pixels.
- Download de PDF A4 horizontal com uma imagem JPEG incorporada; é um PDF de imagem, não texto selecionável.
- Identidade visual por cores do Quintal e logomarca `../logo-cacto.webp`.
- A `index.html` da página inicial não foi alterada, preservando seu CRLF e o Tailwind reduzido.