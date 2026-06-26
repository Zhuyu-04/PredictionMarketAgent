import pytest
from prediction_market_agent.analysis.trackers import ProbabilityTracker
def test_tracker_update_and_change():
    tracker = ProbabilityTracker()
    tracker.update("test", 0.4)
    tracker.update("test", 0.5)
    change = tracker.get_change("test", lookback=1)
    assert change == pytest.approx(0.1)