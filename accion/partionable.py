
def PartionCheck(user_list):
    if len(user_list)%2 == 0:
        print("Entered list"+ str(user_list)+ "is partitionable")
    else:
        print("Entered list"+ str(user_list)+ " is not partitionable")

user_list = list(input("Please enter the valuse"+" "))

PartionCheck(user_list)
