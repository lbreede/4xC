from random import randint

MAGIC_NUMBER = 9
XCHAR = "X"
OCHAR = "O"
PRETTY_BOARD = (
    " {a} | {b} | {c} "
    "\n---+---+---\n"
    " {d} | {e} | {f} "
    "\n---+---+---\n"
    " {g} | {h} | {i} "
    "\n"
    "\n===========\n"
)

gb = [None] * MAGIC_NUMBER


def draw_board():
    a, b, c, d, e, f, g, h, i = [x if x is not None else " " for x in gb]
    print(PRETTY_BOARD.format(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i))


def check_if_won():
    a, b, c, d, e, f, g, h, i = gb

    if a == b and b == c and a is not None:
        return a
    elif d == e and e == f and d is not None:
        return d
    elif g == h and h == i and g is not None:
        return g
    elif a == d and d == g and a is not None:
        return a
    elif b == e and e == h and b is not None:
        return b
    elif c == f and f == i and c is not None:
        return c
    elif a == e and e == i and a is not None:
        return a
    elif c == e and e == g and c is not None:
        return c
    else:
        return False


def pick(val):
    while True:
        idx = randint(0, MAGIC_NUMBER - 1)
        if gb[idx] is None:
            gb[idx] = val
            print(f"{val} -> {idx}\n")
            break


def play():

    for i in range(MAGIC_NUMBER):
        print(f"Turn {i+1}:")
        if i % 2 == 0:
            pick("X")
        else:
            pick("O")

        draw_board()

        winner = check_if_won()
        if winner:
            print(f"We have a winner! Congratualtions [{winner}] !!!\n")
            break
    else:
        print("We have a tie!\n")


if __name__ == "__main__":
    play()
