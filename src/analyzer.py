import pandas as pd


class SecurityAnalyzer:

    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)

        self.df["timestamp"] = pd.to_datetime(
            self.df["timestamp"]
        )

    def user_statistics(self):

        stats = self.df.groupby("user").agg(
            total_events=("event", "count"),
            total_downloads=("file_count", "sum")
        )

        return stats

    def failed_logins(self):

        failed = (
            self.df[self.df["event"] == "failed_login"]
            .groupby("user")
            .size()
            .reset_index(name="failed_logins")
        )

        return failed

    def usb_activity(self):

        usb = (
            self.df[self.df["event"] == "usb_copy"]
            .groupby("user")
            .size()
            .reset_index(name="usb_events")
        )

        return usb

    def after_hours_activity(self):

        self.df["hour"] = self.df["timestamp"].dt.hour

        after_hours = self.df[
            (self.df["hour"] >= 22)
            | (self.df["hour"] <= 5)
        ]

        return (
            after_hours
            .groupby("user")
            .size()
            .reset_index(name="after_hours_events")
        )

def hourly_activity(self):

    self.df["hour"] = (
        self.df["timestamp"]
        .dt.hour
    )

    return (
        self.df.groupby("hour")
        .size()
        .reset_index(name="events")
    )
    
if __name__ == "__main__":

    analyzer = SecurityAnalyzer(
        "../data/activity_logs.csv"
    )

    print("\nUSER STATS")
    print(analyzer.user_statistics().head())

    print("\nFAILED LOGINS")
    print(analyzer.failed_logins().head())

    print("\nAFTER HOURS")
    print(analyzer.after_hours_activity().head())