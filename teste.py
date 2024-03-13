import re
import pandas as pd

dados_curso = """21111676,  Ana  Clara  Felix  Pereira,  4.310,  25.285,  6.314,  5.425,  10.590,  9.920,  1.654,  10.965,  0.000,  -
53.834,  7,  -,  -,  -,  -,  -,  -,  -,  -,  -  /  21182638,  Caio  Soares  Couto,  2.586,  3.158,  5.076,  2.325,  19.890,  4.129, 
1.418, 18.811, 2.935, -45.238, 5, -, -, -, -, -, -, -, -, - / 22201721, Gabriele Cunha da Silva, 0.000, 0.000, 0.000, 
5.425,  4.964,  2.476,  2.127,  26.374,  6.233,  -49.692,  6,  -,  1,  -,  1,  -,  1,  -,  1,  -  /  22214507,  Helena  Alves  de 
Andrade, 0.000, 0.000, 0.000, 2.325, 21.240, 8.477, 3.545, 19.378, 4.345,  -36.397, 4, -, -, -, -, -, -, -, -, - / 
21191427, Isadora Sousa Silva, 7.758, 14.939, 4.074, 3.358, 16.790, 7.908, 4.254, 35.449, 6.100, 3.617, 2, 
-, -, -, -, -, -, -, -, - / 21170668, Joao Guilherme Lopes Lamounier Araujo, 0.000, 18.102, 5.027, 1.550, 1.290, 
2.976, 0.236, 6.711, 5.500,  -85.110, 9, -, -,  -, -, -, -, -, -, - / 21195825, Laila Evelyn, 0.000, 14.887, 8.166, 
3.100, 6.773, 5.490, 0.709, 2.598, 4.571, -82.369, 8, -, -, -, -, -, -, -, -, - / 21108445, Lindson Veras Raposo, 
6.034, 33.545, 4.473, 6.975, 26.923, 4.295, 1.418, 28.359, 4.912, 9.258, 1, -, -, -, -, -, -, -, -, - / 21109354, 
Luis Fernando Silva, 0.000, 13.361, 7.704, 0.000, 26.206, 8.067, 5.672, 19.614, 6.667, -13.412, 3, -, -, -, -, -
, -, -, -, -"""

sql = """USE pas;

        CREATE TABLE `curso`(
            `inscricao` INT PRIMARY KEY,
            `nome` VARCHAR(150),
            `eb1_p1` DECIMAL (7, 3),
            `eb2_p1` DECIMAL (7, 3),
            `nr_p1` DECIMAL (7, 3),
            `eb1_p2` DECIMAL (7, 3),
            `eb2_p2` DECIMAL (7, 3),
            `nr_p2` DECIMAL (7, 3),
            `eb1_p3` DECIMAL (7, 3),
            `eb2_p3` DECIMAL (7, 3),
            `nr_p3` DECIMAL (7, 3),
            `argumento_final` DECIMAL (7, 3),
            `universal` INT,
            `negros` VARCHAR(150),
            `ppi_baixa_renda` VARCHAR(150),
            `ppi_baixa_renda_pcd` VARCHAR(150),
            `n_ppi_baixa_renda` VARCHAR(150),
            `n_ppi_baixa_renda_pcd` VARCHAR(150),
            `ppi_alta_renda` VARCHAR(150),
            `ppi_alta_renda_pcd` VARCHAR(150),
            `n_ppi_alta_renda` VARCHAR(150),
            `n_ppi_alta_renda_pcd` VARCHAR(150)
        );"""

dados_curso = re.sub(r' +', '', dados_curso)
dados_curso = re.sub(r'\n', '', dados_curso)

alunos = dados_curso.split('/')

for aluno in alunos:
    dados_aluno = aluno.split(',')

    inscricao = int(dados_aluno[0])
    nome = dados_aluno[1]
    eb1_p1 = float(dados_aluno[2])
    eb2_p1 = float(dados_aluno[3])
    nr_p1 = float(dados_aluno[4])
    eb1_p2 = float(dados_aluno[5])
    eb2_p2 = float(dados_aluno[6])
    nr_p2 = float(dados_aluno[7])
    eb1_p3 = float(dados_aluno[8])
    eb2_p3 = float(dados_aluno[9])
    nr_p3 = float(dados_aluno[10])
    argumento_final = float(dados_aluno[11])
    universal = int(dados_aluno[12])
    negros = dados_aluno[13]
    ppi_baixa_renda = dados_aluno[14]
    ppi_baixa_renda_pcd = dados_aluno[15]
    n_ppi_baixa_renda = dados_aluno[16]
    n_ppi_baixa_renda_pcd = dados_aluno[17]
    ppi_alta_renda = dados_aluno[18]
    ppi_alta_renda_pcd = dados_aluno[19]
    n_ppi_alta_renda = dados_aluno[20]
    n_ppi_alta_renda_pcd = dados_aluno[21]

    print(dados_aluno)
    print('=' * 150)
