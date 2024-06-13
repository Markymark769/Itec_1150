# # catNames = []
# #
# # while True:
# #     print('Enter the name of cat' + str(len(catNames) + 1) + '(Or enter nothing to stop):' )
# #     name = input()
# #     if name == '':
# #         break
# #     catNames = catNames + [name] # list concatenation
# # print('The cat names are:')
# # for name in catNames:
# #     print('' + name)  # the empty string is just used for putting an empty space in the program
# # print('So many cats!')
#
# def main():
#     catNames = input()
#     someVariable = processing(catNames)
#     outputs(catNames)
#
# def inputs():
#     catNames = []
#     while True:
#         print('Enter the name of cat' + str(len(catNames) + 1) + '(Or enter nothing to stop):' )
#         name = input()
#         if name == '':
#             break
#         catNames = catNames + [name] # list concatenation
#     return catNames
#
# def get_pos_int():
#     pos_int = input('Please enter a whole number only: ')
#         while pos_int.isnumeric() is False or int(pos_int) < 0:
#             pos_int = input('Please enter a number greater than your start number: ')
#         pos_int = int(pos_int)
#     return pos_int
#
# def processing():
#
#
# def outputs(catNames):
#     print('The cat names are:')
#     for name in catNames:
#         print('' + name)  # the empty string is just used for putting an empty space in the program
#     print('So many cats!')
#
# main()

def main():
    cat_names = inputs()
    outputs(cat_names)

def inputs():
    cat_names = []
    while True:
        print('Enter the name of cat ' + str(len(cat_names) + 1) + ' (Or enter nothing to stop):')
        name = input()
        if name == '':
            break
        cat_names.append(name)
    return cat_names

def outputs(cat_names):
    print('The cat names are:')
    for name in cat_names:
        print(name)
    print('So many cats!')

main()
