import singer
import pandas as pd


LOGGER = singer.get_logger()  # type: ignore

schema = {
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "date_utc": {"type": "string", "format": "date-time"},
        "engines": {"type": "string"},
        "landing_legs": {"type": "string"},
        "cost_per_launch": {"type": "number"},
        "success_rate_pct": {"type": "number"},
        "first_flight": {"type": "string"},
        "country": {"type": "string"},
        "company": {"type": "string"},
        "description": {"type": "string"},
        "wikipedia": {"type": "string"},
        "boosters": {"type": "string"},
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


def main() -> None:
    url: str = "https://api.spacexdata.com/v4/launches"
    df = pd.read_json(url)  # type: ignore

    records = df.to_dict(orient="records")  # type: ignore

    singer.write_schema("launches", schema, "id")  # type: ignore
    singer.write_records("launches", records)  # type: ignore


if __name__ == "__main__":
    main()
