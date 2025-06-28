# Cliente-DASH-adaptativo

Nesse trabalho de Redes de Computadores, implementei um Cliente Dash adaptativo, onde o código tem as capacidades:

1. De baixar o manifesto em um servidor local.
2. Medir a largura de banda real da rede com base no tempo de download de um segmento de vídeo de baixa qualidade (ex: 360p).
3. Escolher automaticamente a melhor representação (qualidade do vídeo) de acordo com a largura de banda disponível.
4. Baixar o segmento de vídeo escolhido.
5. Utilizar Wireshark para capturar os pacotes e validar:
   - O recebimento do manifesto
   - O segmento de vídeo transferido
   - O tempo de transferência do segmento

