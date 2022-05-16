n = int(input())

input_rope = []
for i in range(n):
    input_rope.append(int(input()))
input_rope.sort(reverse=True)

for i in range(n):
    input_rope[i] = input_rope[i] * (i+1)
print(max(input_rope))