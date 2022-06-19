#!/usr/bin/env python
from pprint import pprint
import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


def main():
    CREDENTIALS_FILE = 'credentials.json'  # имя файла с закрытым ключом
    spreadsheet_id = '1iiZtElyHPvPVsEzPeqMjcxvZpXFDK5S11DeSM2xFQgw'  # file google docs
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                                   ['https://www.googleapis.com/auth/spreadsheets',
                                                                    'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)

    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A1:E10',
        majorDimension='ROWS'

    ).execute()
    pprint(values)
    exit()



if __name__ == '__main__':
    main()
