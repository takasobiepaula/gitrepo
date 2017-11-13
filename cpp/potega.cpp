/*
 * potega.cpp
 * a0 = 1
 * a1 = a
 * an = a*...*a(n-czynników) dla n zaw. N+ - {1}
 */


#include <iostream>

using namespace std;
 
float potega_it(float x, int n) {
    float wynik = 1;
    for(int i = 0; i< n; i++) {
        cout << i << endl;
        wynik = wynik*i;
    }
    return wynik;
}


int main(int argc, char **argv)
{
	// zadeklaruj zmienne
    // pobieranie od uzytkowanika podstawy i wykładnika
    float x = 0;
    int n = 0;
    cout << "Podaj podstawę: " << endl;
    cin >> x;
    cout << "Podaj wykładnik: " << endl;
    cin >> n;
    cout << "Potęga" << potega_it(x ,n) << endl;
    
	return 0;
}

