/*
** 	HW2 AES
** Name	: Kim Hyeongi
** ID	: 20110032
*/

#ifndef TI_AES
#define TI_AES
unsigned char ct[10][16];
unsigned char ct_diff[10][16];
void aes_encrypt(unsigned char *state, unsigned char *key, int flag);
void aes_decrypt(unsigned char *state, unsigned char *key);
void ans_printf(unsigned char *state);
int ham_dist(unsigned char* rhs, unsigned char* lhs);
void rand_bit(unsigned char* state);
void rand_bit2(unsigned char* state);
void print_ham_dist(void);
#endif
