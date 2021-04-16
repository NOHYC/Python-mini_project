#include "2450addr.h"

#include "option.h"

#include "libc.h"
//Function Declaration
void Key_Port_Init(void);

void Key_Get_Pressed_with_LED();

int Key_Get_Pressed();

int Key_Wait_Get_Pressed();

void Key_Wait_Get_Released();



//Function

void Key_Port_Init(void)
{

	/* GPFCON -Input Mode GPF[2:6] */

	/* YOUR CODE HERE */

    rGPFDAT &= ~(0x3f<<2);
	rGPFUDP &= ~(0x3ff <<4);
	rGPFUDP |= (0x2aa <<4);

	rGPFCON &= ~(0x3ff <<4);

	/* GPFCON, GPGCON - outputmode GPF7, GPG0 */
	rGPFDAT |= (0x1<<7);
	rGPGDAT |= 0x1;

	rGPFCON &= ~(0x3<<14);
	rGPGCON &= ~0x3;

	rGPFCON |= (0x1<<14);

	rGPGCON |= 0x1;
}


int Key_Get_Pressed()
{

	int keyval;

	keyval = ~(rGPFDAT);
	switch(keyval)

	{

		case 1: //sw14  GPG4

			rGPGDAT &= ~(0x1<<4);

			for(i=0;i<0xffff;i++);

			break;

		case 2: // sw15 GPG5

			rGPGDAT &= ~(0x1<<5); 

			for(i=0;i<0xffff;i++);

			break;

		default:
			rGPGDAT |= (0xf<<4);
	}

	return 0;

}



int Key_Wait_Get_Pressed()
{

	int a; 

	while (! (a= Key_Get_Pressed()));

	return a; 

}



void Key_Wait_Get_Released()
{	

	

	Uart_Send_String("released\n");

	while(Key_Get_Pressed());

}
