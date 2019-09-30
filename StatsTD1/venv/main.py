import csv
import math


elementsList = []
findHighest = float(0)
findSmallest = float(10)
countInstances = 0
summe = float(0)
moyenne = 0
s = 'Hello world'
print (s)

with open ('eqarchive-en_sept2018.csv') as csvFile:
        readCSV = csv.reader (csvFile, delimiter = ',')
        for row in readCSV:
            currentValue = row[4]
            if countInstances != 0:
                elementsList.append(currentValue)
                print(currentValue)
                summe += round (float(currentValue),1)

                if float(findHighest) < float(currentValue):
                    findHighest = currentValue

                if float(findSmallest) > float(currentValue):
                   findSmallest = currentValue

            countInstances += 1

        print(countInstances)
        print(summe)
        moyenne = summe / countInstances
        print ('moyenne: ' , moyenne)
        print ('plus petit chiffre: ' , findSmallest)
        print ('plus grand chiffre: ', findHighest)


        sumEcartType = 0
        #calcul de l'écart type
        for i in elementsList:
            sumEcartType += pow (float(i) - float(moyenne) ,2)

        ecartType = math.sqrt(float(sumEcartType) / float(countInstances))
        print ('ecart type: ',ecartType)