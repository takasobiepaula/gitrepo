/*
 * funkcje.cpp
 */


#include <iostream>

using namespace std;

void sumuj(int a, int b) 
{
    cout << "Suma: " << a + b << endl; 
}

void odejmij(int a, int b) 
{
    cout << "Różnica: " << a - b << endl; 
}

void mnozenie(int a, int b) 
{
    cout << "Iloczyn: " << a * b << endl; 
}

void dzielenie(int a, int b) 
{
    cout << "Iloraz: " << a/b << endl; 
    
}
//sprawdz b
int main(int argc, char **argv)
{
	int a, b;
    cout <<"Podaj liczby: ";
    cin >>a >> b;
    
    sumuj(a, b);
    odejmij (a, b);
    mnozenie(a, b);
    dzielenie(a, b);
	return 0;
}

