from typing import List


def triple(alist, blist, clist):
    for a in alist:
        for b in blist:
            for c in clist:
                yield a, b, c


def double(alist, blist):
    for a in alist:
        for b in blist:
            yield a, b


def triplef(alist, blist, clist, func):
    for a in alist:
        for b in blist:
            for c in clist:
                yield func(a, b, c)


def doublef(alist, blist, func):
    for a in alist:
        for b in blist:
            yield func(a, b)


def eci_url(a, b, c):
    url: str = f'https://oec.world/olap-proxy/data.jsonrecords?' \
               f'cube=complexity_eci_a_{b}_{a}&' \
               f'Year={c}&' \
               f'drilldowns=Country,Year,ECI+Rank&' \
               f'measures=ECI&' \
               f'parents=true&' \
               f'sparse=true'

    return url


def pci_url(a, b, c):
    url: str = f'https://oec.world/olap-proxy/data.jsonrecords?' \
               f'cube=complexity_pci_a_{b}_{a}&' \
               f'Year={c}&' \
               f'drilldowns=HS6,PCI+Rank,Year&' \
               f'measures=PCI&' \
               f'parents=true&' \
               f'sparse=true'

    return url


def main() -> None:
    print('hi')

    depth: List[str] = ['hs4', 'hs6']
    rev: List[str] = [
        'hs92',
        'hs96',
        'hs02',
        'hs07',
    ]

    years = range(1965, 2021)
    hs6: List[str] = open('./hs6.csv').readlines()
    countries: List[str] = open('./country-code.csv').readlines()

    for a in triplef(depth, rev, years, eci_url):
        print(a)

    for a in triplef(depth, rev, years, pci_url):
        print(a)


if __name__ == '__main__':
    main()
