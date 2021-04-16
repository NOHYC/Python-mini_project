/*
 * =====================================================================
 * NAME         : Main.c
 *
 * Descriptions : Main routine for S3C2450
 *
 * IDE          : GCC-4.1.0
 *
 * Modification
 *	  
 * =====================================================================
 */
#include "2450addr.h"
#include "libc.h"

#define EXAMPLE 310
/*
 * 310: 실습 3 : LED_ON_Test
 *
 * 311	실습 4-1 : Key_Input_Test_with_LED
 *	
 * 320: 실습 5 : UART_Test
 *
 * 312: 실습 4-2 : Key_Input_Test_with_UART
 *
 * 330: 실습 6 : Timer_Test	
 * 
 */

/***************************************
 * 
 * Title: LED_ON_Test
 * 
 ***************************************/

#if EXAMPLE == 310 

enum SwitchState{
	DEFAULT_SWITCH,
	LEFT_SWITCH,
	RIGHT_SWITCH
};

void ProjectInit();

void Main(void)
{	
	ProjectInit();
	
	// Data relation with LED
	char *right_arr[] = {1, 2, 4, 8, 9, 10, 12, 13, 14, 15}; 
	char *left_arr[] = {8, 4, 2, 1, 9, 5, 3, 11, 7, 15}; 
	// Data relation with Buzzer
	int music[] = {D1, D1, C1, D1, E1, C2, D1, E1, F1, E1, F1, F1, E1, F1, G1-30, F1, A1, C2+100};		
	// Data realtion with Switch
	enum SwitchState cur_state = DEFAULT_SWITCH; 
	
	// Control valuables
	int led_data = 0, music_idx = 0, switch_num = 0;
	int i = 0;
	int dur = 0;

	while(1) {	
		rGPFDAT &= ~(0x1<<14);
		switch_num = (~(rGPFDAT>>0) & 0xF);

		if (switch_num == LEFT_SWITCH || switch_num == RIGHT_SWITCH) cur_state = switch_num;

		switch(cur_state) { 
			case LEFT_SWITCH:
				led_data = *(left_arr + (i % (sizeof(left_arr) / sizeof(left_arr[0]))));
				++i;
				break;

			case RIGHT_SWITCH:
				led_data = *(right_arr + (i % (sizeof(right_arr) / sizeof(right_arr[0]))));
				++i;
				break;

			default:
				break;
		}

		// Debug Our Code
		
		/*Uart_Printf("cur_state : %d\n", cur_state);
		Uart_Printf("music idx : %d\n", music_idx);
		Uart_Printf("music : %d\n", music[music_idx % (sizeof(music) / sizeof(music[0]))]);*/

		Led_Display(led_data);

		if((music_idx%4+2)<6 && (music_idx%4+2)>1) dur= 50;
		else if((music_idx%18) == 16 || (music_idx%18) == 17) dur= 200;
		else dur = 100;

		if (cur_state) Buzzer_Beep((int)(music[music_idx++ % (sizeof(music) / sizeof(music[0]))]), dur);
	}	
}

void ProjectInit() {
	Key_Port_Init();
	Led_Init();
	Buzzer_Init();
}

#endif 
