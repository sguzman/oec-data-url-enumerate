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


def singlef(alist, func):
    for a in alist:
        yield func(a)


def eci_url(a, b):
    url: str = f'https://oec.world/olap-proxy/data.jsonrecords?' \
               f'cube=complexity_eci_a_{b}_{a}&' \
               f'drilldowns=Country,Year,ECI+Rank&' \
               f'measures=ECI&' \
               f'parents=true&' \
               f'sparse=true'

    return url


def pci_url_hs4(a, b):
    url: str = f'https://oec.world/olap-proxy/data.jsonrecords?' \
               f'cube=complexity_pci_a_{a}_hs4&' \
               f'HS4={b}&' \
               f'drilldowns=HS4,PCI+Rank,Year&' \
               f'measures=PCI&' \
               f'parents=true&' \
               f'sparse=true'

    return url


def pci_url_hs6(a, b):
    url: str = f'https://oec.world/olap-proxy/data.jsonrecords?' \
               f'cube=complexity_pci_a_{a}_hs6&' \
               f'HS6={b}&' \
               f'drilldowns=HS6,PCI+Rank,Year&' \
               f'measures=PCI&' \
               f'parents=true&' \
               f'sparse=true'

    return url


def tarrifs_url_hs2(a):
    url: str = f'https://oec.world/olap-proxy/data?' \
               f'HS2={a}&' \
               f'cube=tariffs_i_wits_a_hs_new&' \
               f'drilldowns=Year,HS2,Partner+Country,Reporter+Country,Agreement&' \
               f'measures=Tariff&' \
               f'parents=true&' \
               f'sparse=true&' \
               f'sort=Tariff.desc&' \
               f'locale=en'

    return url


def tarrifs_url_hs4(a):
    url: str = f'https://oec.world/olap-proxy/data?' \
               f'HS4={a}&' \
               f'cube=tariffs_i_wits_a_hs_new&' \
               f'drilldowns=Year,HS4,Partner+Country,Reporter+Country,Agreement&' \
               f'measures=Tariff&' \
               f'parents=true&' \
               f'sparse=true&' \
               f'sort=Tariff.desc&' \
               f'locale=en'

    return url


def tarrifs_url_hs6(a):
    url: str = f'https://oec.world/olap-proxy/data?' \
               f'HS6={a}&' \
               f'cube=tariffs_i_wits_a_hs_new&' \
               f'drilldowns=Year,HS4,Partner+Country,Reporter+Country,Agreement&' \
               f'measures=Tariff&' \
               f'parents=true&' \
               f'sparse=true&' \
               f'sort=Tariff.desc&' \
               f'locale=en'

    return url


def import_hs2(a, b):
    url: str = f'https://oec.world/olap-proxy/data?' \
               f'cube=trade_i_baci_a_{a}&' \
               f'drilldowns=Year,HS2,Exporter+Country,Importer+Country&' \
               f'measures=Quantity,Trade+Value&' \
               f'parents=true&' \
               f'sparse=true&' \
               f'locale=en&' \
               f'HS2={b}'

    return url


def import_hs4(a, b):
    url: str = f'https://oec.world/olap-proxy/data?' \
               f'cube=trade_i_baci_a_{a}&' \
               f'drilldowns=Year,HS4,Exporter+Country,Importer+Country&' \
               f'measures=Quantity,Trade+Value&' \
               f'parents=true&' \
               f'sparse=true&' \
               f'locale=en&' \
               f'HS4={b}'

    return url


def import_hs6(a, b):
    url: str = f'https://oec.world/olap-proxy/data?' \
               f'cube=trade_i_baci_a_{a}&' \
               f'drilldowns=Year,HS6,Exporter+Country,Importer+Country&' \
               f'measures=Quantity,Trade+Value&' \
               f'parents=true&' \
               f'sparse=true&' \
               f'locale=en&' \
               f'HS6={b}'

    return url


def monthly_1_hs2(a):
    url: str = f'https://oec.world/olap-proxy/data?' \
               f'cube=trade_i_comtrade_m_hs&' \
               f'Trade+Flow=1&' \
               f'drilldowns=Time,Trade+Flow,Reporter+Country,Partner+Country,HS2&' \
               f'measures=Trade+Value,Net+Weight&' \
               f'locale=en&' \
               f'HS2={a}'

    return url


def monthly_1_hs4(a):
    url: str = f'https://oec.world/olap-proxy/data?' \
               f'cube=trade_i_comtrade_m_hs&' \
               f'Trade+Flow=1&' \
               f'drilldowns=Time,Trade+Flow,Reporter+Country,Partner+Country,HS4&' \
               f'measures=Trade+Value,Net+Weight&' \
               f'locale=en&' \
               f'HS4={a}'

    return url

def monthly_1_hs6(a):
    url: str = f'https://oec.world/olap-proxy/data?' \
               f'cube=trade_i_comtrade_m_hs&' \
               f'Trade+Flow=1&' \
               f'drilldowns=Time,Trade+Flow,Reporter+Country,Partner+Country,HS6&' \
               f'measures=Trade+Value,Net+Weight&' \
               f'locale=en&' \
               f'HS6={a}'

    return url


def monthly_2_hs2(a):
    url: str = f'https://oec.world/olap-proxy/data?' \
               f'cube=trade_i_comtrade_m_hs&' \
               f'Trade+Flow=2&' \
               f'drilldowns=Time,Trade+Flow,Reporter+Country,Partner+Country,HS2&' \
               f'measures=Trade+Value,Net+Weight&' \
               f'locale=en&' \
               f'HS2={a}'

    return url


def monthly_2_hs4(a):
    url: str = f'https://oec.world/olap-proxy/data?' \
               f'cube=trade_i_comtrade_m_hs&' \
               f'Trade+Flow=2&' \
               f'drilldowns=Time,Trade+Flow,Reporter+Country,Partner+Country,HS4&' \
               f'measures=Trade+Value,Net+Weight&' \
               f'locale=en&' \
               f'HS4={a}'

    return url


def monthly_2_hs6(a):
    url: str = f'https://oec.world/olap-proxy/data?' \
               f'cube=trade_i_comtrade_m_hs&' \
               f'Trade+Flow=2&' \
               f'drilldowns=Time,Trade+Flow,Reporter+Country,Partner+Country,HS6&' \
               f'measures=Trade+Value,Net+Weight&' \
               f'locale=en&' \
               f'HS6={a}'

    return url


def services(a):
    url: str = f'https://oec.world/olap-proxy/data?' \
               f'cube=services_i_comtrade_a_eb02&' \
               f'Reporter+Country={a}&' \
               f'drilldowns=Year,Trade+Flow,Reporter+Country,Service,Partner+Country&' \
               f'measures=Service+Value&' \
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
    for a in doublef(depth, rev, eci_url):
        print(a)

    # ---

    # 2
    for a in doublef(rev, hs4, pci_url_hs4):
        print(a)

    # 3
    for a in doublef(rev, hs6, pci_url_hs6):
        print(a)

    # ---

    for a in singlef(hs2, tarrifs_url_hs2):
        print(a)

    for a in singlef(hs4, tarrifs_url_hs4):
        print(a)

    for a in singlef(hs6, tarrifs_url_hs6):
        print(a)


    # ---

    for a in doublef(rev, hs2, import_hs2):
        print(a)

    for a in doublef(rev, hs4, import_hs4):
        print(a)

    for a in doublef(rev, hs6, import_hs6):
        print(a)

    # ---

    for a in singlef(hs2, monthly_1_hs2):
        print(a)

    for a in singlef(hs4, monthly_1_hs4):
        print(a)

    for a in singlef(hs6, monthly_1_hs6):
        print(a)

    # ---

    for a in singlef(hs2, monthly_2_hs2):
        print(a)

    for a in singlef(hs4, monthly_2_hs4):
        print(a)

    for a in singlef(hs6, monthly_2_hs6):
        print(a)

    # ---

    for a in singlef(countries, services):
        print(a)


if __name__ == '__main__':
    main()
