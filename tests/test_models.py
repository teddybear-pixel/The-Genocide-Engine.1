from src.genocide_engine.models import Entity


def test_entity_creation():
    entity = Entity(id="1", name="Test Entity")

    assert entity.id == "1"
    assert entity.name == "Test Entity"