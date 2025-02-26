# Inicio
print('Seja muito bem vindo ao quiz sobre Inteligência Artificial! (Responda com letras maiúsculas)')
answer_user = input('Quer começar? (S/N) \n')

if answer_user != 'S':
    quit()

score = 0

print('Começando... \n')

# Pergunta 1
print('1. O que é aprendizado supervisionado em inteligência artificial? \n A) Um método em que o algoritmo aprende com dados rotulados para fazer previsões ou classificações. \n B) Um tipo de IA que pode fazer previsões sem qualquer dado de treinamento. \n C) Um sistema que ensina outras IAs de forma autônoma. \n D) Um algoritmo que não utiliza nenhum dado durante o treinamento. \n')
answer_1 = input('Resposta: ')

if answer_1 == 'A':
    print('Correto! \n')
    score = score + 1
else:
    print('Incorreto! Resposta correta: A \n')

# Pergunta 2
print('2. O que é uma rede neural artificial? \n A) Um banco de dados para armazenar informações de forma organizada. \n B) Um tipo de hardware que acelera o processamento de dados. \n C) Um tipo de algoritmo que é utilizado apenas em jogos de tabuleiro. \n D) Um modelo de aprendizado de máquina inspirado no funcionamento do cérebro humano. \n')
answer_2 = input('Resposta: ')

if answer_2 == 'D':
    print('Correto! \n')
    score = score + 1
else:
    print('Incorreto! Resposta correta: D \n')

# Pergunta 3
print('3. O que significa o termo "overfitting" em modelos de IA? \n A) Quando o modelo é treinado com dados insuficientes. \n B) Quando o modelo se ajusta demais aos dados de treinamento e tem baixo desempenho em dados novos. \n C) Quando o modelo aprende de forma independente, sem precisar de supervisão. \n D) Quando o modelo é treinado para prever valores contínuos. \n')
answer_3 = input('Resposta: ')

if answer_3 == 'B':
    print('Correto! \n')
    score = score + 1
else:
    print('Incorreto! Resposta correta: B \n')

# Pergunta 4
print('4. Qual das alternativas é um exemplo de IA fraca? \n A) Um sistema de reconhecimento de voz como a Siri ou a Alexa. \n B) Um algoritmo que tem consciência e autoaprendizado. \n C) Uma IA que pode executar múltiplas tarefas complexas sem limitações. \n D) Um computador que tem a capacidade de fazer decisões éticas de forma autônoma. \n')
answer_4 = input('Resposta: ')

if answer_4 == 'A':
    print('Correto! \n')
    score = score + 1
else:
    print('Incorreto! Resposta correta: A \n')

# Pergunta 5
print('5. Qual das alternativas é um exemplo de IA fraca? \n A) Minimizar o erro de previsão utilizando dados rotulados. \n B) Aprender sem a necessidade de dados de entrada. \n C) Maximizar a recompensa por meio de interações com o ambiente. \n D) Organizar grandes volumes de dados sem supervisionamento. \n')
answer_5 = input('Resposta: ')

if answer_5 == 'C':
    print('Correto! \n')
    score = score + 1
else:
    print('Incorreto! Resposta correta: C \n')

# pontuação final
print(f'Quiz acabou... Pontuação: {score}/5')