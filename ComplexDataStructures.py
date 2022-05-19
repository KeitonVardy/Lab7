

def main():

    me_info = {
        'name': 'Keiton',
        'student_id': '10208745',
        'pizza_toppings' : [
            'pineapple,'
            'sausage',
            'mushroom',
        ],
        'movies': [
            {'title': 'Deadpool',
             'genre': 'action',
            },
            {'title': 'Top Gun',
             'genre': 'action',
            }
        ]

}

    new_movie = {'title': 'Jumanji', 
                 'genre': 'comedy'}
    me_info['movies'].append(new_movie)

    new_toppings = ('pepperoni', 
                    'ham', 
                    'bacon')
    add_toppings(me_info, new_toppings)
    add_toppings.sort()

    print_data_structure(me_info)

def add_toppings(me, toppings):
    for t in toppings:
        me['pizza_toppings'].append(t)



def print_data_structure(me_info):
    print('Hi Joe, my name is', me_info['name'],'and my student ID is', me_info['student_id'], end ='.')

    sentence = 'My ideal pizza has'

    for i,p in enumerate(me_info['pizza_toppings']):
        sentence += p['pizza_toppings']
        if i < len(me_info['pizza_toppings']) -1:
            sentence += ', '
        else:
            sentence += '.'

    print(sentence)

    sentence_movies = 'I like to watch' + me_info['genre'] + 'movies.'

    for m in (me_info['genre']):
        print(m)

    print(sentence_movies)

    sentence_title = "Some of my favourites are" + me_info['title']

    for i,t in enumerate(me_info['title']):
        sentence_title += t['title']
        if i < len(me_info['title']) -1:
            sentence_title += ', '
        else:
            sentence_title += '!'


    
main()