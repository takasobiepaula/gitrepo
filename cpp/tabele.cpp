/*
 * tabele.cpp
 */


#include <iostream>
using namespace std;
void pobierzLiczby(int tab[], int ile){
    int i=0;
    for (i = 0; i < ile; i++) {
       cout << "Podaj liczbę: ";
       cin >> tab[i];
}

void sumuj(int tab[], int ile){
    int i=0;
    int suma=0;
    for(i=0, i<ile,i++){
        suma+=tab[i];
    }
    cout<<"suma liczb:"<<suma<<endl;
    
{
void najmniejsza (int tab[];int ile){
        int mini=tab[0];
        int i=0;
        for(i=0;i<mini;i++){
            if(mini>tab[i])
            mini=tab[i];
}
    cout<<"najmniejsza liczba:"<<mini<<endl;
}

void ile5(int tab[], int ile){
    for(i=0, i<ile,i++){
    if(tab[i] %5 ==0)
    licznik5++;
    int parzyste=0;
    if(tab[i]%2==0)
    parzyste++;
    }
    cout<<"Podzielne przez 5:"<<licznik5<<endl;

int main(int argc, char **atgv)
{
        int rozmiar =0;
        cout<<"ile liczb podasz?";
        cin>>rozmiar;
        int liczby[rozmiar];
        
        pobierzLiczby(liczby,rozmiar);
        sumuj(liczby,rozmiar;
        najmniejsza(liczby,rozmiar);
        return 0;
}
    


