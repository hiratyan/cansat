#include <stdio.h>
#include <wiringPi.h>
#include <wiringSerial.h>
#include <termios.h>

int main() {
    int fd;
    struct termios ttyparam;
    fd = serialOpen("/dev/ttyAMA0", 9600);

    tcgetattr(fd, &ttyparam);

    ttyparam.c_iflag &= ~IXON;
    ttyparam.c_iflag &= ~IXOFF;
    ttyparam.c_iflag &= ~CSIZE;
    ttyparam.c_iflag |= CS8;

    tcsetattr(fd, TCSANOW, &ttyparam);
    serialFlush(fd);

    while('1'){
        putchar(serialGetchar(fd));
    }
    serialClose(fd);
    return 0;
}
