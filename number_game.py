
def play(low, high):
    half =  low + (high-low)/2
    print half
    answer = raw_input('(h)igh or (l)ow: ')
    if answer is 'h':
        return play(low, half-1)
    else:
        return play(half+1, high)
