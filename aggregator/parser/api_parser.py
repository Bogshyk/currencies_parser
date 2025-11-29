class APIParser:

    @staticmethod
    def parse(response_json):
        rates = response_json.get("rates", {})
        return {currency: float(rate) for currency, rate in rates.items()}
