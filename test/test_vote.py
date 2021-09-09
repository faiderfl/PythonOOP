from models.vote import Vote
import pytest

def test_vote_region():
    vote= Vote(123, ['Medellin'])
    vote.region= 'Medellin'
    assert vote.region == 'Medellin'

def test_vote_region_fail():
    with pytest.raises(ValueError) as e:
        vote= Vote(123, ['Medellin'])
        vote.region= 'Bogota'
    assert str(e.value) == 'Region Bogota is not allowed'