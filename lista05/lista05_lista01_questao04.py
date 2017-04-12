pop_a = 80000
grow_a = 0.03
pop_b = 200000
grow_b = 0.015
c = 0
while pop_a < pop_b:
    pop_a = pop_a + (pop_a * grow_a)
    pop_b = pop_b + (pop_b * grow_b)
    c = c + 1
print("Será preciso", c ,"anos para o país A ser mais populoso que o país B")
