
def temp_tester(temp):
    def tt (temp2):
        if temp2 > 75:
            temp2 = temp2*(9/5) + 32
            print("Reference temp was expected in degrees C, but I'll answer you anyway...")
        if temp2 < (temp-1):
            result = False
        elif temp2 > (temp+1):
            result = False
        else:
            result = True
        return result
    return tt

human_tester = temp_tester(37)
chicken_tester = temp_tester(41.1)

print(chicken_tester(42))
print(human_tester(42))
print(chicken_tester(43))
print(human_tester(35))
print(human_tester(98.6))
