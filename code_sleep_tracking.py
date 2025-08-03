# # Directory: sleep_tracking_toolkit
#
# # File: __init__.py
# # Marks the directory as a Python package
#
#
# # File: record.py
# class DailySleepRecord:
#     def __init__(self, date, segments):
#         # Initializes a new record with a date and a list of sleep segments (duration, quality)
#         self.date = date
#         self.segments = segments
#
#     def average_quality(self):
#         # Returns the average quality score for the day
#         if not self.segments:
#             return 0.0
#         avg = sum(score for _, score in self.segments) / len(self.segments)
#         return round(avg, 2)
#
#     def total_duration(self):
#         # Calculates total duration of sleep for the day
#         total = sum(duration for duration, _ in self.segments)
#         return round(total, 2)
#
#     def is_restful(self, duration_threshold=7, quality_threshold=75):
#         # Determines if all sleep segments meet duration and quality thresholds
#         return all(duration >= duration_threshold and quality >= quality_threshold
#                    for duration, quality in self.segments)
#
#     def average_sleep_score(self):
#         # Computes average sleep score using helper from utils
#         from .utils import compute_sleep_score
#         if not self.segments:
#             return 0.0
#         scores = [compute_sleep_score(duration, quality) for duration, quality in self.segments]
#         return round(sum(scores) / len(scores), 2)
#
#     def summary(self):
#         # Returns a summary dictionary with key stats and a quality label
#         from .utils import quality_label
#         avg_quality = self.average_quality()
#         total_duration = self.total_duration()
#         avg_sleep_score = self.average_sleep_score()
#         label = quality_label(avg_sleep_score)
#         return {
#             'date': self.date,
#             'avg_quality': avg_quality,
#             'total_duration': total_duration,
#             'avg_sleep_score': avg_sleep_score,
#             'quality_label': label
#         }
#
#
# # File: utils.py
# def quality_label(score):
#     # Converts numeric score into a quality label
#     if score >= 85:
#         return 'Excellent'
#     elif score >= 70:
#         return 'Good'
#     elif score >= 50:
#         return 'Fair'
#     else:
#         return 'Poor'
#
# def normalize_quality(score, current_max=100):
#     # Normalizes quality score to 0–100 scale
#     if current_max == 0:
#         return 0.0
#     return round((score / current_max) * 100, 2)
#
# def compute_sleep_score(duration, quality_score):
#     # Computes weighted sleep score capped at 100
#     base = min(duration / 8.0, 1.0) * 60 + quality_score * 0.4
#     return round(min(base, 100), 2)
#
#
# # File: analytics.py
# def overall_average_duration(records):
#     # Returns average sleep duration across all records
#     if not records:
#         return 0.0
#     total_duration = sum(record.total_duration() for record in records)
#     return round(total_duration / len(records), 2)
#
# def best_sleep_day(records):
#     # Returns the date with the highest average sleep score
#     if not records:
#         return None
#     return max(records, key=lambda r: r.average_sleep_score()).date
#
# def detect_under_sleep_days(records, threshold):
#     # Returns list of dates with any segment below threshold duration
#     under_days = []
#     for record in records:
#         if any(duration < threshold for duration, _ in record.segments):
#             under_days.append(record.date)
#     return under_days
#
# def detect_spike(durations, *, threshold=2):
#     # Detects large jumps between consecutive durations
#     if len(durations) < 2:
#         return False
#     return any(abs(durations[i] - durations[i - 1]) >= threshold for i in range(1, len(durations)))
#
# def duration_trend(durations):
#     # Returns list of 'up', 'down', 'same' to show change between durations
#     if len(durations) < 2:
#         return []
#     trend = []
#     for i in range(1, len(durations)):
#         if durations[i] > durations[i - 1]:
#             trend.append('up')
#         elif durations[i] < durations[i - 1]:
#             trend.append('down')
#         else:
#             trend.append('same')
#     return trend
#
# def average_sleep_score_across_days(records):
#     # Averages all segment-level sleep scores across days
#     from .utils import compute_sleep_score
#     scores = []
#     for record in records:
#         scores.extend([compute_sleep_score(d, q) for d, q in record.segments])
#     return round(sum(scores) / len(scores), 2) if scores else 0.0
