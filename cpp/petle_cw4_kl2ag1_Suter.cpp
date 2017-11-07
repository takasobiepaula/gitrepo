/*
 * petle_cw4_kl2ag1_Suter.cpp
 */

#include <iostream>
using namespace std;
int main(int argc, char **argv)
{
	int liczba, suma;
	suma = 0;
	cout << " Podaj liczbę: " << endl;
	cin >> liczba;
	
	while(liczba < 0)
	{
		suma += liczba % 10;
		liczba = liczba / 10;
	}
	cout << "Suma cyfr : " << suma << endl;
	
	return 0;
}
