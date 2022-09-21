import storyline as s

player = s.Player()
def fake_input(prompt):
    return 'a'


class TestPlayer:
    def test_hero_pick(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input)
        player.hero_pick()
        assert player.hero == 'a'
    
    def test_set(self):
        player.set()
        assert player.name == 'Grimly The Fierce'
        assert player.attack == 10