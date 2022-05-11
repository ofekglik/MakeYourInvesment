class ProvidentFund:

    def __init__(self, title, name, url):
        self.title = title
        self.name = name
        self.url = url
        self.current_month_yield = None
        self.current_year_yield = None
        self.annual_yield = None
        self.biannual_yield = None
        self.triennial_yield = None

    def get_title(self):
        return self.title

    def get_name(self):
        return self.name

    def get_url(self):
        return self.url

    def set_current_month_yield(self, current_month_yield):
        self.current_month_yield = current_month_yield

    def set_current_year_yield(self, current_year_yield):
        self.current_year_yield = current_year_yield

    def set_annual_yield(self, annual_yield):
        self.annual_yield = annual_yield

    def set_biannual_yield(self, biannual_yield):
        self.biannual_yield = biannual_yield

    def set_triennial_yield(self, triennial_yield):
        self.triennial_yield = triennial_yield

