import sqlite3

def run_query(query: str) -> list:
    try:
        conn = sqlite3.connect('./chinook.db')
        cur = conn.cursor()
        cur.execute(query)  # ('''
        # SELECT * FROM customers;
        # ''')

        # print(cur.fetchall())
        results = cur.fetchall()
        return results
    except Exception:
        return None
    finally:
        conn.close()

def ordering(query_param) -> str:
    """
    country,-city
    """
    result = []
    for elem in query_param.split(','):

        if '-' in elem:
            result.append(f'{elem[1:].capitalize()} DESC')
        else:
            result.append(elem.capitalize())

    return ', '.join(result)

def filter_and(query_param: str) -> str:
    """
    query_params = 'country:USD;city:Boston'

    ?filter=country:USD;city:Boston
    """

    pass

if __name__ == '__main__':
    assert ordering('country,-city') == 'Country, City DESC'
    assert ordering('country,-city') == 'Country DESC, City DESC'
    assert ordering('') == ''

    assert filter_and('country:USA;city:Boston') == "Country = 'USA' AND City = 'Boston'"
    assert filter_and('country:USA') == "Country = 'USA'"



#rr = run_query()
