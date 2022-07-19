# uuri iga listi esimest konna
        # testime hetkel ainult ülevalt ja vasakult

        #teed = [len(list(filter(lambda x: isinstance(x, list), [up, down, left, right])))*[0 for i in range(konni)] + [vahemaa]]

        konnad = [up, None, left, None]
        teed = [[0 for i in range(konni)] + [vahemaa], None, [0 for i in range(konni)] + [vahemaa], None]

        for ind in range(len(konnad)):

            if konnad[ind] != None:
                asukohad = teed[ind]

                while not all(i>=lopp for i in asukohad[:-1]):

                    for i, t in enumerate(konnad[ind]):

                        # see konn peab liikuma
                        if asukohad[i+1] >= vahemaa and asukohad[i]<lopp:
                            t.st()
                            t.fd(kiirus)
                            asukohad[i] += kiirus

    def make_row(self):

        up = [turtle.Turtle("turtle") for _ in range(konni)]
        for t in up:
            t.ht()
            t.penup()
            t.backward(450)
            t.left(45)
            t.forward(750)
            t.right(135)

        left = [turtle.Turtle("turtle") for _ in range(konni)]

        for t in left:
            t.ht()
            t.penup()
            t.backward(450)

        # kõik konnad
        for i, t in enumerate(left+up):
            t.speed(1)
            t.turtlesize(3)
            t.color(choice(cols))

        # kui järgmine konn jõuab kohale vahemaa, siis hakka liikuma
        # peab erinevaid ridu suutma samal ajal liigutada
        liiguta_ridu(up, [], left, [])