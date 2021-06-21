import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
import pandas as pd
import matplotlib.pyplot as plt


class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Конвертер валют от Бонча')
        self.setWindowIcon(QIcon('logo.png'))
        self.ui.input_currency.setPlaceholderText('Из валюты:')
        self.ui.input_amount.setPlaceholderText('Сколько:')
        self.ui.output_currency.setPlaceholderText('В валюту:')
        self.ui.output_amount.setPlaceholderText('Итог:')
        self.ui.pushButton.clicked.connect(self.converter)

    def converter(self):
        from_currency = self.ui.input_currency.text()
        to_currency = self.ui.output_currency.text()
        # api_key = "XDFOLSF7XY4M0WER"
        # base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
        # main_url = base_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key
        # req_ob = requests.get(main_url)
        # result = req_ob.json()
        # Exchange_Rate = float(result["Realtime Currency Exchange Rate"]
        #                       ['5. Exchange Rate'])

        import requests
        from bs4 import BeautifulSoup

        def parse(chart):
            for tr in chart:
                value = []
                for td in tr.find_all('td'):
                    value.append(td.text)
                return value

        def func_chunk(lst, n):
            for x in range(0, len(lst), n):
                e_c = lst[x: n + x]

                if len(e_c) < n:
                    e_c = e_c + [None for y in range(n - len(e_c))]
                yield e_c

        url = 'https://cbr.ru/currency_base/daily/'
        url_week = 'https://cbr.ru/hd_base/micex_doc/'
        response = requests.get(url)
        response_week = requests.get(url_week)
        soup = BeautifulSoup(response.text, 'lxml')
        soup_week = BeautifulSoup(response_week.text, 'lxml')
        table = soup.find_all('table', class_='data')
        table = parse(table)
        table_week = soup_week.find_all('table', class_='data spaced')
        table_week = parse(table_week)
        table_week_date = table_week[0:len(table_week):9]
        table_week_kurs = table_week[1:len(table_week):9]
        for i in range(len(table_week_kurs)):
            k = table_week_kurs[i]
            k = float(k.replace(',', '.'))
            table_week_kurs[i] = k
        date_time = pd.to_datetime(table_week_date)
        lst = []
        for i in range(len(table_week_kurs)):
            lst.append(table_week_kurs[i])
        fig, ax = plt.subplots()
        ax.plot(date_time, lst, "-o")
        ax.set_title('Изменение курса USD за последнюю неделю')
        fig.autofmt_xdate()
        plt.show()

        conv = {}
        name = []
        table = list(func_chunk(table, 5))
        for x in table:
            if str(x[2]) == '1':
                name.append(x[3])
                x[4] = x[4].replace(',', '.')
                conv[x[1]] = float(x[4])

        amount = float(self.ui.input_amount.text())
        new_amount = round((amount * conv[f'{from_currency}'])/conv[f'{to_currency}'], 4)
        self.ui.output_amount.setText(str(new_amount))


app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()

sys.exit(app.exec())
