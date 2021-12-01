import time
import webbrowser
from win10toast_click import ToastNotifier
from yahoofinanceapi import YahooApi

class compare:
    def __init__(self):
        self.__ya = YahooApi()
        self.__data_set_original = {
            "nikkei": abs(float(self.__getNikkei_request()['quoteSummary']['result'][0]['price']['regularMarketChangePercent']['fmt'].split("%")[0])),
            "dax": abs(float(self.__getDax_request()['quoteSummary']['result'][0]['price']['regularMarketChangePercent']['fmt'].split("%")[0])),
            "nasdaq": abs(float(self.__getNasdaq_request()['quoteSummary']['result'][0]['price']['regularMarketChangePercent']['fmt'].split("%")[0]))
        }
        self.init_check(self.__data_set_original["nikkei"], "Nikkei 225")
        self.init_check(self.__data_set_original["dax"], "Dax Index")
        self.init_check(self.__data_set_original["nasdaq"], "NASDAQ")

        self.__data_set_update = {
            "nikkei": 0,
            "dax": 0,
            "nasdaq": 0
        }

    def __getNikkei_request(self):
        return self.__ya.getquoteSummary("%5EN225").json()

    def __getDax_request(self):
        return self.__ya.getquoteSummary("%5EGDAXI").json()

    def __getNasdaq_request(self):
        return self.__ya.getquoteSummary("%5EIXIC").json()

    def get_data_set_original(self):
        return self.__data_set_original

    def update_data_set_update(self):
        self.__data_set_update = {
            "nikkei": abs(float(self.__getNikkei_request()['quoteSummary']['result'][0]['price']['regularMarketChangePercent']['fmt'].split("%")[0])),
            "dax": abs(float(self.__getDax_request()['quoteSummary']['result'][0]['price']['regularMarketChangePercent']['fmt'].split("%")[0])),
            "nasdaq": abs(float(self.__getNasdaq_request()['quoteSummary']['result'][0]['price']['regularMarketChangePercent']['fmt'].split("%")[0]))
        }

    def get_data_set_update(self):
        return self.__data_set_update

    def init_check(self, x, bolsa):
        if x > .5:
            self.notification("Incremento de precio en "+str(bolsa), "Click para abrir el navegador")
        elif x <.5:
            self.notification("Decremento de precio en " + str(bolsa), "Click para abrir el navegador")
        time.sleep(2)


    def increment(self, x1, x2):
        if x2 - x1 >= .5:
            return True
        return False

    def decrement(self, x1, x2):
        if x1 - x2 <= -.5:
            return True
        return False

    def notification(self, tittle, body):
        toaster = ToastNotifier()
        toaster.show_toast(tittle, body, duration=5, threaded=True, callback_on_click=self.open_url())

    def open_url(self):
        try:
            webbrowser.open("https://smarttrader.io/", new=1, autoraise=True)
            print('Abriendo el navegador')
        except:
            print('Fallo al abrir el navegador')

    # Nikkei
    def compare_nikkei(self):
        if self.increment(self.get_data_set_original()['nikkei'], self.get_data_set_update()['nikkei']):
            self.notification("Incremento de precio en Nikkei", "Click para abrir el navegador")
            self.get_data_set_original()['nikkei'] = self.get_data_set_update()['nikkei']
        else:
            if self.decrement(self.get_data_set_original()['nikkei'], self.get_data_set_update()['nikkei']):
                self.notification("Decremento de precio en Nikkei", "Click para abrir el navegador")
                self.get_data_set_original()['nikkei'] = self.get_data_set_update()['nikkei']
        time.sleep(2)
        print("Nikkei finalizo")

    # Dax
    def compare_dax(self):
        if self.increment(self.get_data_set_original()['dax'], self.get_data_set_update()['dax']):
            self.notification("Incremento de precio en DAX Index", "Click para abrir el navegador")
            self.get_data_set_original()['dax'] = self.get_data_set_update()['dax']
        else:
            if self.decrement(self.get_data_set_original()['dax'], self.get_data_set_update()['dax']):
                self.notification("Decremento de precio en DAX Index", "Click para abrir el navegador")
                self.get_data_set_original()['dax'] = self.get_data_set_update()['dax']
        time.sleep(1)
        print("Dax finalizo")

    # Nasdaq
    def compare_nasdaq(self):
        if self.increment(self.get_data_set_original()['nasdaq'], self.get_data_set_update()['nasdaq']):
            self.notification("Incremento de precio en NASDAQ", "Click para abrir el navegador")
            self.get_data_set_original()['nasdaq'] = self.get_data_set_update()['nasdaq']
        else:
            if self.decrement(self.get_data_set_original()['nasdaq'], self.get_data_set_update()['nasdaq']):
                self.notification("Decremento de precio en NASDAQ", "Click para abrir el navegador")
                self.get_data_set_original()['nasdaq'] = self.get_data_set_update()['nasdaq']
        time.sleep(3)
        print("Nasdaq finalizo")
