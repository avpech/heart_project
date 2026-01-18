import pandas as pd
from pydantic import TypeAdapter, ValidationError

from src.api.schemas import HeartDataRow
from src.utils import to_snake_case

row_adapter = TypeAdapter(HeartDataRow)


def validate_csv_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = to_snake_case(df)

    errors = []

    expected_columns = list(row_adapter.core_schema['schema']['fields'].keys())

    missing_cols = set(expected_columns) - set(df.columns)
    if missing_cols:
        raise ValueError({
            "message": "CSV is missing required columns",
            "missing_columns": list(missing_cols),
        })

    df_valid = df[expected_columns]

    for idx, row in enumerate(df_valid.itertuples(index=False, name=None)):
        record = {
            col: (val if pd.notna(val) else None)
            for col, val in zip(df_valid.columns, row)
        }

        try:
            row_adapter.validate_python(record)
        except ValidationError as e:
            errors.append(
                {
                    "row": idx + 1,
                    "errors": e.errors(),
                }
            )
    if errors:
        raise ValueError(
            {
                "message": "CSV validation failed",
                "rows_with_errors": errors,
            }
        )

    return df_valid
