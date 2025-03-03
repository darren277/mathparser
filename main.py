""""""
import argparse
import requests
from bs4 import BeautifulSoup


def fetch_from_wikipedia(page, section_id):
    soup = BeautifulSoup(requests.get(f'https://en.wikipedia.org/wiki/{page}').text)
    section = soup.find('span', {'id': section_id}).parent.nextSibling.nextSibling
    return section


def main(src: str, latex: bool, mathml: bool):
    #from src.inprogress import parse_latex
    #from src.inprogress import parse_mathml
    #parsed = parse_latex(fetch_from_wikipedia('Discrete_cosine_transform', 'DCT-I').find('annotation', {'encoding': 'application/x-tex'}).text)
    #parsed = parse_mathml(fetch_from_wikipedia('Discrete_cosine_transform', 'DCT-I').find('annotation', {'encoding': 'application/x-tex'}).text)
    print(src)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('src')
    parser.add_argument('--latex', default=True)
    parser.add_argument('--mathml', default=False)

    args = parser.parse_args()
    print(args)
    main(args.src, args.latex, args.mathml)



