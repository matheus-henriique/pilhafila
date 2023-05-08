lineOfOP = []

def MathematicalExpression():
    print('Ensira o Valor aqui: ')
    usr_inpt = input('>>> ')
    processingList = list(usr_inpt)
    valueList = ['(',')','{','[',']','}']
    validPairs = ['()','[]','{}']
    valueCompare = []
    comparingStack = []
    counter = len(processingList)
    while counter > 0:
        value = processingList.pop(0)
        if value in valueList:
            valueCompare.append(value)
        else:
            processingList.append(value)
        counter -= 1
    counterCompare = len(valueCompare)/2
    compareIndex = counterCompare
    while counterCompare > 0:
        transition = valueCompare.pop(0)
        comparingStack.append(transition)
        counterCompare -= 1
    validationFlag = 0
    invalidationFlag = 0
    comparingStack.reverse()
    validationCounter = 0
    for value in valueCompare:
        stackTop = comparingStack.pop(0)
        if stackTop+value in validPairs and validationCounter == validPairs.index(stackTop+value):
            validationFlag += 1
            compareIndex -= 1
        else:
            invalidationFlag += 1
            compareIndex -= 1
        validationCounter += 1
    if invalidationFlag == 0:
        print('A expressão é valida')
        Menu()
    elif invalidationFlag >= 1:
        print('A expresão nao é valida')
        Menu()

def fullOP():
    counter = len(lineOfOP)
    while counter > 0:
        singleOP(1)
        counter -= 1
    Operations()

def singleOP(x):
    if bool(lineOfOP) == False:
        print('')
        print('A lista de operações esta vazia')
        print('')
        Operations()
    else:
        print('')
        flag = x
        op = lineOfOP.pop(0)
        print(' ',op," ")
        operation = op.pop(0)
        result = 0
        if operation == '+':
            for x in op:
                result += x
        elif operation == '-':
            result = op.pop(0)
            for x in op:
                result -= x
        elif operation == '*':
            result = op.pop(0)
            for x in op:
                result = result*x
        elif operation == '/':
            result = op.pop(0)
            for x in op:
                result = result/x
        print(' O Resultado da operação: ',result,' ')
        print('')
        if flag == 0:
            Operations()


def lineDictator(x,y):
    value = x
    flag = y
    if flag == 1:
        lineOfOP.append(value)
    elif flag == 0:
        if value == 2:
            singleOP(0)
        elif value == 3:
            fullOP()

# ######### OPERATIONS ############
def OperationInclude():
    print('Ensira os valores que queria adicionar a operação, quando finalizar escreva "pronto"')
    valueList = ["+"]
    flag = 0
    while flag == 0:
        usr_choice = input('--- ')
        if usr_choice == 'Pronto' or usr_choice == 'pronto':
            flag = 1
        else:
            valueList.append(int(usr_choice))
    lineDictator(valueList,1)
    Operations()

def SubtractionOperation():
    print('Ensira os valores que queria adicionar a operação, quando finalizar escreva "pronto"')
    valueList = ["-"]
    flag = 0
    while flag == 0:
        usr_choice = input('--- ')
        if usr_choice == 'Pronto' or usr_choice == 'pronto':
            flag = 1
        else:
            valueList.append(int(usr_choice))
    lineDictator(valueList,1)
    Operations()

def MultiplicationOperation():
    print('Ensira os valores que queria adicionar a operação, quando finalizar escreva "pronto"')
    valueList = ["*"]
    flag = 0
    while flag == 0:
        usr_choice = input('--- ')
        if usr_choice == 'pronto' or usr_choice == 'Pronto':
            flag = 1
        else:
            valueList.append(int(usr_choice))
    lineDictator(valueList,1)
    Operations()

def DivisionOperation():
    print('Ensira os valores que queria adicionar a operação, quando finalizar escreva "pronto"')
    valueList = ["/"]
    flag = 0
    while flag == 0:
        usr_choice = input('--- ')
        if usr_choice == 'Pronto' or usr_choice == 'pronto':
            flag = 1
        else:
            if int(usr_choice) == 0:
                print('Divisões por 0 nao é permitido ')
            else:
                valueList.append(int(usr_choice))
    lineDictator(valueList,1)
    Operations()


def MathematicalExpression():
    print('-' * 50)
    print("1 - Adicão \n2 - Subtração \n3 - Multiplicação \n4 - Divisão")
    print('-' * 50)
    usr_inpt3 = (input('--- '))
    if usr_inpt3 == '1':
        OperationInclude()
    elif usr_inpt3 == '2':
        SubtractionOperation()
    elif usr_inpt3 == '3':
        MultiplicationOperation()
    elif usr_inpt3 == '4':
        DivisionOperation()
    else:
        print('Operação invalida, Tente novamente...')
        MathematicalExpression()

def Operations():
    print("")
    print('-' * 50)
    print("1 - Adicionar Operacao na fila \n2 - Executar proxima operacao da fila \n3 - Executar Todas as operacoes da fila \n0 - Voltar para o menu principal")
    print('-' * 50)
    usr_inpt2 = (input('>>>  '))
    if usr_inpt2 == '1':
        MathematicalExpression()
    elif usr_inpt2 == '2':
        lineDictator(2,0)
    elif usr_inpt2 == '3':
        lineDictator(3,0)
    elif usr_inpt2 == '0':
        Initialization()
    else:
        print('Operação invalida. Tente novamente...')
        Operations()

def EndSequence():
    print('-' * 50)
    print('Obrigado pela preferencia volte sempre.')
    print('-' * 50)

def Menu():
    print('-' * 50)
    print('                    MENU PRINCIPAL                        ')
    print('-' * 50)
    print(' 1 - Operações \n 2 - Expressão \n 0 - Finalizar Programa')
    print('-' * 50)
    usr_inpt = (input('>>>  '))
    if usr_inpt == '0':
        EndSequence()
    elif usr_inpt == '1':
        Operations()
    elif usr_inpt == '2':
        MathematicalExpression()
    else:
        print('-' * 50)
        print('Operação invalida. Tente novamente...')
        print('-' * 50)
        Menu()

def Initialization():
    print('-' * 50)
    print('Trabalho de Estrutura de Dados, feito por Lordany, Lucca e Matheus Lopes')
    print('-' * 50)
    Menu()
    
Initialization()
