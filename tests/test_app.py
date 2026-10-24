from pathlib import Path
from streamlit.testing.v1 import AppTest

def test_render_empty(tmp_path,monkeypatch):
    from research import store
    monkeypatch.setattr(store,'DB_PATH',tmp_path/'absent.sqlite')
    at=AppTest.from_file(str(Path(__file__).resolve().parents[1]/'app.py'),default_timeout=15).run()
    assert not at.exception
    assert any('has not published' in x.value for x in at.info)

def test_render_manual_and_switch(fixture_db,monkeypatch):
    from research import store
    import urllib.request
    monkeypatch.setattr(store,'DB_PATH',fixture_db)
    original_connect=store.connect
    def fixture_connect(path=None,readonly=True):return original_connect(fixture_db,readonly)
    monkeypatch.setattr(store,'connect',fixture_connect)
    def deny(*a,**kw):raise AssertionError('Interactive rendering attempted network request')
    monkeypatch.setattr(urllib.request,'urlopen',deny)
    at=AppTest.from_file(str(Path(__file__).resolve().parents[1]/'app.py'),default_timeout=20).run()
    assert not at.exception
    at.radio[0].set_value('Manual teams').run()
    assert not at.exception
    assert any('STATISTICAL CONFIDENCE LEVELS' in x.value for x in at.markdown)
    next(x for x in at.selectbox if x.label=='Team A (away by default)').set_value('2').run()
    assert not at.exception
    at.checkbox[1].check().run()
    assert not at.exception
    assert all('TEST FIXTURE' in x.value or 'old' in x.value for x in at.warning)


def test_division_dropdown_separates_teams_and_schedules(fixture_db,monkeypatch):
    from research import store
    monkeypatch.setattr(store,'DB_PATH',fixture_db)
    original_connect=store.connect
    def fixture_connect(path=None,readonly=True):return original_connect(fixture_db,readonly)
    monkeypatch.setattr(store,'connect',fixture_connect)
    with original_connect(fixture_db,False) as c:
        c.execute("UPDATE team_seasons SET division='FCS' WHERE team_id IN ('2','3')")
    at=AppTest.from_file(str(Path(__file__).resolve().parents[1]/'app.py'),default_timeout=20).run()
    at.radio[0].set_value('Manual teams').run()
    team_a=lambda:next(x for x in at.selectbox if x.label=='Team A (away by default)')
    assert set(team_a().options)=={'Test Team 0','Test Team 1'}
    at.selectbox(key='division').set_value('FCS').run()
    assert not at.exception
    assert set(team_a().options)=={'Test Team 2','Test Team 3'}
    at.date_input[0].set_value(__import__('datetime').date(2025,1,1)).run()
    at.radio[0].set_value('Scheduled matchup').run()
    matchup=next(x for x in at.selectbox if x.label=='Scheduled matchup')
    assert matchup.options and all('Test Team 0' not in x and 'Test Team 1' not in x for x in matchup.options)
    at.selectbox(key='division').set_value('FBS').run()
    assert not at.exception
    matchup=next(x for x in at.selectbox if x.label=='Scheduled matchup')
    assert matchup.options and all('Test Team 2' not in x and 'Test Team 3' not in x for x in matchup.options)
