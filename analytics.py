from utils import round_to, compute_sleep_score

def overall_average_duration(records):
    if not records:
        return None

    # Flatten all durations from all records
    durations = [duration for record in records for duration, _ in record.segments]

    if not durations:
        return round_to(0.0)

    return round_to(sum(durations) / len(durations))

def best_sleep_day(records):
    if not records:
        return None

    max_sleeps_score_record = max(records, key=lambda r: r.average_sleep_score())
    return max_sleeps_score_record.date

def detect_under_sleep_days(records, threshold):
    under_sleep_days = []
    for record in records:
        if any(duration < threshold for duration, _ in record.segments): under_sleep_days.append(record.date)

    return under_sleep_days

def detect_spike(durations, *, threshold=2):
    if len(durations) < 2:
        return False

    return any(abs(durations[i] - durations[i - 1]) >= threshold
               for i in range(1, len(durations)))

def duration_trend(durations):
    if not isinstance(durations, list) or len(durations) < 2:
        return []

    trend = []
    for i in range(1, len(durations)):
        if durations[i] > durations[i - 1]:
            trend.append('up')
        elif durations[i] < durations[i - 1]:
            trend.append('down')
        else:
            trend.append('same')

    return trend

def average_sleep_score_across_days(records):
    if not records:
        return round_to(0.0)

    # Collect all segment-level sleep scores using compute_sleep_score
    scores = [
        compute_sleep_score(duration, quality)
        for record in records
        for duration, quality in record.segments
    ]

    return round_to(sum(scores) / len(scores)) if scores else round_to(0.0)
