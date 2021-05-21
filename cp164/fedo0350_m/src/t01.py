from Set_linked import Set

source = Set()
source.add(12)
source.add(13)
source.add(14)
source.add(15)
source.add(16)
source.add(17)
source.add(18)
source.add(19)
source.add(20)
source.add(21)

target1, target2 = source.split_th()

for x in target1:
    print(x)
print("--------------------------------")
for x in target2:
    print(x)
