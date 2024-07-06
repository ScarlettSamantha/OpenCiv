import pytest
from openciv.gameplay.tech import Tech
from openciv.engine.managers.tech import TechManager


class MockGame:
    pass

@pytest.fixture
def tech_manager():
    game = MockGame()
    return TechManager(game)

def test_add_tech_to_queue(tech_manager):
    tech = Tech("Tech1")
    tech_manager.add_tech_to_queue(tech)
    assert tech_manager.queue[0] == tech

def test_reorder(tech_manager):
    tech1 = Tech("Tech1")
    tech2 = Tech("Tech2")
    tech_manager.add_tech_to_queue(tech1)
    tech_manager.add_tech_to_queue(tech2)
    tech_manager.queue[0] = tech2
    tech_manager.queue[1] = tech1
    tech_manager.reorder()
    assert list(tech_manager.queue.values()) == [tech2, tech1]

def test_do_first_queue(tech_manager):
    tech1 = Tech("Tech1")
    tech2 = Tech("Tech2")
    tech_manager.add_tech_to_queue(tech1)
    tech_manager.do_first_queue(tech2)
    assert tech_manager.queue[0] == tech2

def test_delete_tech(tech_manager):
    tech = Tech("Tech1")
    tech_manager.add_tech(tech)
    tech_manager.delete_tech(tech)
    assert tech not in tech_manager.registered_techs

def test_add_tech(tech_manager):
    tech = Tech("Tech1")
    tech_manager.add_tech(tech)
    assert tech in tech_manager.registered_techs

def test_current_tech(tech_manager):
    tech = Tech("Tech1")
    tech_manager.add_tech_to_queue(tech)
    assert tech_manager.current_tech() == tech

def test_next_tech(tech_manager):
    tech1 = Tech("Tech1")
    tech2 = Tech("Tech2")
    tech_manager.add_tech_to_queue(tech1)
    tech_manager.add_tech_to_queue(tech2)
    assert tech_manager.next_tech() == tech2

def test_current_tech_empty_queue(tech_manager):
    assert tech_manager.current_tech() is None

def test_next_tech_empty_queue(tech_manager):
    assert tech_manager.next_tech() is None

def test_process_queue(tech_manager):
    tech1 = Tech("Tech1")
    tech2 = Tech("Tech2")
    tech_manager.add_tech_to_queue(tech1)
    tech_manager.add_tech_to_queue(tech2)
    tech_manager.process_queue()
    assert tech_manager.current_tech() == tech2
    assert tech_manager.next_tech() is None

def test_complete_research(tech_manager):
    tech1 = Tech("Tech1")
    tech2 = Tech("Tech2")
    tech_manager.add_tech_to_queue(tech1)
    tech_manager.add_tech_to_queue(tech2)
    tech_manager.add_science(tech_manager._needed_science)
    assert tech_manager._current_science_pool == 0
    assert tech_manager.current_tech() == tech2

def test_add_science_no_auto_complete(tech_manager):
    tech1 = Tech("Tech1")
    tech_manager.add_tech_to_queue(tech1)
    tech_manager.add_science(tech_manager._needed_science, auto_complete_tech=False)
    assert tech_manager._current_science_pool == tech_manager._needed_science
    assert tech_manager.current_tech() == tech1

def test_remove_science(tech_manager):
    tech_manager.add_science(10)
    tech_manager.remove_science(5)
    assert tech_manager._current_science_pool == 5

def test_science_processing(tech_manager):
    # Initialize techs and add to queue
    tech1 = Tech("Tech1")
    tech2 = Tech("Tech2")
    tech3 = Tech("Tech3")
    tech_manager.add_tech_to_queue(tech1)
    tech_manager.add_tech_to_queue(tech2)
    tech_manager.add_tech_to_queue(tech3)

    # Set needed science for each tech
    tech_manager._needed_science = 10

    # Add science and check progress after each addition
    tech_manager.add_science(5, auto_complete_tech=True)
    assert tech_manager._current_science_pool == 5
    assert tech_manager.current_tech() == tech1

    tech_manager.add_science(5, auto_complete_tech=True)
    assert tech_manager._current_science_pool == 0
    assert tech_manager.current_tech() == tech2

    tech_manager.add_science(15, auto_complete_tech=True)
    assert tech_manager._current_science_pool == 5
    assert tech_manager.current_tech() == tech3

    # Ensure queue is processed correctly
    tech_manager.add_science(5, auto_complete_tech=True)
    assert tech_manager._current_science_pool == 0
    assert tech_manager.current_tech() is None
    assert tech_manager.next_tech() is None

    # Re-add science to ensure it handles an empty queue correctly
    tech_manager.add_science(10, auto_complete_tech=True)
    assert tech_manager._current_science_pool == 10
    assert tech_manager.current_tech() is None
