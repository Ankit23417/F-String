a= "my name is {} i am from {}"
b = "india"
c="ankit"
print(a.format(c,b))
print(f"my name is {c} i am from {b}")

txt = "for only{price:.2f}doller"
print(txt.format(price = 874.3333333))
 
print(f"{{c}}")