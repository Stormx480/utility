
class Tree:

    def __init__(self, tree_dict_messages, tree_dict_first_messages, tree_id):
        self.tree_dict = tree_dict_messages
        self.tree_dict_first_messages = tree_dict_first_messages
        self.tree_id = tree_id

    def __int__(self):
        return self.tree_id

    def get_new_message(self, id_prev, sentiment_answer):
        return self.tree_dict[id_prev][sentiment_answer]

    def get_first_message(self, tree_id):
        return self.tree_dict_first_messages[tree_id]


if __name__ == '__main__':

    tree_dict_messages = {
            1: {
                'good': ['How are you?', 2, False],
                'bad': ['Sorry, goodbye', 3, True]
            },
            2: {
                'good': ['Take a look here', 7, True],
                'bad': ['Take a look here, okay?', 8, True]
            }
        }

    tree_dict_first_messages = {
        1: ['Hello', 1],
        2: ['Hey!', 4]
    }

    tree_id = input('Введите tree_id с которым будем работать: ')

    t = Tree(tree_dict_messages, tree_dict_first_messages, tree_id=int(tree_id))

    while True:

        choice = input('Вы хотите получить первое сообщение или последующие? (first/second): ')

        if choice == 'first':

            try:
                print('Ваше сообщение и его id: ', t.get_first_message(int(tree_id)))
            except Exception as ex:
                print('Вы ввели неправильный айди дерева')

        elif choice == 'second':
            prev_mess_id = input('Введите id сообщения которое вы послали:')
            sentiment_answer = input('Введите характер полученного ответа (very good/good/neutral/bad/very_bad):')

            try:
                print('Ваше сообщение и его id:', t.get_new_message(int(prev_mess_id), sentiment_answer))
            except Exception as ex:
                print(ex)
                print('Не удалось получить сообщение')

        else:
            print('Вы ввели неправильный индетификатор. Выберите first/second')