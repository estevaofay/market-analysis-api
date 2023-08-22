import csv
import xml.etree.ElementTree as ET
from contextlib import asynccontextmanager
from pathlib import Path

from models.currency import Currency
from models.exchange import Exchange, LegalEntity, MarketCategory


@asynccontextmanager
async def lifespan(app):
    exchanges_database = load_exchanges_from_csv()
    app.state.exchanges_database = exchanges_database
    exchanges_list = list(exchanges_database.values())
    app.state.exchanges_list = exchanges_list
    currencies = load_currencies_from_xml()
    currency_list = list(currencies.values())
    app.state.currencies = currencies
    app.state.currency_list = currency_list
    yield
    exchanges_database.clear()
    currencies.clear()


# noinspection PyTypeChecker
def load_exchanges_from_csv():
    with open(
        f"{Path(__file__).resolve().parent.parent.parent}/data/ISO10383_MIC.csv", encoding="cp1252"
    ) as stock_exchange_csv_file:
        reader = csv.DictReader(stock_exchange_csv_file)
        exchanges = {}
        for exchange in reader:
            exchanges[exchange["MIC"]] = Exchange(
                market_name=exchange["MARKET NAME-INSTITUTION DESCRIPTION"],
                market_identifier_code=exchange["MIC"],
                operating_market_identifier_code=exchange["OPERATING MIC"],
                operating_or_segment=exchange["MIC"],
                operating=exchange["MIC"].upper() == "OPRT",
                segment=exchange["MIC"].upper() == "SGMT",
                legal_entity=LegalEntity(name=exchange["LEGAL ENTITY NAME"], identifier=exchange["LEI"]),
                market_category=MarketCategory(code=exchange["MARKET CATEGORY CODE"], description="Not Specified"),
                acronym=exchange["ACRONYM"],
                country=exchange["ISO COUNTRY CODE (ISO 3166)"],
                city=exchange["CITY"],
                status=exchange["STATUS"],
                active=exchange["STATUS"].upper() == "ACTIVE",
                creation_date=exchange["CREATION DATE"],
                last_update_date=exchange["LAST UPDATE DATE"],
                last_validation_date=exchange["LAST VALIDATION DATE"],
                expiry_date=exchange["EXPIRY DATE"],
                comments=exchange["COMMENTS"],
                website=exchange["WEBSITE"],
            )
        return exchanges


def load_currencies_from_xml():
    currencies_from_xml = ET.parse(f"{Path(__file__).resolve().parent.parent.parent}/data/currencies.xml")
    root = currencies_from_xml.getroot()
    currencies = {}
    for currency in root.findall("moeda"):
        currencies[currency.findtext("codigo")] = Currency(
            code=currency.findtext("codigo"),
            iata_code=currency.findtext("codigoIata"),
            country_code=currency.findtext("codigoPais"),
            swift_code=currency.findtext("codigoSwift"),
            inclusion_date=currency.findtext("dataHoraInclusao"),
            registration_date=currency.findtext("dataHoraRegistro"),
            gender=currency.findtext("genero"),
            name=currency.findtext("nome"),
            formatted_name=currency.findtext("nomeFormatado"),
            name_in_singular=currency.findtext("nomeSingular"),
            name_in_plural=currency.findtext("nomePlural"),
            acronym=currency.findtext("sigla"),
            type=currency.findtext("tipo"),
            symbol=currency.findtext("simbolo"),
        )
    return currencies
