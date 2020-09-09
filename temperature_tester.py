
def temp_tester(temp):
    def tt (temp2):
        if temp2 < (temp-1):
            result="False. The temperature is abnormally low."
        elif temp2 > (temp+1):
            result="False - The patient has a FEVER."
        else:
            result="True."
        return result
    return tt
