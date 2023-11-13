input = "了解食物和植物非常重要。 如果我*们*不了*解*， 就会犯*大*错误。 我们需*要*知道哪*些*植物是安全可食用的。 过去， 人们害*怕*番茄。 他们认*为*番茄是有毒的， 因*为*它们长在一种看*起来*像危*险*植物的藤上， 叫做龙*葵*。 直到19*世纪*， 美*国*人才开*始*吃番*茄*。 他们花了很长时*间*才接*受*番茄作*为*食物。 如今， 番茄是美国饮*食*的重*要*组成部*分*。 我们可*以*在汤*和*番茄酱中找到它*们*。"

list = input.split(" ")
output = ""

for word in list:
    counter = 0
    counter2 = 0
    prelength = 0
    astrixFound = False
    for char in word:
        counter2 = counter2 + 1
        if char == "*" and astrixFound == False:
            prelength = counter2
            astrixFound = True
        elif char != "*" and astrixFound == True:
            counter = counter + 1
        elif char == "*" and astrixFound == True:
            break
    print(counter)
    if astrixFound is True:
        word = word[:prelength-1] + ("_"*(counter)) + word[(prelength+counter+1):]
    output = output + word + " "

print(output)