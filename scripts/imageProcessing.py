class imageProcessing(object):


    def normalLines(self, images):
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
        return newImages
