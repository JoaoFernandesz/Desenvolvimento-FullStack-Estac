Algoritmo "N?meros primos"
// Tutor        : Andre Przewodowski Filho
// Fun??o       : dado um n?mero primo, retorna todos os n?meros primos menores que esse e a soma de todos esses
// Autor(a)     : Jo?o Victor Macedo Fernandes Ramos



Var
   i, numeros, primo, divisores, divisoresPrimo, soma:inteiro

Inicio
escreva("Digite um n?mero:")
leia(primo)

para numeros de 2 at? primo faca
      se (primo mod numeros=0)entao
        divisoresPrimo<-divisoresPrimo+1
      fimse
      fimpara
se (divisoresPrimo=1)entao
      para i de 1 at? primo faca
         divisores<-0
         para numeros de 1 at? i faca
          se(i mod numeros=0)entao
            divisores<-divisores+1
          fimse
           numeros <-numeros+1
         fimpara
         se(divisores=2)entao
            escreval("o numero", i, " ? primo")
            soma<-soma+i
         fimse
         fimpara

         escreva("a soma de todos os n?meros primos menores ou iguais a ", soma, " ?:")

senao
     escreva("inserir um n?mero primo")

fimse

Fimalgoritmo
