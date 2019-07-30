from jiwer import wer
import nltk 
import distance
import re, math
from collections import Counter
from nltk.corpus import stopwords
from nltk import tokenize
import argparse
import os
from pathlib import Path


# Global variables
WORD = re.compile(r'\w+')
sws = stopwords.words('portuguese')

# Stopwords removal
def text_normalized(text):
    palavras_tokenize = tokenize.word_tokenize(text, language='portuguese')
    filtered_sentence = list(filter(lambda x: x.lower() not in sws, palavras_tokenize))
    return " ".join(filtered_sentence)


# Cosine
def get_cosine_result(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)


def get_cosine(text1, text2):
    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)
    cosine = get_cosine_result(vector1, vector2)
    return cosine


# Jaccard
def get_jaccard(text1, text2):
    jaccard = nltk.jaccard_distance(set(text1), set(text2))
    return jaccard

# Levenshtein
def get_levenshtein(text1, text2):
    levenshtein = distance.levenshtein(text1, text2)
    return levenshtein


# Word Error Rate
def get_wer(text1, text2):
    return wer(text1, text2)


def get_wrr(text1, text2):
    return 1 - wer(text1, text2)

# Characters
def get_numberTotalCharacters(text1):
	return len(text1)

def get_numberTotalCharactersSemEspaco(text1):
	count = 0
	for c in text1:
		if c.isspace() != True:
			count = count+1
	return count

# Punctuations
def get_pontuation(text):
    numberOfFullStops = 0
    numberOfQuestionMarks = 0
    numberOfExclamationMarks = 0
    numberOfCommaMarks = 0
    numberOfColonMarks = 0
    numberTotalPunctuation = 0

    for line in text:
        numberOfFullStops += line.count(".")
        numberOfQuestionMarks += line.count("?")
        numberOfExclamationMarks += line.count("!")
        numberOfCommaMarks += line.count(",")
        numberOfColonMarks += line.count(":")
        

    numberTotalPunctuation = numberOfFullStops + numberOfCommaMarks + numberOfQuestionMarks + numberOfExclamationMarks + numberOfColonMarks
    return numberOfFullStops, numberOfCommaMarks, numberOfQuestionMarks, numberOfExclamationMarks, numberOfColonMarks, numberTotalPunctuation 


if __name__ == '__main__':

    lines = []
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', type=str, nargs=2, metavar='dir', help='directories of documents .txt. OBS.: First .txt might be the text recovered by API')
    args = parser.parse_args()
    filename = args.d
    for line in filename:
        lines.append(Path(line).read_text())

    # Documents or Texts
    test1 = re.sub(r'\n{1,}|\s{2,}', " ", lines[0])
    test2 = re.sub(r'\n{1,}|\s{2,}', " ", lines[1])

    print('\n'"TEXTO BASE")
    print(test1)
    print('\n'"TEXTO AMOSTRAL ANALISADO")
    print(test2)

    # Get punctuation
    numberOfPunctuation = get_pontuation(test1)
    numberOfPunctuation2 = get_pontuation(test2)
    
    # Stopwords removal
    # test1 = text_normalized(test1)
    # test2 = text_normalized(test2)

    # Punctuation results
    print('\n'"PRECISÃO NA PONTUAÇÃO:",'\t',"   TEXTO BASE",'\t',"AMOSTRA")
    print('- Quantidade de Pontos:  ','\t', numberOfPunctuation[0],'\t', numberOfPunctuation2[0])
    print('- Quantidade de Virgulas:','\t', numberOfPunctuation[1],'\t', numberOfPunctuation2[1])
    print('- Quantidade de Interrogações:','\t', numberOfPunctuation[2],'\t', numberOfPunctuation2[2])
    print('- Quantidade de Exclamações:','\t', numberOfPunctuation[3],'\t', numberOfPunctuation2[3])
    print('- Quantidade de Dois Pontos:','\t', numberOfPunctuation[4],'\t', numberOfPunctuation2[4])
    print('- Quantidade de Pontuações:','\t', numberOfPunctuation[5],'\t', numberOfPunctuation2[5])
    print('- Precisão na pontuação:','\t', round((numberOfPunctuation2[5] / numberOfPunctuation[5])*100,2) , '%')
    
    # Levenshtein results
    print('\n'"DISTÂNCIA ENTRE OS TEXTOS:")  
    print("- Distância entre Caracteres (Levenshtein):",'\t', round((((get_levenshtein(test1, test2) - get_numberTotalCharactersSemEspaco(test1)) / get_numberTotalCharactersSemEspaco(test1))+1)*100,2), '%', '\t', get_levenshtein(test1, test2), 'de', get_numberTotalCharactersSemEspaco(test1))
    print("- Distância entre Palavras (Word Error Rate):",'\t', round(get_wer(test1, test2)*100,2), '%','\t', "%.2f" % get_wer(test1, test2))
    print('- Distância entre os textos (dissimilaridade):','\t', round((((get_wer(test1, test2))+(((get_levenshtein(test1, test2) - get_numberTotalCharactersSemEspaco(test1)) / get_numberTotalCharactersSemEspaco(test1))+1 ))/2)*100,2) , '%')
    
    # Similatities results
    print('\n'"PROXIMIDADE ENTRE OS TEXTOS:")
    print("- Taxa Reconhecimento de palavras (WRR):",'\t', round(get_wrr(test1, test2)*100,2), '%','\t', "%.2f" % get_wrr(test1, test2))    
    print("- Coeficiente de similaridade (Jaccard):",'\t', round((1 - get_jaccard(test1, test2))*100,2), '%','\t', "%.2f" % get_jaccard(test1, test2))
    print('- Coeficiente de similaridade (Cosseno):','\t', round(get_cosine(test1, test2)*100,2), '%','\t', "%.2f" % get_cosine(test1, test2))
    print('- Proximidade entre os textos (similaridade):','\t', round((( get_wrr(test1, test2) + get_cosine(test1, test2) + (1-get_jaccard(test1, test2)))/3)*100,2) , '%')
    print('')


