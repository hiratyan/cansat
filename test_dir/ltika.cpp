#include <wiringPi.h>
#include <iostream>
using namespace std ;
int main(void){
	if (wiringPiSetupGpio() < 0){
		cout << "GPIO ERROR" << endl ;
		return 0 ;
	}
	const int pin = 2 ;
	pinMode(pin,OUTPUT) ;
	while(1){
		digitalWrite(pin, 1) ;
		delay(1000) ;
		digitalWrite(pin, 0) ;
		delay(1000) ;
	}
	return 0 ;
}
