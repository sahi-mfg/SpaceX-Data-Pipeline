import singer  # type: ignore
import pandas as pd  # type: ignore
import math

LOGGER = singer.get_logger()  # type: ignore

# Updated schema to match likely data types
schema = {
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "date_utc": {"type": "string", "format": "date-time"},
        "engines": {"type": "number"},  # assuming integer count
        "landing_legs": {"type": "number"},  # assuming integer count
        "cost_per_launch": {"type": "number"},
        "success_rate_pct": {"type": "number"},
        "first_flight": {"type": "string"},
        "country": {"type": "string"},
        "company": {"type": "string"},
        "description": {"type": "string"},
        "wikipedia": {"type": "string"},
        "boosters": {"type": "number"},  # assuming integer count
        "stages": {"type": "number"},
        "active": {"type": "boolean"},
        "type": {"type": "string"},
        "flickr_images": {"type": "array"},
        "height": {"type": "object"},
        "diameter": {"type": "object"},
        "mass": {"type": "object"},
        "payload_weights": {"type": "array"},
        "first_stage": {"type": "object"},
    }
}


# Helper function to clean out-of-range float values
def clean_record(record):
    for key, value in record.items():
        if isinstance(value, float) and (math.isnan(value) or math.isinf(value)):
            record[key] = None  # Replace problematic values with None
    return record


def main() -> None:
    url: str = "https://api.spacexdata.com/v4/launches"
    df = pd.read_json(url)

    records = df.to_dict(orient="records")

    # Clean each record before passing it to `write_records`
    cleaned_records = [clean_record(record) for record in records]

    singer.write_schema("launches", schema, "id")
    singer.write_records("launches", cleaned_records)


if __name__ == "__main__":
    main()
