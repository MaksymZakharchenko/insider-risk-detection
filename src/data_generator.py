import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

EVENT_TYPES = [
    "login",
    "logout",
    "file_download",
    "file_upload",
    "email_sent",
    "usb_copy",
    "failed_login"
]


def generate_normal_user_activity(user_id, num_events=100):

    records = []

    start_date = datetime.now() - timedelta(days=30)

    for _ in range(num_events):

        event_time = start_date + timedelta(
            minutes=random.randint(0, 43200)
        )

        event = random.choice(EVENT_TYPES[:5])

        records.append(
            {
                "user": user_id,
                "timestamp": event_time,
                "event": event,
                "file_count": random.randint(1, 10)
            }
        )

    return records


def generate_suspicious_user_activity(user_id):

    records = []

    start_date = datetime.now() - timedelta(days=30)

    for _ in range(50):

        event_time = start_date + timedelta(
            minutes=random.randint(0, 43200)
        )

        records.append(
            {
                "user": user_id,
                "timestamp": event_time,
                "event": "file_download",
                "file_count": random.randint(100, 500)
            }
        )

    for _ in range(15):

        event_time = start_date + timedelta(
            minutes=random.randint(0, 43200)
        )

        records.append(
            {
                "user": user_id,
                "timestamp": event_time,
                "event": "failed_login",
                "file_count": 0
            }
        )

    return records


def generate_dataset():

    data = []

    for i in range(45):
        user = fake.user_name()
        data.extend(generate_normal_user_activity(user))

    for i in range(5):
        user = f"suspicious_user_{i}"
        data.extend(generate_suspicious_user_activity(user))

    df = pd.DataFrame(data)

    df.to_csv(
        "../data/activity_logs.csv",
        index=False
    )

    print(f"Generated {len(df)} events")


if __name__ == "__main__":
    generate_dataset()