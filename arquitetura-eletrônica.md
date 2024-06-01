# Arquitetura de Eletrônica

A arquitetura de eletrônica começa pela função do projeto, será um sistema capaz de acionar a captura de larvas depositadas em um reservatório de água. Para isso a arquitetura utiliza os seguintes componentes: o microcontrolador Raspberry, sensor de temperatura, sensor de nível de água, GPS/SIM e câmera. Utiliza também atuadores eletrônicos: relés e bomba de aguá.

A Raspberry contem o _Firmware_ que irá controlar todo o sistema, ela foi escolhida pelo grande número de entradas GPIO que são utilizadas para receber dados e controlar os atuadores. Possui um poder de processamento considerável a ponto de poder processar localmente aprendizado de maquina que é uma opção considerável se for necessário fazer o processamento de imagem localmente. Outro motivo que levou à escolha da Raspberry é a sua capacidade de mudança do projeto se necessário, número de GPIOs e poder de processamento,possibilitando a escalabilidade do projeto.

Os sensores de temperatura, nível de água, GPS/SIM e câmera foram escolhidos modelos que utilizam comunicação digital, pois a Raspberry não possui entradas analógicas. Essa opção também evita o uso de conversores analógico-digital tornando o projeto menos complexo. Esses sensores é o que vão permitir um uso inteligente da armadilha e é o ponto forte do projeto, pois permite uma visão mais clara da proliferação de mosquitos a partir do envio e disponibilização desses dados pelos servidores em nuvem.

Os relés permitem uma operação autônoma das armadilhas, diminuindo assim a necessidade de trabalho manual e isso permite uma implementação mais eficiente da solução, evitando o problema de esquecimento do acionamento e manutenção da armadilha que é comum em casos como esse que exige uma atenção constante.

A baixo segue o diagrama de blocos simplificado da solução de eletrônica

![Arquitetura de Eletrônica](assets/images/diagrama-eletronico.png)

## Histórico de versões

| Versão | Alteração                                        | Data       | Autor         |
| ------ | ------------------------------------------------ | ---------- | ------------- |
| 1.0    | Criação do documento e explicação da arquitetura | 26/04/2024 | Gabriel Bacon |
| 2.0    | Atualização da arquitetura                       | 30/05/2024 | Gabriel e Jhéssica|
