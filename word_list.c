#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main(int argc, char **argv)
{
	int auxI;

	char arrUpper[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	char arrLower[] = "abcdefghijklmnopqrstuvwxyz";
	char arrNumbers[] = "01234567889";
	char arrSimbols[] = "'\"!@#$%&*()_+-=,.;/<>:?[]{}~^'`|";
	char arrPonct[] = "áéíóúàèìòùãẽĩõũâêîôûçÁÉÍÓÚÀÈÌÒÙÃẼĨÕŨÂÊÎÔÛÇ";

	if (argc < 4)
	{
		printf("Uso: wordlist <charset bits> <min size> <max size> [custom charset]\n");
		exit(1);
	}

	int g_charsetBits = atoi(argv[1]);
	int g_minSize = atoi(argv[2]);
	int g_maxSize = atoi(argv[3]);

	char *g_charset = malloc(1);
	g_charset[0] = '\0';

	if (argc < 5)
	{
		if ((int)(g_charsetBits & 1) == 1)
		{
			auxI = strlen(arrUpper) + strlen(g_charset);
			char *tmp = g_charset;
			g_charset = malloc(auxI);
			sprintf(g_charset, "%s%s", tmp, arrUpper);
			free(tmp);
		}

		if ((int)(g_charsetBits & 2) == 2)
		{
			auxI = strlen(arrLower) + strlen(g_charset);
			char *tmp = g_charset;
			g_charset = malloc(auxI);
			sprintf(g_charset, "%s%s", tmp, arrLower);
			free(tmp);
		}

		if ((int)(g_charsetBits & 4) == 4)
		{
			auxI = strlen(arrNumbers) + strlen(g_charset);
			char *tmp = g_charset;
			g_charset = malloc(auxI);
			sprintf(g_charset, "%s%s", tmp, arrNumbers);
			free(tmp);
		}

		if ((int)(g_charsetBits & 8) == 8)
		{
			auxI = strlen(arrSimbols) + strlen(g_charset);
			char *tmp = g_charset;
			g_charset = malloc(auxI);
			sprintf(g_charset, "%s%s", tmp, arrSimbols);
			free(tmp);
		}

		if ((int)(g_charsetBits & 16) == 16)
		{
			auxI = strlen(arrPonct) +  strlen(g_charset);
			char *tmp = g_charset;
			g_charset = malloc(auxI);
			sprintf(g_charset, "%s%s", tmp, arrPonct);
			free(tmp);
		}
	}
	else
	{
		free(g_charset);
		auxI = strlen(argv[4]);
		g_charset = malloc(auxI);
		sprintf(g_charset, "%s", argv[4]);
	}

	int g_charsetSize = strlen(g_charset);

	int l_currSize, l_maxCombina, l_currCombina, c_modwalk, l_idxCombina;
	char *l_combinacao = malloc(1);

	// Contagem do tamanho maximo de caracteres a atingir # 1 ate 64
	l_currSize = g_minSize;
	while (l_currSize <= g_maxSize)
	{
		// Determina matematicamente o andamento do buffer
		l_maxCombina = pow(g_charsetSize, l_currSize);

		// Buffer de saida
		free(l_combinacao);
		l_combinacao = malloc(l_currSize + 1);
		l_combinacao[l_currSize] = '\0';

		// Inicia o preenchimento matematico # 1 ate N, sendo N o numero de combinacoes
		l_currCombina = 0;
		while (l_currCombina < l_maxCombina)
		{
			// Posicao real dentro do buffer de entrada do caractere a ser usado
			c_modwalk = l_currCombina;

			// Preenche cada posicao da string de saida # N-1 ate 0, sendo N o tamanho do buffer atual
			l_idxCombina = l_currSize;
			while (--l_idxCombina >= 0)
			{
				// Grava o caractere no buffer
				l_combinacao[ l_idxCombina ] = g_charset[ c_modwalk % g_charsetSize ];

				// Calcula a posicao do proximo caractere
				c_modwalk = (int)(c_modwalk / g_charsetSize);
			}

			printf("%s\n", l_combinacao);
			l_currCombina++;
		}

		l_currSize++;
	}

	return 0;
}
