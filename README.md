## Primeiros passos
Este estudo tem o objetivo medir a qualidade de transcrições de áudio para texto no idioma Português Brasil.
Para analisar as transcrições são utilizados algoritmos em python 3 para medir os graus de precisão das transcrições.
Para simular este estudo, basta seguir as intruções abaixo. 
Para dar inicio aos testes é necessário obter o texto original (base.txt) e o texto adivindo de uma transcrição gerado de forma automática utilizando uma API de transcrição (amostra.txt)

### Pré-requisitos
Python 3,
NLTK,
Jiwer,
Distance,
Six,
Numpy

### Instalação:
	sudo apt install python3 python3-pip // sudo yum install python35 python-pip
	sudo -H pip install --default-timeout=100 -r algorithms.txt
  
  
### Execução:
  python comparar.py -d base.txt amostra.txt

### Detalhes:
Este script calcula similaridade textual a partir da semelhança do conteúdo semântico em oposição à semelhança estimada em sua representação sintática. Já a dissimilaridade foi calculada com base na estrutura sintática do texto em oposição ao sentido das unidades linguísticas. Por esse motivo uma técnica não refletiu, necessariamente, o inverso da outra.
Para análise dos resultados foram utilizados cinco algoritmos computacionais capazes de estimar a força da relação semântica entre os textos a partir de uma descrição numérica obtida pela comparação das informações, e assim, definindo a distância ou a proximidade de edição dos termos textuais.
O primeiro algoritmo utilizado foi a Distância Levenshtein, uma métrica que tem como finalidade medir a diferença entre duas sequências de caracteres. A segunda baseou-se no algoritmo WER (Word Error Rate), que define a taxa de erro de palavras, sendo usado frequentemente para verificar a precisão de sistemas de reconhecimento de fala. Assim como a  Distância de Levenshtein, o WER define a distância pela quantidade de operações mínimas que devem ocorrer para que as amostras fiquem idênticas, mas ao contrário da ​primeira as operações são avaliadas com base nas palavras e não em caracteres individuais.
Para o cálculo da similaridade foi adotado um terceiro algoritmo, o WRR (Word Recognition Rate) uma métrica que define a taxa de reconhecimento de palavras, sendo na verdade o inverso do WER. Outro algoritmo adotado foi o coeficiente de Jaccard, que mede a similaridade entre dois conjuntos dividindo a interseção dos conjuntos pela sua união. Por fim, foi utilizada uma abordagem mais semântica, analisando apenas os graus de similaridade entre o texto original e o texto transcrito e, para este fim, foi utilizado o algoritmo baseado no coeficiente entre os cossenos de similaridade.
Para aplicação do benchmarking foram utilizados scripts escritos em python e difundidos no meio científico e organizacional, sendo eles: NLTK, Jiwer, Distance, Six e Numpy.

NLTK
O Natural Language Toolkit (NLTK), é um conjunto de bibliotecas e programas para processamento de linguagem natural simbólica e estatística. Desenvolvido no Departamento de Computação e Ciência da Informação da Universidade da Pensilvânia por Steven Bird e Edward Loper, o NLTK inclui demonstrações gráficas e dados de amostragem e destina-se a apoiar a pesquisa e o ensino em Programação Neurolinguística ou em áreas estreitamente relacionadas, incluindo linguística empírica, ciência cognitiva, inteligência artificial, recuperação de informações e aprendizado de máquina. 
O NLTK tem sido usado com sucesso como uma ferramenta de ensino, como uma ferramenta de estudo individual, e como uma plataforma para prototipagem e construção de sistemas de pesquisa, pois suporta funcionalidades de classificação, tokenização, stremming, marcação, análise e raciocínio semântico.

Jiwer
O Jiwer implementa métodos para calcular o WER (Word error rate), ou seja, a taxa de erro de palavras entre uma sentença verdadeira e uma sentença hipotética, é geralmente uma medida de desempenho para um sistema de reconhecimento automático de fala. Ele Calcula a distância mínima de edição entre a sentença correta e a sentença transcrita automaticamente por um sistema informatizado usando o algoritmo de Wagner-Fisher. Como esse algoritmo calcula a distância mínima de edição de nível de caractere, cada palavra de uma frase é atribuída a um inteiro único e a distância de edição é calculada sobre uma cadeia de inteiros.

Distance
Este pacote fornece diversas funcionalidades matemáticas para calcular semelhanças entre sequências arbitrárias. Entre as diversas métricas incluídas neste pacote é possível citar: Levenshtein, Hamming, Jaccard, Sorensen e alguns bônus. Todos os cálculos de distância são implementados em Python puro, e a maioria deles podem ser implementados também em C.
A distância de Hamming e Levenshtein podem ser normalizadas, de modo que os resultados de várias medidas de distância possam ser significativamente comparados. Inclusive o pacote distance disponibiliza duas estratégias para Levenshtein: o comprimento de menor distância e o comprimento mais longo.
Entre os bônus, há a função fast_comp, que calcula a distância entre duas strings até um valor de 2 incluído. Se a distância entre as strings for maior que isso, -1 será retornado. Esta função é de uso limitado, mas por outro lado é bastante mais rápida que a Levenshtein.

Six
Six é uma biblioteca de compatibilidade entre o Python 2 e 3 (2 * 3 = 6). Todo o código do six está contido em apenas um arquivo Python e tem como objetivo fornecer funções utilitárias para suavizar as diferenças entre as versões, auxiliando no processo de escrever códigos em Python que sejam compatíveis em ambas as versões.

Numpy
NumPy é um pacote para a linguagem Python que suporta arrays e matrizes multidimensionais, possuindo uma larga coleção de funções matemáticas para trabalhar com estas estruturas. NumPy é um pacote fundamental para computação científica com o Python. Ele contém entre outras coisas:
um poderoso objeto array N-dimensional;
funções sofisticadas;
ferramentas para integrar código C / C ++ e Fortran;
álgebra linear útil, transformada de Fourier e capacidades de números aleatórios
Além de seus usos científicos óbvios, o NumPy também pode ser usado como um contêiner multidimensional eficiente de dados genéricos, onde tipos de dados arbitrários podem ser definidos, o que permite sua integração de forma fácil e rápida a uma ampla variedade de bancos de dados.
