
import requests

import json


class Kingdee(object):

    def __init__(self):
        self.domain = "https://jisulife.ik3cloud.com/k3cloud/"
        pass

    def get_cookies(self, user_id, user_name, password):
        login_url = self.domain + "Kingdee.BOS.WebApi.ServicesStub.AuthService.ValidateUser.common.kdsvc"
        login_data = {"acctid": user_id, "username": user_name, "password": password, "lcid": 2052}
        response = requests.post(url=login_url, data=login_data)
        cookies = response.cookies
        return cookies

    def make_request(self, url, data, cookies):

        res = requests.post(url=url, data=data, cookies=cookies).text

        response = json.loads(str(res))

        return response

    def view(self, data, cookies):

        view_url = self.domain + "Kingdee.BOS.WebApi.ServicesStub.DynamicFormService.View.common.kdsvc"

        return self.make_request(view_url, data=data, cookies=cookies)

    def save(self, data, cookies):

        save_url = self.domain + "Kingdee.BOS.WebApi.ServicesStub.DynamicFormService.Save.common.kdsvc"

        return self.make_request(save_url, data=data, cookies=cookies)

    def submit(self, data, cookies):

        submit_url = self.domain + "Kingdee.BOS.WebApi.ServicesStub.DynamicFormService.Submit.common.kdsvc"

        return self.make_request(submit_url, data=data, cookies=cookies)

    def audit(self, data, cookies):
        audit_url = self.domain + "Kingdee.BOS.WebApi.ServicesStub.DynamicFormService.Audit.common.kdsvc"

        return self.make_request(audit_url, data=data, cookies=cookies)

    def push(self, data, cookies):
        push_url = self.domain + "Kingdee.BOS.WebApi.ServicesStub.DynamicFormService.Push.common.kdsvc"

        return self.make_request(push_url, data=data, cookies=cookies)

    def anti_audit(self, data, cookies):
        anti_audit_url = self.domain + "Kingdee.BOS.WebApi.ServicesStub.DynamicFormService.UnAudit.common.kdsvc"

        return self.make_request(anti_audit_url, data=data, cookies=cookies)

    def query(self, data, cookies):

        query_url = self.domain + "Kingdee.BOS.WebApi.ServicesStub.DynamicFormService.ExecuteBillQuery.common.kdsvc"

        return self.make_request(query_url, data=data, cookies=cookies)
