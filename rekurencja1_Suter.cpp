/*
 * rekurencja1.cpp
 */


#include <iostream>

using namespace std;

int rek(int n)
{
    if (n == 1)
        return 1;
    else if (n == 2)
        return 2;
    return rek(n-1) + 2 * n + rek(n-2);
}
 
int main(int argc, char **argv)
{
    int n;
    cout << "Podaj wartość ciągu: " << endl;
    cin >> n;
    cout << "Wartość ciągu " << n << " wynosi: " << rek(n) << endl;
   
    return 0;
}

