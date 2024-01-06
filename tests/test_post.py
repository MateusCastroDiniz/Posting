import pytest
from core.Posting.factories import PostFactory

@pytest.fixture
def post_created():
    return PostFactory(title='Primeiro test de task')

@pytest.mark.django_db
def test_create_post(post_created):
    assert post_created.title == 'Primeiro test de task'
