#include <signal.h>
#include <stdio.h>
#include <unistd.h>

static void sigwinch_handler(int sig)
{
	printf("got signal: %d\n", sig);
}

int main()
{
	signal(SIGWINCH, sigwinch_handler);
	printf("waiting for signal...\n");
        pause();
        return 0;
}
