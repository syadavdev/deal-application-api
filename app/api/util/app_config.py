from flask import current_app

class AppConfig:
    def __init__(self):
        self.apiKey = current_app.config['API_KEY']
        self.apiSecret = current_app.config['API_SECRET']
        self.apiPort = current_app.config['API_PORT']
        self.serverName = current_app.config['ROOT']
        self.timeFormat = current_app.config['DATETIME_FORMAT']
        self.appUri = current_app.config['APP_URI']
        self.secret = current_app.config['SECRET_KEY']
        self.t_exp = current_app.config.get('TOKEN_EXP', 12)
        self.birt_uri = current_app.config.get('BIRT_URI')
        self.birt_server = current_app.config.get('BIRT_SERVER')
        self.is_secure_active = current_app.config.get('SECURE')
        self.es_index = current_app.config.get('ES_INDEX')
        self.es_txt_index = current_app.config.get('ES_TXT_INDEX')

    def getAPIKey(self):
        return self.apiKey

    def getAPISecret(self):
        return self.apiSecret

    def getAPIPort(self):
        return self.apiPort

    def getServerName(self):
        return self.serverName

    def getAPITimeFormat(self):
        return self.timeFormat

    def getAPIUri(self):
        return self.appUri

    def getSecret(self):
        return self.secret

    def getTokenExp(self):
        return self.t_exp

    def getBirtUri(self):
        return self.birt_uri

    def getBirtServer(self):
        return self.birt_server

    def is_secure_server_access(self):
        return self.is_secure_active

    def elastic_index(self):
        return self.es_index;
    def elastic_txt_index(self):
        return self.es_txt_index