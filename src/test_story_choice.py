import storyline as s

welcome = s.StoryChoice('hello','yes')
def fake_input():
    return 'no'

class TestStoryChoice:
    def test_welcome(self):
        assert welcome.question == 'hello'
        assert welcome.answer == 'yes'

    def test_welcome_choice(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input)
        welcome.choice()
        assert welcome.progress == False