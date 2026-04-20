from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session
from db.models import Post

def upsert_posts(df, engine):

    data = df.to_dict(orient='records')

    stmt = insert(Post).values(data)

    stmt = stmt.on_conflict_do_nothing(index_elements=['id'])

    with engine.begin() as conn:
        conn.execute(stmt)

'''
def upsert_posts(df, engine):
    """
    Inserta datos evitando duplicados usando ON CONFLICT
    """

    with Session(engine) as session:
        for _, row in df.iterrows():

            stmt = insert(Post).values(
                id=row['id'],
                user_id=row['user_id'],
                title=row['title'],
                body=row.get('body'),
                title_length=row['title_length']
            )

            # evita duplicados por PK
            stmt = stmt.on_conflict_do_nothing(index_elements=['id'])

            session.execute(stmt)

        session.commit()
        '''