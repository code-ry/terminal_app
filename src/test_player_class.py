import main as m

inputs = iter(['A','B','C'])

def fake_input(prompt):
    return next(inputs)

class TestPlayer:
    def test_hero_pick_A(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input)
        m.player.hero_pick(m.brimly, m.mokimo, m.ailwyn)
        assert m.player.name == 'Brimly the Fierce'
    
    def test_hero_pick_B(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input)
        m.player.hero_pick(m.brimly, m.mokimo, m.ailwyn)
        assert m.player.attack == 40

    def test_hero_pick_C(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input)
        m.player.hero_pick(m.brimly, m.mokimo, m.ailwyn)
        assert m.player.hp == 30
