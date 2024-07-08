#include <stdio.h>
#include <string.h>
char* toup(char *s) {
	for (int i=0; i < strlen(s); i++) {
		if (s[i] >= 0x61 && s[i] <= 0x7a)
			s[i] = s[i] - 32;
	}
	return s;
}
int main(void) {
	char s[] = "menteb.in";
	puts(toup(s));
}