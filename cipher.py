"""
RULES FOR MY CIPHER

 RULE ONE: divide letter into two groups.
 Group one is 1 stroke letters (it takes 1 stroke to write the letter without overlapping [in capitals])
 Group two is 2 or more stroke letters (it takes 2+ stroke to write the letter without overlapping [in capitals])
    Group one: {C, I, J, L, M, N, O, S, U, V, W, Z}
    Group two: {A, B, D, E, F, G, H, K, P, Q, R, T, X, Y}

RULE TWO: sort the groups into reverse alphabetical order.
    Then combine the two groups, with group one first and group two second

        New Group: {Z, W, V, U, S, O, N, M, L, J, I, C, Y, X, T, R, Q, P, K, H, G, F, E, D, B, A}

RULE THREE: Numbers are sorted using letters.
    Each letter has been reassigned based of there new place in the alphabet

    New Letter placements:
    |A|B|B|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|
    |Z|W|V|U|S|O|N|M|L|J|I|C|Y|X|T|R|Q|P|K|H|G|F|E|D|B|A|

"""


def secret_message(message: str) -> str:
    """
    Return a new string with encrypted message in letters

    >>> secret_message('abcdefghijklmnopqrstuvwxyz')
    'zwvusonmljicyxtrqpkhgfedba'
    >>> secret_message('I think that MAT102 is going to be the death of me XD!')
    'L hmlxi hmzh YZH102 lk ntlxn ht ws hms uszhm to ys DU!'
    """
    secret = ''

    for ch in message:
        if not ch.isalpha():
            secret += ch
        elif ch == 'a':
            secret += chr(ord('a') + 25)
        elif ch == 'b':
            secret += chr(ord('b') + 21)
        elif ch == 'c':
            secret += chr(ord('c') + 19)
        elif ch == 'd':
            secret += chr(ord('d') + 17)
        elif ch == 'e':
            secret += chr(ord('e') + 14)
        elif ch == 'f':
            secret += chr(ord('f') + 9)
        elif ch == 'g':
            secret += chr(ord('g') + 7)
        elif ch == 'h':
            secret += chr(ord('h') + 5)
        elif ch == 'i':
            secret += chr(ord('i') + 3)
        elif ch == 'j':
            secret += chr(ord('j') + 0)
        elif ch == 'k':
            secret += chr(ord('k') - 2)
        elif ch == 'l':
            secret += chr(ord('l') - 9)
        elif ch == 'm':
            secret += chr(ord('m') + 12)
        elif ch == 'n':
            secret += chr(ord('n') + 10)
        elif ch == 'o':
            secret += chr(ord('o') + 5)
        elif ch == 'p':
            secret += chr(ord('p') + 2)
        elif ch == 'q':
            secret += chr(ord('q') + 0)
        elif ch == 'r':
            secret += chr(ord('r') - 2)
        elif ch == 's':
            secret += chr(ord('s') - 8)
        elif ch == 't':
            secret += chr(ord('t') - 12)
        elif ch == 'u':
            secret += chr(ord('u') - 14)
        elif ch == 'v':
            secret += chr(ord('v') - 16)
        elif ch == 'w':
            secret += chr(ord('w') - 18)
        elif ch == 'x':
            secret += chr(ord('x') - 20)
        elif ch == 'y':
            secret += chr(ord('y') - 23)
        elif ch == 'z':
            secret += chr(ord('z') - 25)
        elif ch == 'A':
            secret += chr(ord('A') + 25)
        elif ch == 'B':
            secret += chr(ord('B') + 21)
        elif ch == 'C':
            secret += chr(ord('C') + 19)
        elif ch == 'D':
            secret += chr(ord('D') + 17)
        elif ch == 'E':
            secret += chr(ord('E') + 14)
        elif ch == 'F':
            secret += chr(ord('F') + 9)
        elif ch == 'G':
            secret += chr(ord('G') + 7)
        elif ch == 'H':
            secret += chr(ord('H') + 5)
        elif ch == 'I':
            secret += chr(ord('I') + 3)
        elif ch == 'J':
            secret += chr(ord('J') + 0)
        elif ch == 'K':
            secret += chr(ord('K') - 2)
        elif ch == 'L':
            secret += chr(ord('L') - 9)
        elif ch == 'M':
            secret += chr(ord('M') + 12)
        elif ch == 'N':
            secret += chr(ord('N') + 10)
        elif ch == 'O':
            secret += chr(ord('O') + 5)
        elif ch == 'P':
            secret += chr(ord('P') + 2)
        elif ch == 'Q':
            secret += chr(ord('Q') + 0)
        elif ch == 'R':
            secret += chr(ord('R') - 2)
        elif ch == 'S':
            secret += chr(ord('S') - 8)
        elif ch == 'T':
            secret += chr(ord('T') - 12)
        elif ch == 'U':
            secret += chr(ord('U') - 14)
        elif ch == 'V':
            secret += chr(ord('V') - 16)
        elif ch == 'W':
            secret += chr(ord('W') - 18)
        elif ch == 'X':
            secret += chr(ord('X') - 20)
        elif ch == 'Y':
            secret += chr(ord('Y') - 23)
        elif ch == 'Z':
            secret += chr(ord('Z') - 25)
    secret += ''
    return secret
