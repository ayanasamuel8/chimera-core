import pytest
# This import will fail because the code doesn't exist yet.
# This causes the desired ImportError for TDD.
from skills.trend_fetcher import TrendFetcher
from schemas.models import TrendSignal

def test_trend_fetcher_contract():
    """
    Ensures the TrendFetcher returns data matching the Spec.
    """
    fetcher = TrendFetcher()
    result = fetcher.get_trends(category="tech")
    
    # Assert return type matches Technical Spec
    assert isinstance(result, list)
    assert len(result) > 0
    assert isinstance(result[0], TrendSignal)
    assert 0.0 <= result[0].momentum_score <= 1.0
