/*
 * iloczyn.cpp
 */
 
#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
int a;
int b;
int c;
int d;
a=1;
cout<<"Podaj liczbe wieksza od 0\n";
cin>>b;
do
{
cout<<"Podaj nastepna liczbe ";
cin>>c;
b*=c;
a++;
}
while (b<10000);
cout<<"Zostalo wprowadzonych "<<a<<" liczb\n";
cout<<"Iloczyn tych liczb wynosi "<<b<<endl;
system("PAUSE");
return EXIT_SUCCESS;
}
