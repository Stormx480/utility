class Tree:
    def __init__(self, message, bad=None, good=None, end=False):
        self.message = message
        self.good = good
        self.bad = bad
        self.end = end

    def __str__(self):
        return self.message


if __name__ == '__main__':
    t = Tree(
        'Hello',
        Tree('Goodbye', end=True),
        Tree('How are you?',
             Tree('I have one question for you. Can you hear him?',
                  Tree('Sorry, goodbye!', end=True),
                  Tree('Do you know something about big data?',
                       Tree('This is scary. Bad people know all about you. Can I tell you how u can protect?',
                            Tree('Okay. Goodbye.', end=True),
                            Tree('Take a look here:', end=True)
                            ),
                       Tree('You can protect yourself. Take a look here:', end=True)
                       )
                  ),
             Tree('Well. Do you know something about big data?',
                  Tree('That bad. Gl', end=True),
                  Tree('Okay. Take a look here:', end=True)
                  )
             )
    )

    def main():

        command = ''

        while True:

            x = str(t)

            sentiment = yield x

            step = command.split('.')

            if len(command) == 0:
                command += sentiment
                print('Сообщение для отправки:', getattr(t, sentiment))
            else:
                command += '.'+sentiment

                a = t

                for _ in step:
                    a = getattr(a, _)

                message_for_send = getattr(a, sentiment)

                end_flag = getattr(getattr(a, sentiment), 'end')

                print('Сообщение для отправки:', message_for_send)

                if end_flag:
                    print('Это было конечное сообщение')
                    break

                if message_for_send is None:
                    print('Сообщения закончились')
                    break

    g = main()
    print('Первое сообщение:', g.send(None))

    while True:
        try:
            sentiment = input("Введите характер полученного сообщения: ")
            g.send(sentiment)
        except StopIteration:
            break
