/*
 * nieparzyste.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    cout << "Podaj n:" << endl;
    int n;
    cin >> n;
        for ( int i = 1; i < n ; i = i + 2)
            cout << i << " " ;
	return 0;
}

