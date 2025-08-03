# converts a numeric score into a descriptive quality label
def quality_label(score: float) -> str:
    """
        Converts a numeric sleep score into a descriptive quality label.

        Parameters:
            score (float): A value between 0 and 100.

        Returns:
            str: One of 'Excellent', 'Good', 'Fair', or 'Poor'.
        """
    # Explicitly handle invalid or negative inputs as 'Poor'
    if not isinstance(score, (int, float)) or score < 0:
        return 'Poor'  # For invalid or negative input
    if score >= 85:
        return 'Excellent'
    elif score >= 70:
        return 'Good'
    elif score >= 50:
        return 'Fair'
    else:
        return 'Poor'  # For valid scores below 50

# normalizes a score to a 0–100 scale based on a given current_max
def normalize_quality(score: float, current_max: float = 100) -> float:
    if not isinstance(score, (int, float)) or not isinstance(current_max, (int, float)):
        return 0.0
    if current_max <= 0:
        return 0.0
    normalized = (score / current_max) * 100
    return round(min(max(normalized, 0.0), 100.0), 2)

# computes a combined sleep score (0–100) based on weighted duration and quality
def compute_sleep_score(duration: float, quality_score: float) -> float:
    """
        Computes a sleep score out of 100 based on duration and quality.
        Duration is capped at 8.0 hours, and score is weighted:
          - 60% from duration (max 8 hours)
          - 40% from quality_score (0–100 scale)

        Returns:
            float: Sleep score between 0.0 and 100.0, rounded to two decimals.
        """
    if not isinstance(duration, (int, float)) or not isinstance(quality_score, (int, float)):
        return 0.0
    if duration < 0 or quality_score < 0:
        return 0.0

    duration_factor = min(duration / 8.0, 1.0) * 60
    quality_factor = quality_score * 0.4
    score = duration_factor + quality_factor
    return round_to(min(score, 100.0))

# rounds a value to a specified number of decimal places
def round_to(value: float, digits: int = 2) -> float:
    if not isinstance(value, (int, float)):
        return 0.0
    return round(value, digits)
