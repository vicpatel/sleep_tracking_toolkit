from utils import round_to, compute_sleep_score, quality_label

class DailySleepRecord:
    """
    Represents a daily sleep record.

    Attributes:
        date (str): Date of the record, e.g., '2025-04-29'.
        segments (list[tuple[float, float]]): List of (duration, quality_score) tuples, where
            duration is in hours (float) &
            quality_score is a value from 0 to 100 (int or float).
    """

    def __init__(self, date: str, segments: list[tuple[float, float]]):
        # Initialize the record with a date and sleep segments
        self.date = date
        self.segments = segments

    def average_quality(self):
        # Return 0.0 if there are no segments
        if not self.segments:
            return 0.0
        # Calculate the average quality score across all segments
        return round_to(sum(score for _, score in self.segments) / len(self.segments))

    def total_duration(self):
        # Return 0.0 if there are no segments
        if not self.segments:
            return 0.0
        # Calculate the total sleep duration across all segments
        return round_to(sum(duration for duration, _ in self.segments))

    def is_restful(self, duration_threshold=7, quality_threshold=75):
        # Check if all segments meet the restful criteria
        return all(duration >= duration_threshold and quality >= quality_threshold
                   for duration, quality in self.segments)

    def average_sleep_score(self):
        # Return 0.0 if there are no segments
        if not self.segments:
            return 0.0
        # Compute sleep score for each segment and average them
        scores = [compute_sleep_score(duration, quality) for duration, quality in self.segments]
        return round_to(sum(scores) / len(scores))

    def summary(self):
        # Return a summary dictionary of the sleep record
        return {
            'date': self.date,
            'average_quality': self.average_quality(),
            'total_duration': self.total_duration(),
            'average_sleep_score': self.average_sleep_score(),
            'quality_label': quality_label(self.average_quality())
        }
