from typing import List
from typing import Tuple


def quadf(alist, blist, clist, dlist, func):
    for a in alist:
        for b in blist:
            for c in clist:
                for d in dlist:
                    yield func(a, b, c, d)


def triplef(alist, blist, clist, func):
    for a in alist:
        for b in blist:
            for c in clist:
                yield func(a, b, c)


def doublef(alist, blist, func):
    for a in alist:
        for b in blist:
            yield func(a, b)


def eci_url(a, b, c,):
    url: str = f'https://oec.world/olap-proxy/data.jsonrecords?' \
               f'cube=complexity_eci_a_{b}_{a}&' \
               f'Year=2020&' \
               f'Country={c}&' \
               f'drilldowns=Country,Year,ECI+Rank&' \
               f'measures=ECI&' \
               f'parents=true&' \
               f'sparse=true'

    return url


def pci_url_hs4(a, b):
    url: str = f'https://oec.world/olap-proxy/data.jsonrecords?' \
               f'cube=complexity_pci_a_{a}_hs4&' \
               f'Year=2020&' \
               f'HS4={b}&' \
               f'drilldowns=HS4,PCI+Rank,Year&' \
               f'measures=PCI&' \
               f'parents=true&' \
               f'sparse=true'

    return url


def pci_url_hs6(a, b):
    url: str = f'https://oec.world/olap-proxy/data.jsonrecords?' \
               f'cube=complexity_pci_a_{a}_hs6&' \
               f'Year=2020&' \
               f'HS6={b}&' \
               f'drilldowns=HS6,PCI+Rank,Year&' \
               f'measures=PCI&' \
               f'parents=true&' \
               f'sparse=true'

    return url


def tarrifs_url_hs2(a, b):

    url: str = f'https://oec.world/olap-proxy/data?' \
               f'HS2={a}&' \
               f'Reporter+Country={b}&' \
               f'Year=2020&' \
               f'cube=tariffs_i_wits_a_hs_new&' \
               f'drilldowns=Year,HS2,Partner+Country,Reporter+Country,Agreement&' \
               f'measures=Tariff&' \
               f'parents=true&' \
               f'sparse=true&' \
               f'sort=Tariff.desc&' \
               f'locale=en'

    return url


def tarrifs_url_hs4(a, b):
    url: str = f'https://oec.world/olap-proxy/data?' \
               f'HS4={a}&' \
               f'Reporter+Country={b}&' \
               f'Year=2020&' \
               f'cube=tariffs_i_wits_a_hs_new&' \
               f'drilldowns=Year,HS4,Partner+Country,Reporter+Country,Agreement&' \
               f'measures=Tariff&' \
               f'parents=true&' \
               f'sparse=true&' \
               f'sort=Tariff.desc&' \
               f'locale=en'

    return url


def tarrifs_url_hs6(a, b):
    url: str = f'https://oec.world/olap-proxy/data?' \
               f'HS6={a}&' \
               f'Reporter+Country={b}&' \
               f'Year=2020&' \
               f'cube=tariffs_i_wits_a_hs_new&' \
               f'drilldowns=Year,HS4,Partner+Country,Reporter+Country,Agreement&' \
               f'measures=Tariff&' \
               f'parents=true&' \
               f'sparse=true&' \
               f'sort=Tariff.desc&' \
               f'locale=en'

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

    depth2: List[str] = ['hs2', 'hs4', 'hs6']
    rev2: List[str] = [
        'hs92',
        'hs96'
    ]

    hs2: List[str] = [s.removesuffix('\n') for s in open('./hs2.csv').readlines()]
    hs4: List[str] = [s.removesuffix('\n') for s in open('./hs4.csv').readlines()]
    hs6: List[str] = [s.removesuffix('\n') for s in open('./hs6.csv').readlines()]
    countries: List[str] = [s.removesuffix('\n') for s in open('./country-code.csv').readlines()]

    # 1
    for a in triplef(depth, rev, countries, eci_url):
        print(a)

    # ---

    # 2
    for a in doublef(rev, hs4, pci_url_hs4):
        print(a)

    # 3
    for a in doublef(rev, hs6, pci_url_hs6):
        print(a)

    # ---

    for a in doublef(hs2, countries, tarrifs_url_hs2):
        print(a)

    for a in doublef(hs4, countries, tarrifs_url_hs4):
        print(a)

    for a in doublef(hs6, countries, tarrifs_url_hs6):
        print(a)


if __name__ == '__main__':
    main()
