from src.temporal_benchmark import signal, threshold_events, latency_fading, score


def test_sparse_encodings_reduce_transfer():
    s=signal()
    assert len(threshold_events(s)) < len(s)/10
    assert len(latency_fading(s)) < len(s)/10


def test_event_detection_is_nonzero():
    s=signal()
    assert score(threshold_events(s)) > 0
    assert score(latency_fading(s)) > 0
