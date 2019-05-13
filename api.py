"""
    Pivot Security Python API is free software: you can redistribute it and/or modify
    it under the terms of the MIT licence.

    Pivot Security Python API is distributed in the hope that it will be useful, under MIT licence 
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    Please read licence file for more information.
"""

from requests.auth import HTTPBasicAuth
import requests,json

class Api():
 
    base_url = 'https://api.pivotsecurity.com/api'
    public_key = None
    private_key = None
    endpoints = { "OP_CREATE":"account/create", "OP_INFO":"account/info", "OP_RISK_SCORE":"account/riskscore", "OP_UPDATE_RISK_SCORE":"account/updateriskscore", "OP_QRCODE":"account/qrcode", "OP_AUTH_CODE":"account/authcode", "OP_LOGS":"account/logs", "OP_LOCK":"account/lock","OP_UNLOCK":"account/unlock","OP_TRAIN_ML":"account/trainml","OP_TEST_ML":"account/testml","OP_AUTH_META":"account/authwithmetadata","OP_AUTH_SEND_META":"account/sendauthwithmetadata","OP_VERIFY_META":"account/verifywithmetadata","OP_VERIFY_SESSION":"account/verifysession""OP_AUTH":"customer/auth","OP_VALIDATE":"customer/verify","OP_CUST_CREATE":"customer/create"}

    def __init__(self, public_key='', private_key=''):
        self.private_key = private_key
        self.public_key = public_key

    def post(self, endpoint, data, public=False, private=True):
        try:
            url = '%s/%s' % (self.base_url, self.endpoints[endpoint])
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain' }
            if private:
                auth=HTTPBasicAuth(self.private_key, '')
            else:
                auth=HTTPBasicAuth(self.public_key,'')
            r = requests.post(url, data=data, auth=auth , headers=headers)

            return r.text
        except Error:
            return "You must pass valid values as the arguments to Pivot Security API "
            + "method calls.  (HINT: an example call to get customer info call"
            + "would be: Api.info('uid')";
    def info(self, uid, email):
        return self.post("OP_INFO", '{"uid":"' + uid + '","email":"' + email + '"}');

    def create(self, uid, email, channel):
        return self.post("OP_INFO", '{"uid":"' + uid + '","email":"' + email + '"},"channel":"'+channel+'"}');

    def riskscore(self, uid, email):
        return self.post("OP_RISK_SCORE", '{"uid":"' + uid + '","email":"' + email + '"}');
        
    def update_riskscore(self, uid, email, risk_score):
         return self.post("OP_RISK_SCORE", '{"uid":"' + uid + '","email":"' + email + '"}","riskscore":"'+risk_score+'"}');

    def qrcode(self, uid, email):
        return self.post("OP_QRCODE", '{"uid":"' + uid + '","email":"' + email + '"}');

    def authcode(self, uid, email):
        return self.post("OP_AUTH_CODE", '{"uid":"' + uid + '","email":' + email + '"}');

    def logs(self, uid, email):
        return self.post("OP_LOGS", '{"uid":"' + uid + '","email":"' + email + '"}');

    def lock(self, uid, email):
        return self.post("OP_LOCK", '{"uid":"' + uid + '","email":"' + email + '"}');

    def unlock(self, uid, email):
        return self.post("OP_UNLOCK", '{"uid":"' + uid + '","email":"' + email + '"}');

    def trainml(self, uid, email, data):
        return self.post("OP_TRAIN_ML", '{"uid":"' + uid + '","email":"' + email + '","data":"'+data+'"}');

    def testml(self, uid, email, data):
        return self.post("OP_TEST_ML", '{"uid":"' + uid + '","email":"' + email + '","data":"'+data+'"}');
    
    def auth_with_metadata(self, uid, email, metadata):
        return self.post("OP_AUTH_META", '{"uid":"' + uid + '","email":"' + email + '","metadata":"'+metadata+'"}');

    def send_auth_with_metadata(self, uid, email, metadata):
        return self.post("OP_AUTH_SEND_META", '{"uid":"' + uid + '","email":"' + email + '","code":"'+metadata+'"}');

    def validate_auth_with_metadata(self, uid, email, code):
        return self.post("OP_VALIDATE", '{"uid":"' + uid + '","email":"' + email + '","code":"'+code+'"}');
    
    def validate_auth_with_metadata(self, uid, email, sessionid):
        return self.post("OP_VERIFY_SESSION", '{"uid":"' + uid + '","email":"' + email + '","sessionid":"'+sessionid+'"}');
	
    def auth(self, uid, email):
        return self.post("OP_AUTH", '{"uid":"' + uid + '","email":"' + email + '"}',True, False);
    
    def validate_auth(self, uid, email, code):
        return self.post("OP_VALIDATE", '{"uid":"' + uid + '","email":"' + email + '","code":"'+code+'"}', True, False);
        
    def customer_create(self, uid, email, channel):
        return self.post("OP_CUST_CREATE", '{"uid":"' + uid + '","email":"' + email + '","channel":"'+channel+'"}', True, False);

        
