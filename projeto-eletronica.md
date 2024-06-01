O projeto de eletrônica lista e explica o uso de componentes relacionados ao sistema de telemetria e controle da solução.

## **Raspberry pi 3 +B**

![Raspberry](assets/images/raspberry-pi-3b.png)

A Raspberry foi escolhida porque é um computador de placa única, significa que implementa todos os componentes de forma pequena e eficiente apesar de ter a capacidade de funcionalidades de um computador completo com processador, memoria ram e placa de video. Dessa forma é capaz de processar informações e utilizar um sistema operacional embarcado comum Linux de fácil implementação que facilita a realização do projeto.

O tamanho e o fato de ser um computador feito e projeto por uma única empresa também significa que possui uma integração bem otimizada e nesse caso um consumo energético pequeno. O projeto pode utilizar isso pois visa um dispositivo que possa funcionar sem intervenção humana por muitos dias. O baixo consumo então permite o uso racional da energia fornecida pela bateria.

O computador Raspberry também permite conexão WiFi que é essencial para o projeto além da implementação de um modem GSM para ambientes sem internet local. O numero de GPIOs também foi importante para a escolha da Raspberry que possui 40 pinos GPIO e como os dispositivo utiliza muitos sensores e atuadores, esse número atendeu a todas as demandas e ainda tem pinos sobrando para mudanças no futuro do projeto.

| Parâmetros                             | Especificações                                                        |
| -------------------------------------- | --------------------------------------------------------------------- |
| Tensão de entrada                      | 5 V (entrada)                                                         |
| Processador                            | Broadcom BCM2837B0 quad-core Cortex-A53 de 64 bits                    |
| Velocidade do Processador              | 1,4 GHz                                                               |
| Memória RAM                            | 1 GB LPDDR2                                                           |
| GPIOs                                  | 40 pinos                                                              |
| Entradas Conversoras Analógica/Digital | A Raspberry Pi 3 B+ não possui conversores analógico/digital internos |
| UART                                   | 1 UART                                                                |

## **Webcam C925e**

![webcam_C925e](assets/images/webcam-C925e.png)

Essa webcam foi escolhida pois o grupo já a possuía. O fato de utilizar uma resolução baixa de 1080p, não atrapalha pois um produto final comercial utilizaria uma camera de resolução proxima e melhor custo beneficio. Logo a imagem não sendo a melhor possível mas suficiente é perfeito para implementar o reconhecimento de imagens e testar suas capacidades para esse cenário. O reconhecimento de número de larvas pela camera não deve ser tão difícil quanto outras situações como reconhecimento de placas de carros ou facial, isso porque a imagem será sempre a mesma e com a luz controlada. A imagem será checada para questão de luminosidade e caso necessário será desligado ou ligado os LED.

## **Relé JQC3F Temporizador Digital Ajustável**

![webcam_C925e](assets/images/reles.png)

Esse dispositivo temporizador e modelo de relé foi escolhido pois possui um sistema integrado que permite a temporização individual sem estar sob o controle da Raspberry, isso é necessário para ligar e desligar a Raspberry que não possui essa função nativa, apenas ligando no momento que é fornecido tensão na entrada de 5V da mesma. Dessa forma será evitado que a Raspberry fique ligada no momento que não tem operações sendo realizadas e menor custo energético para o projeto. Esse relé pode ser alimentado diretamente pela bateria de 24v e isso facilita a implementação. 

## **Módulo Rele 2 canais com optoacoplador**

![webcam_C925e](assets/images/rele.png)

Esse Módulo Relé possui 2 reles de 1 canal 5V com interface padrão TTL, que pode ser controlado diretamente por diversos Microcontroladores (Arduino, 8051, AVR, PIC, DSP, ARM, ARM, MSP430, Raspberry).
O modulo tem proteção do optoacoplador 817C para previnir danos ao microcontrolador ou placa de desenvolvimento.
Através deste módulo é possível controlar vários aparelhos e equipamentos de alta corrente.
No projeto serão utilizado dois relés desse modelo, que serão operados pela raspberry, um para controlar a bomba e o outro para realizar o acionamento dos LEDs.

## **Bomba de água 22w 800l/h 24v Dc**

![webcam_C925e](assets/images/bomba.png)

Essa bomba foi escolhida por apresentar a tensão de operação correta para o projeto. O fluxo de água que é possível movimentar também é importante pois é necessário um fluxo alto para garantir que nenhuma larva fique no reservatório superior e seja descartada. Uma bomba de aquário pequena de 12V consegue realizar um fluxo de 200L/h enquanto essa bomba consegue 4x com um valor de 800L/h e ainda está dentro do que é possível ser operado pelo conjunto de baterias. O consumo de energia é importante mas o período de utilização será pequeno de apenas alguns segundo deixando o consumo baixo.

## **Sensor de nível de água horizontal tipo boia**

![webcam_C925e](assets/images/nivel.png)

O sensor foi escolhido por ser uma solução prática e simples para controlar o nível de água do reservatório inferior. O controle de nível no reservatório inferior é necessário para evitar que a bomba de água opere em vazio e sofra danos. Esse sensor é utilizado para controle de nível em aquários, tanques, recipientes de enchimento entre outros. Quando o líquido chega a um determinado nível, é acionado uma chave, que é utilizado para enviar a informação do nível do liquido a um dispositivo. Esse sensor é compatível com a maioria dos microcontroladores do mercado como PIC, Arduino e Raspberry.

## **Sensor de temperatura Ds18b20**

![webcam_C925e](assets/images/sensortemp.png)

O sensor foi escolhido pois utiliza uma interface presente na Raspberry, interface de comunicação de fio único que normalmente é utilizada no GPIO 4. Essa interface é extremamente simples e fácil de implementar. Esse dispositivo também apresenta uma faixa de operação muito boa entre -55 C° e +125 C°, como é esperado que o sistema opere entre 5 e 30° então está corretamente especificado. O sensor confirma a temperatura da água para pesquisadores que queiram esse dado, mas também para controle da temperatura do reservatório superior. Isso é necessário para que a água esteja em temperatura adequada para as larvas e isso leve a mais mosquitos depositarem ali.

## Histórico de versões

| Versão | Alteração                           | Data       | Autor              |
| ------ | ----------------------------------- | ---------- | ------------------ |
| 1.0    | Criação do documento e seu conteúdo | 26/04/2024 | Gabriel e Jhessica |
| 2.0    | Atualização do documento            | 30/05/2024 | Jhessica           |
