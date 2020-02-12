
def main():
    # Example Challenge
    print(anagram('aa','bb'))

def anagram(s, t):
    _s1 = sorted(list(s.replace(' ', '').lower()))
    _t1 = sorted(list(t.replace(' ', '').lower()))
    return _s1 == _t1

if __name__ == '__main__':
    main()