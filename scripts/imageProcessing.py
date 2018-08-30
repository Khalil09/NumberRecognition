class imageProcessing(object):

    def normalLines(images):
        print('[processing] normal lines start')
        newImages = []
        maxValue = 255
        lineSize = 28
        count = 0
        lineSum = 0
        sumOfVector = 0
        for image in images:
            newVector = []
            for pos in image:
                if pos > 0:
                    pos = pos/maxValue
                lineSum += pos
                count += 1

                if count == lineSize:
                    sumOfVector += lineSum
                    newVector.append(lineSum)
                    lineSum = 0
                    count = 0

            vectorPos = 0
            for value in newVector:
                if value > 0:
                    newVector[vectorPos] = value/sumOfVector
                vectorPos += 1
            newImages.append(newVector)
        print('[processing] normal lines end')
        return newImages

    def binaryLines(images):
        print('[processing] binary lines start')
        count = 0
        aux = list()
        final = list() 
        for li in images:
            if aux != []:
                final.append(aux)
            aux = list()
            count = 0
            for i in range(len(li)-1):
                if li[i] != 0:
                    count += 1
                if (i+1) % 28 == 0:
                    aux.append(count)
                    count = 0

            if li == images[-1]:
                final.append(aux)

        print('[processing] binary lines end')
        return final