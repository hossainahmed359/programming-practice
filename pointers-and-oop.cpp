#include<bits/stdc++.h>

using namespace std;

class Student {
    public:
        string name;
        int std_id;
        int age;
        string fathers_name;
        string mothers_name;
        
        void printInfo () {
            cout << name << "\n" << std_id << "\n" << age << "\n" << fathers_name << "\n" << mothers_name;
        }
};

class Nationality {
    public:
        string nationality;
};

class Person {
    public:
        string name;
        Nationality n;
        Person* father;
        
        void printInfo () {
            cout<<"Name: "<<name<<"\n";
            cout<<"Nationality: "<<n.nationality<<"\n";
            cout<<"Father's Name: "<<father->name<<"\n";
            cout<<"Father's Nationality: "<<father->n.nationality<<"\n";
        }
};


int main () {
    
    
    Person p;
    p.father = new Person;
    
    p.name = "Albert";
    p.n.nationality = "UK";
    
    p.father -> name  = "John";
    p.father -> n.nationality = "America";

    
    p.printInfo();
    
    return 0;
}
