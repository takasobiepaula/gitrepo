/*
 * algorytm2.cpp
 */


#include <iostream>
#include <cstdlib>
 
using namespace std;
 
int main()
{
    int ilosc, liczba;
 
    cout << "Podaj ilość liczb: ";
    cin >> ilosc;
    cout << endl;
 
    for (int i = 0; i < ilosc; i++)
    {
        cout << "Podaj liczbe " << i +1 << ": ";
        cin >> liczba;
    }
 
    int n;
    n = 0;
    while(n <= ilosc)
    {
        if(liczba%2 == 0)
        {
            cout << "Liczby parzyste: " << liczba << endl;
                }           
            else if(liczba%2 == 1)
            {
                cout << "Liczby nie parzyste: " << liczba << endl;
 
            }
 
    break;  
    };

}
