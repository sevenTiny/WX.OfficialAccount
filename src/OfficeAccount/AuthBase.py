import requests
import json
import datetime
import time

# ------ 手动配置 -----
# 微信公众号 appid
_appid = 'wxa584ee2936d52516'
# 微信公众号 appsecret
_appSecret = ''

# ------ 内部变量 ------
# 全局过期时间
_accessTokenExpiredTime = 1
# 全局token
_accessToken = '41_KjCz9-kseQZUdbL3ESe5FNIzE65LJ8WOPjWovma1zSm_VQsw8ZEQ7WdzFyUj2lu3DG6bjInraEQKac9wzB4liKPR3H0wx1MLohvbe7WmkCbxHJRnvFA1USV4CVKMgeLGPwmlRfMzcVdQxml_FQSgAGAWHJ'


class AuthBase():
    def __init__(self):
        None

    def __SetAccessTokenExpiredTime(self, token):
        global _accessTokenExpiredTime, _accessToken
        _accessToken = token
        _accessTokenExpiredTime = (
            datetime.datetime.now() + datetime.timedelta(hours=1)).timestamp()

    def __checkAccessTokenHasBeenExpired(self):
        # 调试时候用，如果有手动添加的Token，则直接用即可
        if _accessToken.strip() != '':
            return False

        global _accessTokenExpiredTime
        if _accessTokenExpiredTime == 1 or _accessTokenExpiredTime < time.time():
            return True
        else:
            return False

    def getAccessToken(self):
        if self.__checkAccessTokenHasBeenExpired() == False:
            return _accessToken

        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' + \
            _appid + '&secret=' + _appSecret
        response = requests.get(url).json()
        accessToken = response['access_token']
        if accessToken is not None:
            self.__SetAccessTokenExpiredTime(accessToken)
            print('_accessToken='+_accessToken)
            return _accessToken
        else:
            raise Exception('获取token失败：' + json.dumps(response))
