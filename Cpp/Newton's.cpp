//In this file I'll try implementing Newton's Rootfinding Algorithm.
//The Python implementation succeeded.
#include<iostream>
#include<cmath>

double x2_minus2(double m);
double x2_minus2(double m){
    return pow(m, 2) -2;
};

double d(double (*f)(double), double x);
double d(double (*f)(double), double x){
    float h = 0.1;
    double f_left = f(x-h);
    double f_right = f(x+h);
    return (f_right - f_left)/(2*h);
};

double newton(double (*func)(double), double x);
double newton(double (*func)(double), double x){
    double derv = d(func, x);
    return x - (func(x)/derv);
}

int main(){
    float abscissa;
    double step;
    std::cout << "Enter input to find derivative of function (x^2)-2 :  \n";
    std::cin >> abscissa;
    std::cout << "Derivative of f(x) = x^2 -2 at x = " << abscissa << "=" << d(x2_minus2, abscissa) << '\n';

    //Updating Newton's Step
    step = abs(abscissa - newton(x2_minus2, abscissa));
    //Updating the abscissa according to Newton's Step:
    abscissa = newton(x2_minus2, abscissa);

    //Printing the new abscissa:
    std::cout << "New X after Newton's Step is = " << abscissa << '\n';

    //Printing Newton's Step
    std::cout << "Newton's step = " << step;

    std::string next;
    std::cin >> next;

  //  do{


  //  }while(next == "");

    return 0;
}