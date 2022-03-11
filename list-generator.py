# list maker
"""
┏━━┓━━━━━━━━━┏┓━┏┓━━━━━━━━━━┏┓━━━━━━━━━━━━━┏━━━┓━━━━━━━━┏┓━━━━━━━━━
┃┏┓┃━━━━━━━━━┃┃━┃┃━━━━━━━━━━┃┃━━━━━━━━━━━━━┃┏━┓┃━━━━━━━━┃┃━━━━━━━━━
┃┗┛┗┓┏━━┓━━━━┃┗━┛┃┏━━┓┏━┓━┏━┛┃┏━┓┏┓┏┓┏┓━━━━┃┗━┛┃┏━━┓━┏━┓┃┃┏┓┏━━┓┏━┓
┃┏━┓┃┃┏┓┃━━━━┃┏━┓┃┃┏┓┃┃┏┓┓┃┏┓┃┃┏┛┣┫┗╋╋┛━━━━┃┏━━┛┗━┓┃━┃┏┛┃┗┛┛┃┏┓┃┃┏┛
┃┗━┛┃┃┗┛┃━━━━┃┃━┃┃┃┃━┫┃┃┃┃┃┗┛┃┃┃━┃┃┏╋╋┓━━━━┃┃━━━┃┗┛┗┓┃┃━┃┏┓┓┃┃━┫┃┃━
┗━━━┛┗━━┛━━━━┗┛━┗┛┗━━┛┗┛┗┛┗━━┛┗┛━┗┛┗┛┗┛━━━━┗┛━━━┗━━━┛┗┛━┗┛┗┛┗━━┛┗┛━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def main():
    # prompt user for a list type
    list_type = input('type ul or ol: ')
    print()

    while list_type != 'ul' and list_type != 'ol':
        print('Please type either ul or ol: ')
        list_type = input()

    # creat the file
    file = open('list.html', 'w')

    # create sequence
    list = []

    # keep asking for items
    li = ''
    while li != 'quit-list':
        li = input('Enter a list item, enter quit-list to stop ')
        if li != 'quit-list':
            list.append(li)
    print(list)

    # add the list to the file
    create_list(list_type,list,file)

    # clost the file
    file.close()



def create_list(list_type,list,file):
    if list_type == 'ul':
        open_tag = '<ul>'
        close_tag = '</ul>'
    else:
        open_tag = '<ol>'
        close_tag = '</ol>'

    file.write(open_tag + '\n')

    for item in list:
        file.write('\t' + '<li>' + item + '</li>' + '\n')

    file.write(close_tag + '\n')


main()
