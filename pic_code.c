#include "mcc_generated_files/mcc.h"
#include <string.h> 
#include <stdlib.h>
#include <stdio.h>
void clear (char* str){
    strcpy(str,"");
}
int read_input(char* str){
    unsigned char temp;
    int i = 0;
    int index = 0;
    char buffer[4];
    while (i < 4){
    if (EUSART_is_rx_ready())
    {
        
        temp=EUSART_Read();
        switch(temp)
        {
            case ';':
            case '\n':
         {
                strcpy(str,buffer);
                clear(buffer);
                i=0;
                return 0;
         //return buffer;
         }    
    
         default:{
                buffer[index++] = temp;
                i++;
            }
        }
    }}
        strcpy(str,buffer);
        clear(buffer);
        return 0;
        //return buffer;
                }
void main(void)
{
    // initialize the device
    SYSTEM_Initialize();
    while (1)
    {
    char sp[4];
    char f_kp[4];
    char f_ki[4];
    char f_kd[4];
    
    int i=0;
    while (i<5){
    switch(i){
        case 1: {
            read_input(sp);
            puts(sp);
            __delay_ms(200);
            //int spi = atoi(sp);
        }
        case 2:{
            read_input(f_kp);
            puts(f_kp);
            __delay_ms(200);
            //int f_kpi = atoi(f_kp);
        }
        case 3:{
            read_input(f_ki);
            puts(f_ki);
            __delay_ms(200);
            //int f_kii = atoi(f_ki);
        }
        case 4:{
            read_input(f_kd);
            puts(f_kd);
            __delay_ms(200);
            //int f_kdi = atoi(f_kd);
        }
        case 5:{
            printf("Run PID");
            __delay_ms(200);
        }
    }
    i++;
    }
    }
}
    // Add your application code
    
