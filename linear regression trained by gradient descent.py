r=[1,2,3,4,5,6,7,8,9,10]
y=[2.3,4.2,6.2,8.7,10.5,12.4,14.5,16,17.9,20.2]
w=0.0
b=0.0
s=0.01
for epoch in range(1000):
    for i in range(len(r)):
        error = y[i] - (r[i] * w + b)
        w += s * error * r[i]
        b += s * error
  
print("sloop: ",w,"constant: ",b)
for i in range (len(r)):
    print(y[i],r[i]*w+b)

