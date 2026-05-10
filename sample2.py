import os
from dotenv import load_dotenv
from vnstock import Quote, Company, Finance, Listing, change_api_key

load_dotenv()
change_api_key(os.environ["VNSTOCK_API_KEY"])

SYMBOL = "MSN"
SOURCE = "KBS"

quote = Quote(symbol=SYMBOL, source=SOURCE)
company = Company(symbol=SYMBOL, source=SOURCE)
finance = Finance(symbol=SYMBOL, source=SOURCE)
listing = Listing(source=SOURCE)


def price_history():
    df = quote.history(start="2024-01-01", end="2024-12-31", interval="1D")
    print(df.head())
    return df


def company_overview():
    info = company.overview()
    print(info)
    return info


def income_statement():
    df = finance.income_statement(period="year", lang="en")
    print(df.head())
    return df


def balance_sheet():
    df = finance.balance_sheet(period="year", lang="en")
    print(df.head())
    return df


def intraday_quotes():
    df = quote.intraday(page_size=100)
    print(df.head())
    return df


def list_all_symbols():
    df = listing.all_symbols()
    print(df.head(20))
    return df


if __name__ == "__main__":
    print("=== Price History ===")
    price_history()

    print("\n=== Company Overview ===")
    company_overview()

    print("\n=== Income Statement ===")
    income_statement()

    print("\n=== Balance Sheet ===")
    balance_sheet()

    print("\n=== Intraday Quotes ===")
    intraday_quotes()

    print("\n=== All Symbols ===")
    list_all_symbols()
