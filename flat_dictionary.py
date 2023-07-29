n= {"name12":"tirlok12","name":"tirlok","about":{"age":26,"email":{"myemail":"gmail"}},"kali":"chand"}

y = {}
my ={}
def flat(x):
    for i,j in x.items():
        if type(j) is dict:
            my[i] = j
            return flat(my[i])
        else:
            y[i] = j
flat(n)
print(y)

# isme {"kali":"chand" wala data nhi aya mere se}
# koi logic nhi soch paya main
