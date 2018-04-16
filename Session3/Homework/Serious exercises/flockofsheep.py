# 2.1
print("Hello, my name is Canh and these are my ship sizes")
sheepsize = [5,7,300,90,24,50,75]
print(sheepsize)
# 2.2
maxsize = max(sheepsize)
print("{0} {1} {2}".format("Now my biggest sheep has size", maxsize, "let's shear it"))
# 2.3
a = sheepsize.index(maxsize)
sheepsize[a] = 8
print("After shearing, here is my flock"+"\n",sheepsize)

# 2.4
for i in range(len(sheepsize)):
    sheepsize[i] += 50
print("One month has passed, now here is my flock" + "\n", sheepsize)
