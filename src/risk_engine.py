import pandas as pd

from analyzer import SecurityAnalyzer


def assign_severity(score):

    if score >= 80:
        return "HIGH"

    if score >= 40:
        return "MEDIUM"

    return "LOW"


class RiskEngine:

    def __init__(self, csv_path):

        self.analyzer = SecurityAnalyzer(
            csv_path
        )

    def calculate_risk_scores(self):

        stats = (
            self.analyzer
            .user_statistics()
            .reset_index()
        )

        failed = self.analyzer.failed_logins()

        after_hours = (
            self.analyzer
            .after_hours_activity()
        )

        stats["risk_score"] = 0

        for idx, row in stats.iterrows():

            score = 0

            downloads = row["total_downloads"]

            if downloads > 300:
                score += 40

            if downloads > 1000:
                score += 60

            user = row["user"]

            failed_count = (
                failed[
                    failed["user"] == user
                ]["failed_logins"]
            )

            if len(failed_count):

                score += int(
                    failed_count.iloc[0] * 2
                )

            after_count = (
                after_hours[
                    after_hours["user"] == user
                ]["after_hours_events"]
            )

            if len(after_count):

                score += int(
                    after_count.iloc[0]
                )

            stats.loc[idx, "risk_score"] = score

        stats["severity"] = (
            stats["risk_score"]
            .apply(assign_severity)
        )

        return stats.sort_values(
            by="risk_score",
            ascending=False
        )
    

if __name__ == "__main__":

    engine = RiskEngine(
        "../data/activity_logs.csv"
    )

    result = engine.calculate_risk_scores()

    print(
        result[
            ["user", "risk_score", "severity"]
        ].head(20)
    )