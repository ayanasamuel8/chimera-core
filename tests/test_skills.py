import pytest
from pydantic import ValidationError

# We are testing against the Interface, not the implementation yet.
# Note: The 'skills' module does not exist yet. This is intentional.
# The AI's job in the future is to make this import work.
try:
    from skills.trend_fetcher import TrendFetcher
    from schemas.models import TrendSignal
except ImportError:
    pytest.skip("Skills module not yet implemented", allow_module_level=True)

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