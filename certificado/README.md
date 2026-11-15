# Certificado da Oficina Mãos à Terra — 16/11/2026

## Fluxo
A página `/certificado/` oferece código de acesso **SOMOS**, campo para nome, prévia no modelo oficial, download **PNG ou PDF A4 horizontal** e convite opcional para fotografar a plantinha e enviar ao WhatsApp do Quintal Suculento.

O nome é renderizado no próprio navegador sobre a linha do certificado, sem alterar a ilustração original. Não há banco de dados nem envio de nomes/fotos ao site.

## IMPORTANTE: imagem pendente antes do merge
A página carrega `certificado/modelo-certificado.jpg`. **Anexar na mesma branch esse arquivo binário com o certificado final fornecido por Giovanni (1024 × 768, proporção 4:3)** antes de fazer merge. A imagem não pôde ser enviada automaticamente pela integração textual do GitHub. O ZIP fornecido na conversa contém o JPEG original pronto para upload.

Não fazer merge enquanto essa imagem não constar na branch; sem ela a geração do certificado não funciona. O arquivo `index.html` do site principal, seu CRLF e Tailwind não foram alterados.

## WhatsApp
Número: **+55 71 98765-0501**.
Mensagem: **Olá Vanni e Anne! Participei da oficina Mãos à Terra e essa é a minha nova plantinha!**

O link `wa.me` prepara a conversa e o texto, mas **não consegue anexar uma foto automaticamente**. O compartilhamento nativo via `navigator.share({files, text})` permite selecionar WhatsApp e contato no celular quando suportado, porém não fixa destinatário e pode exigir colar a mensagem manualmente. A interface oferece ambos os caminhos.

## Privacidade / acesso
Código compartilhado no JavaScript não é autenticação nem comprovação individual de presença; divulgar após a oficina. Não são coletados nomes ou fotos pelo site. Para participantes menores, solicitar autorização do responsável antes do envio de imagens; preferir fotografar apenas a planta.

## Verificações antes de publicar
1. Conferir que `modelo-certificado.jpg` está presente na pasta `certificado/`.
2. Testar código errado e código SOMOS.
3. Conferir sobreposição do nome na linha e download PNG/PDF em iPhone e Android.
4. Conferir câmera/galeria e escolha de WhatsApp.
5. Gerar QR Code para `https://quintalsuculento.com.br/certificado/`.
6. Só então aprovar o PR e publicar pelo GitHub Pages.
