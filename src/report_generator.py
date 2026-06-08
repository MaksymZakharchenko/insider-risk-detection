from risk_engine import RiskEngine


def generate_html_report():

    engine = RiskEngine(
        "../data/activity_logs.csv"
    )

    results = engine.calculate_risk_scores()

    html_table = results.to_html(
        index=False,
        classes="risk-table"
    )

    results = results[
    results["severity"] != "LOW"
    ]


    html = f"""
    <html>
    <head>
        <title>Insider Risk Report</title>

        <style>

            body {{
                font-family: Arial;
                margin: 40px;
            }}

            table {{
                border-collapse: collapse;
                width: 100%;
            }}

            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
            }}

            th {{
                background-color: #f4f4f4;
            }}

            img {{
                max-width: 100%;
                border: 1px solid #ddd;
                margin-bottom: 20px;
            }}

        </style>

    </head>

    <body>

        <h1>Insider Risk Report</h1>

        <h2>Visual Analytics</h2>

        <img src="charts/top_risk_users.png">

        <img src="charts/risk_distribution.png">

        <img src="charts/severity_distribution.png">

        <img src="charts/activity_by_hour.png">

        <h2>Detected Users</h2>

        {html_table}

    </body>

    </html>
    """

    with open(
        "../reports/risk_report.html",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(html)

    print("Report generated successfully.")


if __name__ == "__main__":
    generate_html_report()