import storyline as s

welcome = s.StoryChoice('Question','Path_one','Path_two')

inputs_one = iter(['Path_one','Path_one'])
inputs_two = iter(['Path_two','Path_two'])

def fake_input_one(prompt):
    return next(inputs_one)

def fake_input_two(prompt):
    return next(inputs_two)

class TestStoryChoice:
    def test_welcome(self):
        assert welcome.question == 'Question'
        assert welcome.path_one == 'Path_one'
        assert welcome.path_two == 'Path_two'

    def test_welcome_choice_path_one(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input_one)
        welcome.choice()
        assert welcome.progress == True
    
    def test_welcome_choice_path_two(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input_two)
        welcome.choice()
        assert welcome.progress == False