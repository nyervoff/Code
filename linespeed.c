#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <sys/timeb.h>

#define MAXCOUNT 5000000

int main(int argc, char **argv)
{
	long count = 0;
	double seconds;

	char *buffer = malloc(100);

	struct timeb *before, *after;

	before = malloc(sizeof(struct timeb));
	after = malloc(sizeof(struct timeb));

	ftime(before);

	while (1)
	{
		scanf("%s", buffer);
		if (++count == MAXCOUNT)
		{
			ftime(after);
			seconds = (double)after->time - before->time + ((double)after->millitm - before->millitm) / 1000;
			printf("%.3f time span (secs)\n", seconds);
			printf("%.3f word/sec\n", MAXCOUNT / seconds);
			printf("%s\n", buffer);

			memcpy(before, after, sizeof(struct timeb));
			count = 0;
		}
	}

	return 0;
}

