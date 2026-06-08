import pandas as pd
import matplotlib.pyplot as plt

from risk_engine import RiskEngine

from analyzer import SecurityAnalyzer

def load_results():

    engine = RiskEngine(
        "../data/activity_logs.csv"
    )

    return engine.calculate_risk_scores()

def top_risk_users_chart(df):

    top_users = df.head(10)

    plt.figure(figsize=(10, 6))

    plt.bar(
        top_users["user"],
        top_users["risk_score"]
    )

    plt.title("Top Risk Users")

    plt.xlabel("User")
    plt.ylabel("Risk Score")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(
        "../reports/charts/top_risk_users.png"
    )

    plt.close()

def risk_distribution_chart(df):

    plt.figure(figsize=(10, 6))

    plt.hist(
        df["risk_score"],
        bins=15
    )

    plt.title(
        "Risk Score Distribution"
    )

    plt.xlabel("Risk Score")
    plt.ylabel("Users")

    plt.tight_layout()

    plt.savefig(
        "../reports/charts/risk_distribution.png"
    )

    plt.close()

def severity_chart(df):

    counts = (
        df["severity"]
        .value_counts()
    )

    plt.figure(figsize=(8, 5))

    plt.bar(
        counts.index,
        counts.values
    )

    plt.title(
        "Severity Distribution"
    )

    plt.xlabel("Severity")
    plt.ylabel("Count")

    plt.tight_layout()

    plt.savefig(
        "../reports/charts/severity_distribution.png"
    )

    plt.close()

def activity_hours_chart():

    analyzer = SecurityAnalyzer(
        "../data/activity_logs.csv"
    )

    activity = (
        analyzer.hourly_activity()
    )

    plt.figure(figsize=(10, 6))

    plt.plot(
        activity["hour"],
        activity["events"]
    )

    plt.title(
        "User Activity by Hour"
    )

    plt.xlabel("Hour")

    plt.ylabel("Events")

    plt.grid()

    plt.tight_layout()

    plt.savefig(
        "../reports/charts/activity_by_hour.png"
    )

    plt.close()

if __name__ == "__main__":

    df = load_results()

    top_risk_users_chart(df)

    risk_distribution_chart(df)

    severity_chart(df)

    activity_hours_chart() 

    print(
        "Charts generated successfully."
    )