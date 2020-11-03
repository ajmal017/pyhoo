from dataclasses import asdict, dataclass, field
from typing import Iterable, List, Sequence

from pynance.models.abc import BaseModel
from pynance.models.iterables import Strikes, Timestamp
from pynance.types.options import OptionDict, OptionQuoteDict, OptionsDataRecord


@dataclass
class Option:

    contractSymbol: str
    strike: float
    currency: str
    lastPrice: float
    change: float
    percentChange: float
    ask: float
    contractSize: str
    expiration: int
    lastTradeDate: int
    impliedVolatility: float
    inTheMoney: bool
    volume: int = field(default=0)
    bid: float = field(default=0.0)
    openInterest: int = field(default=0)


@dataclass
class OptionQuote:
    language: str
    region: str
    quoteType: str
    quoteSourceName: str
    triggerable: bool
    currency: str
    sharesOutstanding: int
    bookValue: float
    fiftyDayAverage: float
    fiftyDayAverageChange: float
    fiftyDayAverageChangePercent: float
    twoHundredDayAverage: float
    twoHundredDayAverageChange: float
    twoHundredDayAverageChangePercent: float
    marketCap: int
    forwardPE: float
    priceToBook: float
    sourceInterval: int
    exchangeDataDelayedBy: int
    tradeable: bool
    ask: float
    bidSize: int
    askSize: int
    fullExchangeName: str
    financialCurrency: str
    regularMarketOpen: float
    averageDailyVolume3Month: int
    averageDailyVolume10Day: int
    fiftyTwoWeekLowChange: float
    fiftyTwoWeekLowChangePercent: float
    fiftyTwoWeekRange: str
    fiftyTwoWeekHighChange: float
    fiftyTwoWeekHighChangePercent: float
    fiftyTwoWeekLow: float
    fiftyTwoWeekHigh: float
    dividendDate: int
    earningsTimestamp: int
    earningsTimestampStart: int
    earningsTimestampEnd: int
    trailingAnnualDividendRate: float
    trailingPE: float
    trailingAnnualDividendYield: float
    epsTrailingTwelveMonths: float
    epsForward: float
    epsCurrentYear: float
    priceEpsCurrentYear: float
    exchange: str
    shortName: str
    longName: str
    messageBoardId: str
    exchangeTimezoneName: str
    exchangeTimezoneShortName: str
    gmtOffSetMilliseconds: int
    market: str
    esgPopulated: bool
    marketState: str
    firstTradeDateMilliseconds: int
    priceHint: int
    regularMarketChange: float
    regularMarketChangePercent: float
    regularMarketTime: float
    regularMarketPrice: float
    regularMarketDayHigh: float
    regularMarketDayRange: str
    regularMarketDayLow: float
    regularMarketVolume: int
    regularMarketPreviousClose: float
    bid: float
    displayName: str
    symbol: str
    preMarketChange: float = field(default=0.0)
    preMarketChangePercent: float = field(default=0.0)
    preMarketTime: float = field(default=0.0)
    preMarketPrice: float = field(default=0.0)


class Options(BaseModel):

    expirationDate: int
    hasMiniOptions: bool
    calls: Iterable[Option]
    puts: Iterable[Option]

    def __init__(
        self, expirationDate: int, hasMiniOptions: bool, calls: Iterable[OptionDict], puts: Iterable[OptionDict]
    ) -> None:
        self.expirationDate = expirationDate
        self.hasMiniOptions = hasMiniOptions
        self.calls = [Option(**call) for call in calls]
        self.puts = [Option(**put) for put in puts]


class OptionsData(BaseModel):

    underlyingSymbol: str
    expirationDates: Timestamp
    strikes: Strikes
    hasMiniOptions: bool
    quote: OptionQuote
    options: Options

    def __init__(
        self,
        underlyingSymbol: str,
        expirationDates: Iterable[int],
        strikes: Iterable[float],
        hasMiniOptions: bool,
        quote: OptionQuoteDict,
        options: Sequence[OptionDict],
    ) -> None:
        self.underlyingSymbol = underlyingSymbol
        self.expirationDates = Timestamp(expirationDates)
        self.strikes = Strikes(strikes)
        self.hasMiniOptions = hasMiniOptions
        self.quote = OptionQuote(**quote)
        self.options = Options(**options[0])

    def to_records(self) -> List[OptionsDataRecord]:
        return [
            {
                "underlyingSymbol": self.underlyingSymbol,
                "type": type,
                **asdict(option),
            }
            for option, type in [(call, "CALL") for call in self.options.calls]
            + [(put, "PUT") for put in self.options.puts]
        ]
