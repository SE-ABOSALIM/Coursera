# Python version of switch-case structure, instead of switch-case -> match-case

http_status = 100

match http_status:
    case 200:
        print('Success')
    case 400:
        print('Bad request')
    case 404:
        print('Not found')
    case 500 | 501:
        print('Server error')
    case _:
        print('Something went wrong')