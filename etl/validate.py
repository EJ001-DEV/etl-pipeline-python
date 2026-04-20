def validate_data(df):
    issues = {}

    # detectar duplicados
    issues['duplicates'] = df[df.duplicated()]

    # detectar títulos cortos
    issues['short_titles'] = df[df['title_length'] < 5]

    return issues