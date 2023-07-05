import logging
import os

import pandas as pd
from src.utils import config
from src.utils.connect import DatabaseModelsClass
from dotenv import find_dotenv, load_dotenv
import requests


class GetDataTemplate:
    """ Class to etl data. """
    logger = logging.getLogger(f"{__name__}.GetDataTemplate")
    database_instance = DatabaseModelsClass('MYSQLLINUX')

    load_dotenv(find_dotenv())
    APIKEY = os.environ.get('KEYNAME')
    DATA_FOLDER = os.path.join(config.ROOTDIR, 'data')

    def get_excel_DATA(self):
        self.logger.debug(f"- get_excel_DATA")

        path = os.path.join(self.DATA_FOLDER, 'raw', 'SHEETNAME')
        df = pd.read_excel(path, 'TABNAME', engine='openpyxl')

        return df

    def get_sql_DATA(self):
        self.logger.debug(f"- get_sql_DATA")

        query_str = f""" 
            SELECT * FROM DATABASE.TABLE;
        """
        df = self.database_instance.select_query(query_str=query_str)

        return df

    def get_api_DATA(self, dataframe):
        self.logger.debug(f"- get_api_DATA")

        url = f""" URL FOR API"""
        response = requests.get(url)

        if response.ok:
            response = response.json()

            if dataframe:
                response = pd.DataFrame(response)

        else:
            self.logger.info(f"- get_api_DATA response not OK")
            exit()

        return response
