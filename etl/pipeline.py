from etl.extract import extract_from_api
from etl.transform import transform_posts
from etl.validate import validate_data
from etl.upsert import upsert_posts
from db.connection import engine

def run_pipeline():

    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        df = extract_from_api(url)

        df = transform_posts(df)

        issues = validate_data(df)

        upsert_posts(df, engine)

        print("Pipeline ejecutado correctamente")
        print("Issues:", {k: len(v) for k, v in issues.items()})

    except Exception as e:
        print(f"Error: {e}")