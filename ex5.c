#include<stdlib.h>
#include<stdio.h>

int achaNumeroTriangular(int pos, int num_anterior); //Função que encontra o número de posição N utilizando o numero da posição N-1
int achaQtdDivisores(int num); //Função que acha o numero de divisores de um número


int main(){
    int divisores=0; //contador de divisores
    int pos_atual = 0; //posição atual a ser considerada
    int num_atual=0; //Numero triangular da posição atual
    while (divisores <500) // Realiza a operação ate o contador de divisores atinga 500 ou mais
    {   
    
    num_atual = achaNumeroTriangular(pos_atual,num_atual);
    divisores = achaQtdDivisores(num_atual);
    
    pos_atual++;
    }
    printf("\n resultado: %d\n",num_atual);    
}

int achaNumeroTriangular(int pos, int num_anterior){
    return pos+num_anterior;
}

int achaQtdDivisores(int num){
    int cont=0;
    for(int i=1;i<=num;i++){
    if(num%i==0){ //verifica se o resto da divisão é zero o que o caracteriza como divisor
        cont++;
    }
    }
    return cont;
}