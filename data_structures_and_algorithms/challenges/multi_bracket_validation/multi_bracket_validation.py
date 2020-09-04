# def multi_bracket_validation(input):
#     curly_1 = input.count('{')
#     curly_2 = input.count('}')
#     paran_1 = input.count('(')
#     paran_2 = input.count(')')
#     brack_1 = input.count('[')
#     brack_2 = input.count(']')
#     print(brack_1, paran_1)
#     if curly_1 == 0 and curly_2 == 0 and paran_1 == 0 and paran_2 == 0 and brack_1 == 0 and brack_2 == 0:
#         return False
#     elif curly_1 != curly_2:
#         return False
#     elif brack_1 != brack_2:
#         return False
#     elif paran_1 != paran_2:
#         return False
#     else:
#         return True


# print(multi_bracket_validation('[this is() a{ test for true]'))

def multi_bracket_validation(input):
    """
    given a string it will check if the brackets inside it are opened/closed correctly
    """

    opening = ["[","{","("]
    closing = ["]","}",")"]
    check = []

    for i in input:

            if i in opening:
                check.append(opening.index(i))

            elif i in closing:
                if ((len(check) > 0) and (closing.index(i) == check[-1])):
                    check.pop()
                else:
                    return False

    if len(check) == 0:
            return True
    else:
            return False

if __name__ == "__main__":
    print(multi_bracket_validation('({)}'))
    print(multi_bracket_validation('(some string)'))

