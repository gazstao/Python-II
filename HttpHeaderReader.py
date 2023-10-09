import requests


def getheaders(website: object) -> object:
    try:
        response = requests.get(website, timeout=20)
        print(f"Website: {website}")
        print(f"\nStatus code: {str(response.status_code)}")
        print("\n___________________Headers: ")
        for header, value in response.headers.items():
            print(header, " - ", value)
        print("\n___________________Headers Request:")
        for header, value in response.request.headers.items():
            print(header, " - ", value)
    except Exception as e:
        print(f"Algo deu errado =(   {e}")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Http Header Reader")
    parser.add_argument("website", nargs="?", help="Website to read the header", default=None)
    args = parser.parse_args()

    if args.website is None:
        print("Argumentos faltando! Exemplo de uso: $ python HttpHeaderReader.py 'https://gastao.app.br'")
        args.website = 'http://192.168.0.32:8080'

    getheaders(args.website)
