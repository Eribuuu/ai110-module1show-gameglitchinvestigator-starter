from logic_utils import check_guess, get_range_for_difficulty

def test_range_for_easy():
    # Easy should return a range of 1 to 20
    result = get_range_for_difficulty("Easy")
    assert result == (1, 20)

def test_range_for_normal():
    # Normal should return a range of 1 to 50
    result = get_range_for_difficulty("Normal")
    assert result == (1, 50)

def test_range_for_hard():
    # Hard should return a range of 1 to 100
    result = get_range_for_difficulty("Hard")
    assert result == (1, 100)

def test_range_for_unknown_difficulty():
    # Any unrecognized difficulty should fall back to the default range of 1 to 100
    result = get_range_for_difficulty("Nightmare")
    assert result == (1, 100)

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"
