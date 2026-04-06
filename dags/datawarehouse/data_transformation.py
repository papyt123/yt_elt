import logging
from datetime import datetime

logger = logging.getLogger(__name__)


def transform_data(row):
    """Transform a staging row into the core table format."""
    try:
        duration_str = row["Duration"]
        duration_time = parse_iso8601_duration(duration_str)
        duration_seconds = iso8601_duration_to_seconds(duration_str)
        video_type = "Short" if duration_seconds <= 60 else "Regular"

        upload_date = row["Upload_Date"]
        if isinstance(upload_date, str):
            upload_date = datetime.fromisoformat(upload_date.replace("Z", "+00:00"))

        transformed_row = {
            "Video_ID": row["Video_ID"],
            "Video_Title": row["Video_Title"],
            "Upload_Date": upload_date,
            "Duration": duration_time,
            "Video_Type": video_type,
            "Video_Views": row["Video_Views"],
            "Likes_Count": row["Likes_Count"],
            "Comments_Count": row["Comments_Count"],
        }

        logger.info(f"Transformed row for Video_ID={row['Video_ID']}")
        return transformed_row

    except Exception as e:
        logger.error(f"Error transforming row for Video_ID={row.get('Video_ID')} - {e}")
        raise e


def parse_iso8601_duration(duration_str):
    import re

    pattern = r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?"
    match = re.match(pattern, duration_str)
    if not match:
        return "00:00:00"

    hours = int(match.group(1) or 0)
    minutes = int(match.group(2) or 0)
    seconds = int(match.group(3) or 0)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def iso8601_duration_to_seconds(duration_str):
    import re

    pattern = r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?"
    match = re.match(pattern, duration_str)
    if not match:
        return 0

    hours = int(match.group(1) or 0)
    minutes = int(match.group(2) or 0)
    seconds = int(match.group(3) or 0)
    return hours * 3600 + minutes * 60 + seconds
