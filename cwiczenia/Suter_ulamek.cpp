/*
 * Suter_ulamek.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int licznik,mianownik,i;
    cout << "Podaj licznik: ";
    cin >> licznik;
    cout << "Podaj mianownik: ";
    cin >> mianownik;
    st:
    for (i=mianownik; i>1; i--)
    {
        if (licznik % i == 0)
    {
        if (mianownik % i == 0)
        {
            licznik=licznik/i;
            mianownik=mianownik/i;
   
}}
}
   return 0
} 
