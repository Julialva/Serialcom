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
    char buffer[4]="";
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
int count = 0;
char s[4];
int num;
int adc;
void main(void)
{
    // initialize the device
    SYSTEM_Initialize();
    int count = 0;
    LADO1_SetHigh();
    LADO2_SetLow();
    while (1)
    {
        
    read_input(s);
    //puts(s);
    __delay_ms(1000);
    num = atoi(s);
    //printf("%i\n",num);
    //loads pwm value to motor
    PWM3_LoadDutyValue(num);
    count = 0;
    //printf("%i\n",num);
    // Reads adc 100 times than expects next input
    while (count <=20){       
            ADC_SelectChannel(TACO);
            ADC_StartConversion();
            adc = ADC_GetConversionResult();
            printf("%i\n",adc);
            __delay_ms(200);
            count++;
    }    
    }
}
    
