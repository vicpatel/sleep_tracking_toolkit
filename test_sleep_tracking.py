
import unittest
from sleep_tracking_toolkit.record import DailySleepRecord
from sleep_tracking_toolkit.utils import compute_sleep_score, quality_label, normalize_quality
from sleep_tracking_toolkit.analytics import (
    overall_average_duration, best_sleep_day,
    detect_under_sleep_days, detect_spike,
    duration_trend, average_sleep_score_across_days
)

class TestSleepTracking(unittest.TestCase):

    def setUp(self):
        self.records = [
            DailySleepRecord('2025-07-01', [(7.5, 80), (1.5, 90)]),
            DailySleepRecord('2025-07-02', [(6.0, 50)]),
            DailySleepRecord('2025-07-03', [(8.0, 95)])
        ]

    def test_average_quality(self):
        self.assertAlmostEqual(self.records[0].average_quality(), 85.0)

    def test_total_duration(self):
        self.assertAlmostEqual(self.records[0].total_duration(), 9.0)

    def test_is_restful(self):
        self.assertTrue(self.records[0].is_restful(1.0, 70))
        self.assertFalse(self.records[1].is_restful())

    def test_average_sleep_score(self):
        score = self.records[0].average_sleep_score()
        self.assertIsInstance(score, float)

    def test_summary(self):
        summary = self.records[0].summary()
        self.assertIn('date', summary)
        self.assertIn('quality_label', summary)

    def test_compute_sleep_score(self):
        score = compute_sleep_score(8.0, 90)
        self.assertAlmostEqual(score, 96.0)

    def test_quality_label(self):
        self.assertEqual(quality_label(90), 'Excellent')
        self.assertEqual(quality_label(72), 'Good')
        self.assertEqual(quality_label(60), 'Fair')
        self.assertEqual(quality_label(45), 'Poor')

    def test_normalize_quality(self):
        self.assertEqual(normalize_quality(50, 100), 50.0)
        self.assertEqual(normalize_quality(25, 50), 50.0)

    def test_overall_average_duration(self):
        avg = overall_average_duration(self.records)
        self.assertIsInstance(avg, float)

    def test_best_sleep_day(self):
        best_day = best_sleep_day(self.records)
        self.assertEqual(best_day, '2025-07-03')

    def test_detect_under_sleep_days(self):
        result = detect_under_sleep_days(self.records, threshold=7)
        self.assertIn('2025-07-02', result)

    def test_detect_spike(self):
        self.assertTrue(detect_spike([5, 9]))
        self.assertFalse(detect_spike([7, 7.5]))

    def test_duration_trend(self):
        trend = duration_trend([7, 8, 8, 6])
        self.assertEqual(trend, ['up', 'same', 'down'])

    def test_average_sleep_score_across_days(self):
        avg = average_sleep_score_across_days(self.records)
        self.assertGreater(avg, 0)

if __name__ == '__main__':
    unittest.main()
