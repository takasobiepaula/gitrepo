/*
 * sumuj2.cxx
 * Program pobiera liczby od użytkowniak aż ich suma nie przekroczy 100
 */


#include <iostream>
using namespace std;
int main(int argc, char **argv)
{
	//int i;
    int suma = 0;
    int liczba = 0;
    int ilosc = 0;
    cout<<" Wprowadzaj kolejne liczby: " << endl;
    //for (;;)
    while (1) // pętla nieskończona2
    {
        cin >> liczba;
        ilosc++;
        cout << " Podano:" << liczba << endl;
        suma += liczba;
        if (suma > 100)
            break;
    };
    cout << " Wprowadzono liczb: " <<ilosc<< endl;
    cout << "Suma liczb: " << suma << endl;
    
	return 0;
}

