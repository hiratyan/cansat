#include <stdio.h>
#include <stdint.h>
#include <wiringPi.h>
#include <wiringSerial.h>

int main(){
    /* シリアルポートオープン */
    int fd = serialOpen("/dev/ttyS0",9600);    
    
    wiringPiSetup();
    fflush(stdout);
    
    if(fd<0){
        printf("can not open serialport");
    }

    while(1){
    /* 受信処理 */
    while(serialDataAvail(fd)){
        int get_char =  serialGetchar(fd);
        if(get_char !=  -1){
            printf("recive : %d\n",get_char);
        }else{
            printf("no data\n");    
        }
    }
    }
    return 0;
}