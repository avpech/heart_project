import pandas as pd


def to_snake_case(df: pd.DataFrame) -> pd.DataFrame:
    """Convert DataFrame column names to snake_case."""
    df.columns = (
        df.columns.str.strip()
        .str.replace(r'[ \-]', '_', regex=True)
        .str.replace(r'[\(\)]', '', regex=True).str.lower()
    )

    return df
