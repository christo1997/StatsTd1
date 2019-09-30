import csv
import math



def TachesABCD():
    elementsList = []
    findHighest = float(0)
    countInstances = 0
    summe = float(0)
    moyenne = 0
    ignoredCounter = 0

    with open ('eqarchive-en_sept2018.csv') as csvFile:
            readCSV = csv.reader (csvFile, delimiter = ',')
            for row in readCSV:
                currentValue = row[4]
                if countInstances != 0:
                    elementsList.append(currentValue)
                    #print(currentValue)
                    summe += round (float(currentValue),1)

                    if float(findHighest) < float(currentValue):
                        findHighest = currentValue

                countInstances += 1

            moyenne = summe / countInstances
            print ('moyenne: ' , moyenne)
            print ('plus grand chiffre: ', findHighest)

            sumEcartType = 0
            #calcul de l'écart type
            for i in elementsList:
                sumEcartType += pow (float(i) - float(moyenne) ,2)

            ecartType = math.sqrt(float(sumEcartType) / float(countInstances))
            print ('ecart type: ',ecartType)


def TachesEFIH():
    elementsList = []

    FrequencyTab = [0,1,2,3,4,5,6,7]
    for x in FrequencyTab:
        FrequencyTab[x]=int(0)

    countInstances = 0
    summe = float(0)
    ignoredCounter = 0
    aftershockCounter = 0
    blastCounter =0
    inducedEventsCounter = 0
    eventsLargerThanOneCounter = 0



    with open('eqarchive-en_sept2018.csv') as csvFile:
        readCSV = csv.reader(csvFile, delimiter=',')
        for row in readCSV:
            str = row[6]
            if (str.find("AFTERSHOCK") > -1 or str.find("aftershock") > -1 or str.find("Aftershock") > -1 ): #Aftershock
                aftershockCounter += 1
               # print ('found aftershock at ', countInstances, aftershockCounter)
            elif (str.find("BLAST") > -1 or str.find("blast") > -1 or str.find("Blast") > -1 ): #Blast
                blastCounter += 1
                #print ('found blast at ', countInstances, blastCounter)

            elif (str.find("INDUCED EVENT") > -1 or str.find("Induced Event") > -1 or str.find("induced event") > -1): #Évennements secondaires
                inducedEventsCounter += 1
                #print('found blast at ', countInstances, inducedEventsCounter)

           # elif (countInstances != 0 and (float(row[4]) >= 1)):
            else:
                currentValue = row[4]
                if countInstances != 0 and float(currentValue) > float(0):
                    elementsList.append(currentValue)
                    print(currentValue)
                    summe += round(float(currentValue), 1)
                    eventsLargerThanOneCounter +=1

                else:
                    ignoredCounter += 1
                    #print('valeur ignorée ', currentValue, countInstances, ignoredCounter)

            countInstances += 1

            for i in elementsList:
                index = math.floor(float(i))
                FrequencyTab[index] += int(1)


        print ('found ' , eventsLargerThanOneCounter, ' events')
        print ('monthly average of events' , eventsLargerThanOneCounter/372)


def TacheG():
    elementsList = []
    countInstances = 0
    summe = float(0)


    HighestElement = 0
    HighestElementPosition = 0

    secondhighestElement = 0
    secondhighestElementPosition = 0

    thirdHighestElement = 0
    thirdHighestElementPosition = 0


    with open('eqarchive-en_sept2018.csv') as csvFile:
        readCSV = csv.reader(csvFile, delimiter=',')
        for row in readCSV:
            currentValue = row[4]
            if countInstances != 0:
                elementsList.append(currentValue)
                # print(currentValue)
                summe += round(float(currentValue), 1)

            countInstances += 1


    countInstances = 0
    for i in elementsList:
        if (float(i) > float(HighestElement)):
            HighestElement = i
            HighestElementPosition = countInstances
        countInstances +=1

    countInstances = 0
    for i in elementsList:
        if (float(i) > float(secondhighestElement) and i != HighestElement):
            secondhighestElement = i
            secondhighestElementPosition = countInstances
        countInstances += 1

    countInstances = 0
    for i in elementsList:
        if (float(i) > float(thirdHighestElement) and i != HighestElement and i != secondhighestElement):
            thirdHighestElement = i
            thirdHighestElementPosition = countInstances
        countInstances += 1

    print('fin')


TachesEFIH()