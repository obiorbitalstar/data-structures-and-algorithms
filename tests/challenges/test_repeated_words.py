from data_structures_and_algorithms.challenges.repeated_word.repeated_word import repeated_word

def test_normal_string():
    x = "Once upon a time, there was a brave princess who..."
    actual = repeated_word(x)
    expected = 'a'
    assert expected == actual

def test_string_with_commas():
    x = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    actual = repeated_word(x)
    expected = 'summer'
    assert expected == actual
def test_really_long_string():
    x = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    actual = repeated_word(x)
    expected = 'it'
    assert expected == actual
def test_no_repetaetd_word():
    x = "nothing is repeated"
    actual = repeated_word(x)
    expected = None
    assert expected == actual
