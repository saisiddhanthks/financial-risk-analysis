import pandas as pd
import numpy as np

def load_data():
    try:
        df = pd.read_csv("data/final_data.csv")
        return df
    except:
        return pd.DataFrame()

def process_data(df):
    if df.empty:
        return df

    def safe_div(a, b):
        if pd.isna(a) or pd.isna(b) or b == 0:
            return np.nan
        return a / b

    df["ROA"] = df.apply(lambda r: safe_div(r.get("profit"), r.get("total_assets")), axis=1)
    df["Debt"] = df["total_assets"] - df["equity"]
    df["Debt_to_Equity"] = df.apply(lambda r: safe_div(r.Debt, r.equity), axis=1)
    df["Loan_to_Deposit"] = df.apply(lambda r: safe_div(r.loans, r.deposits), axis=1)
    df["Liquidity"] = df.apply(lambda r: safe_div(r.cash, r.deposits), axis=1)
    df["Equity_Ratio"] = df.apply(lambda r: safe_div(r.equity, r.total_assets), axis=1)

    df["risk_score"] = (
        0.7 * df["Debt_to_Equity"].rank(pct=True)
        + 0.3 * (1 - df["ROA"].rank(pct=True))
    )

    q75 = df["risk_score"].quantile(0.75)
    q50 = df["risk_score"].quantile(0.50)

    df["risk_level"] = np.where(
        df["risk_score"] >= q75, "High",
        np.where(df["risk_score"] >= q50, "Medium", "Low")
    )

    return df

def get_summary(df):
    if df.empty:
        return {"error": "No data"}

    latest = df.iloc[-1]

    return {
        "ROA": latest.get("ROA"),
        "Debt_to_Equity": latest.get("Debt_to_Equity"),
        "Risk_Level": latest.get("risk_level")
    }