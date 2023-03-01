# Chain Of Responsibility
> Feito por **Gabriel Dos Santos Lima - 2115310010**

O **Chain of Responsibility** é um padrão de projeto
comportamental que permite que você passe pedidos por uma
corrente de handlers. Ao receber um pedido, cada handler
decide se processa o pedido ou o passa adiante para o próximo
handler na corrente.

> Fonte: Mergulho nos padrões de projeto, de Alexander Shvets

O código para implementação dos _handlers_ segue a seguinte estrutura:

<img width="500" src="./structure.jpg"/>

Cada _handler_ deve, ou processar a _request_ ou passar a mensagem adiante formando uma cadeia de
tratativas.
