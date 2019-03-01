import requests
import unittest
import xmlrunner
from datetime import datetime, timedelta
import json
import re
from pprint import pprint
import time
import sys
import os

#
# _pth = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(_pth[0:_pth.find("ZuoraScripts")] + "Library")
# import EnvDict
# import qa_utils as utils


class Stonez(unittest.TestCase):
    TIMEOUT = 450
    skip = True
    
    # CREATED_KEYS = []
    KEYSTONE_REGEX = '[A-z0-9]{5}-[A-z0-9]{5}-[A-z0-9]{5}-[A-z0-9]{5}'
    MBAM_REGEX = '[A-z0-9]{5}-[A-z0-9]{5}:[A-z0-9]{4}-[A-z0-9]{4}-[A-z0-9]{4}-[A-z0-9]{4}'
    MBAE_REGEX = '[A-z0-9]{4}-[A-z0-9]{4}:[A-z0-9]{4}-[A-z0-9]{4}-[A-z0-9]{4}-[A-z0-9]{4}'

    # Staing and Dev
    GET_SUB_URL = 'https://apisandbox-api.zuora.com/rest/v1/subscriptions/%s'
    CREATE_SUB_URL = 'https://apisandbox-api.zuora.com/rest/v1/subscriptions'
    CREATE_ACC_URL = 'https://apisandbox-api.zuora.com/rest/v1/accounts'
    GET_CATALOG_URL = 'https://apisandbox-api.zuora.com/rest/v1/catalog/products'
    UPDATE_SUB_URL = 'https://apisandbox-api.zuora.com/rest/v1/subscriptions/'
    GET_ACC_URL = 'https://apisandbox-api.zuora.com/rest/v1/subscriptions/accounts/%s'
    
    REGEX = '[A-Z]{4}-[A-Z]{1}\([A-Z0-9]{5}-[A-Z0-9]{5}-[A-Z0-9]{5}-[A-Z0-9]{5}\)|[A-Z]{4}-[A-Z]{1}\([A-Z0-9]{4,5}-[A-Z0-9]{4,5}:[A-Z0-9]{4,5}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}\)|[A-Z]{4}-[A-Z]{1}\(NO-KEY\)|[A-Z]{4}-[A-Z]{1}\(!\)'
    
    # Dev
    CONNECTION_INPUT = {
        'Content-Type': 'application/json',
        'Accept-Encoding': 'application/json',
        'Authorization': 'Basic \
            aHlkcmFfcGFydGlhbHNiQG1hbHdhcmVie\
            XRlcy5vcmc6dDF5V1UyZFZRRE9ENTRm',
        'apiAccessKeyId': 'hydra_partialsb@malwarebytes.org',
        'apiSecretAccessKey':'t1yWU2dVQDOD54f',
    }

    PRPID = {}
    
    CREATE_SUB_INPUT = {
        # Empty fields accountKey, contractEffectiveDate, initialTerm,
        # renewalTerm, and productRatePlanId must be filled in later
        'accountKey': '', 
        'contractEffectiveDate': '',
        'termType': 'TERMED',
        'initialTerm': '',
        'initialTermPeriodType': 'Month',
        'autoRenew': 'true',
        'renewalTerm': '',
        'renewalTermPeriodType': 'Month',
        'notes': 'StyxTest',
        'subscribeToRatePlans': [{
            'productRatePlanId': '',
        }],
        'invoiceTargetDate': '',
        'invoiceCollect': 'false'
    }
    
    CREATE_ACC_INPUT = {
        'name': '',
        'currency': 'USD',
        'billToContact': {
            'firstName': 'Styx',
            'lastName': 'Stones',
            'address1': '3979 Freedom Circle',
            'address2': '12th Floor',
            'state': 'CA',
            'country': 'US',
            'zipCode': '95054',
            },
        'creditCard': {
            'cardType': 'Visa',
            'cardNumber': '4112344112344113',
            'expirationMonth': '12',
            'expirationYear': '2020',
            'securityCode': '123',
            'cardHolderInfo': {
                'cardHolderName': 'Styx and Stones',
                'addressLine1': '3979 Freedom Circle',
                'addressLine2': '12th Floor',
                'city': 'Santa Clara',
                'state': 'CA',
                'country': 'US',
                'zipCode': '95054',
                }
        },
        'billCycleDay': '1',
    }
    
    UPDATE_SUB_INPUT = {
        'update': [{
            'ratePlanId': '',
            'contractEffectiveDate': '2016-07-08',
            'chargeUpdateDetails': [{
                'ratePlanChargeId': "2c92c8f83dcbd8b1013dcce0eb510075",
                'quantity': '100',
                }]
            }],
        'invoiceCollect': False,
        'preview': False,
    }
    
    # ENVIRONMENT =   sys.argv[1]# 'staging' / 'dev'
    # Keystone API calls
    ENVIRONMENT = 'dev'
    if ENVIRONMENT == 'staging':
        TOKEN =         'aKV2QeBV5QNvS-tLMrV_'
        KEYSTONE_BASE = 'https://keystone-staging.mwbsys.com'
    elif ENVIRONMENT == 'dev':
        TOKEN =         'dev2abc'
        KEYSTONE_BASE = 'https://keystone-dev.mwbsys.com:443'
    AUTH_KEY =      {'Authorization':'Token token="%s"' % TOKEN}
    URL =           "%s/api/v1" % KEYSTONE_BASE
    INSTALLATIONS = "%s/installations" % URL        
    TRIALS =        "%s/trials" % URL
    KEYS =          "%s/keys/" % URL
    KEYGEN =        "%s/keygen" % URL
    KEYSEARCH =     "%s/keygen/support_search" % URL
    BASE_DICTIONARY = {'content-type': 'application/json'}
        
    BASE_DICTIONARY.update(AUTH_KEY)
    INPUT_TYPE =    BASE_DICTIONARY
    
    def _add_today(self, days=0):
        '''Returns today's date plus @param days'''
        t = datetime.utcnow() + timedelta(hours=-8)
        t = datetime.utcnow() + timedelta(days=days)
        return u'{:>4}-{:>02}-{:>02}'.format(t.year, t.month, t.day)
    
    def _breakpoint(self,msg=""):
        '''Stops execution of code bringing up python console and prints msg'''
        import code, sys
        
        # Use exception trick to pick up the current frame
        try:
            raise None
        except:
            frame = sys.exc_info()[2].tb_frame.f_back
        
        # Evaluate commands in current namespace
        namespace = frame.f_globals.copy()
        namespace.update(frame.f_locals)
        code.interact(banner="-%s>>" % msg, local=namespace)
        
    def _delete_key(self,licenseKey):
        '''Deletes a license key. If there is an error, it will be printed and 
            script is halted.'''
        _url = "%s%s" % (self.KEYS,licenseKey)
        try:
            r = requests.delete(_url,data=None,headers=self.INPUT_TYPE,
                timeout=self.TIMEOUT)
            if r.ok:
                print 'Successfully deleted key...%s' % licenseKey
            else:
                print r.text
                print 'Failed to delete key... %s' % licenseKey
        except requests.exceptions.RequestException as e:
            print e
            sys.exit(1)
            
    def compareKeystoneZuora(self, subName, productsEntitled):
        print 'Comparing keystone to zuora...'
        keystone = self.searchKeystoneForEntitlements(subName, type='transaction_id')
        zuora = self.searchZuoraForEntitlements(subName)
        
        if keystone == productsEntitled  == zuora:
            print 'Subscriptions match expected values'
        else:
            print '=' * 70
            # If subs dont match print values grabbed from Keystone/Zuora/Expected
            print 'Subscriptions do not match'
            print 'Entitled in Keystone: '
            pprint (keystone)
            print 'Entitled in Zuora: '
            pprint(zuora)
            print 'Expected Products Entitled: '
            pprint (productsEntitled)
            print '=' * 70
        return keystone == zuora == productsEntitled
    
    def amendSubscription(self, subName):
        try:
            r = requests.put(self.UPDATE_SUB_URL + subName, data = json.dumps(
                self.UPDATE_SUB_INPUT, ensure_ascii = False),
                headers = self.CONNECTION_INPUT, timeout = self.TIMEOUT)
            a = json.loads(r.text)
            
            if a[u'success']:
                print 'Success'
                
                pprint (a)
            else:
                print 'Failure'
                print a
        except:
            raise
    
    def createSubscription(self, accountNumber, termLength):
        # Initialize accountKey to build sub on any account
        # and termlengths to accomodate 1, 2, 3 year subs
        self.CREATE_SUB_INPUT['accountKey'] = accountNumber
        self.CREATE_SUB_INPUT['initialTerm'] = termLength
        self.CREATE_SUB_INPUT['renewalTerm'] = termLength
        
        # try:
        # Call api to create an subscription
        r = requests.post(self.CREATE_SUB_URL, data = json.dumps(
            self.CREATE_SUB_INPUT, ensure_ascii = False), 
            headers = self.CONNECTION_INPUT, timeout = self.TIMEOUT)
        a = json.loads(r.text)
        
        if a[u'success']:
            print 'Successfully created subscription: ' + \
                a[u'subscriptionNumber']
            return a[u'subscriptionNumber']
        else:
            failCounter = 1
            while True:
                # Loop making subscription
                r = requests.post(self.CREATE_SUB_URL, data = json.dumps(
                self.CREATE_SUB_INPUT, ensure_ascii=False), 
                headers = self.CONNECTION_INPUT, timeout = self.TIMEOUT)
                a = json.loads(r.text)
                print a
                
                # Return when successful
                if a[u'success']:
                    print 'Successfully created subscription: ' + \
                        a[u'subscriptionNumber']
                    return a[u'subscriptionNumber']
                else:
                    # Increment counter when subscription making fails
                    failCounter += 15
                    time.sleep(5)
                    print 'Failed. Trying again.'
                    
                    # Raise error if fail counter exceeds timeout
                    if failCounter > self.TIMEOUT:
                        print  a[u'reasons'][0][u'message']
                        raise Exception('Failed to create subscription')
    
    def createAccount(self):
        # Call api to create an account
        r = requests.post(self.CREATE_ACC_URL, data = json.dumps(
            self.CREATE_ACC_INPUT, ensure_ascii=False),
            headers = self.CONNECTION_INPUT, timeout = self.TIMEOUT)
        a = json.loads(r.text)
        
        # Make sure response is good
        if not a['success']:
            pprint(a)
            raise Exception('Failed to create an account: ' + 
                a['reasons'][0]['message'])
        account = a[u'accountNumber']
        print 'Successfully created account: ' + account
        return account

    def getCatalog(self):
        # Call api to retrieve product list
        r = requests.get(self.GET_CATALOG_URL,
            headers = self.CONNECTION_INPUT, timeout = self.TIMEOUT)
        a = json.loads(r.text)['products']
        with open('product_catalog.json','w') as f:
            pprint(a, stream=f)

for i in a:
    for j in i['productRatePlans']:
        for k in j['productRatePlanCharges']:
            print i['name']
            print j['OfferDuration__c']
            print j['PortalDescription__c']
            print k['id']
        
        self._breakpoint()
        # Build dictionary of products
        for i in a:
            sku = i['sku']
            for j in i['productRatePlans']:
                # print sku + ' ' +  j['name'] + ' : ' + j['id']
                self.PRPID[sku + ' ' +  j['name']] = j['id']
        
    def setUp(self):
        self.CREATE_SUB_INPUT['contractEffectiveDate'] = self._add_today()
        self.CREATE_SUB_INPUT['invoiceTargetDate'] = self._add_today()
        self.CREATE_ACC_INPUT['name'] = 'Styx and Stones #' + str(int(time.time()))
        
        
    def tearDown(self):
        # Matt says dont delete keys
        # for i in self.CREATED_KEYS:
            # self._delete_key(i)
        pass
        
    
    # Fix detection for missing key/entitlement based on transactionID
    def searchKeystoneForEntitlements(self, id, type):
        url = self.KEYSEARCH
        body = {
            'search_token': id,
            'search_type': type,
        }
        
        try:
            # Call api to retrieve keys from Keystone
            # Wait to ensure keys have been created
            failureCount = 0
            while True:
                out = {}
                r = requests.post(url, data=json.dumps(body, ensure_ascii=False),
                headers=self.INPUT_TYPE, timeout=self.TIMEOUT)
                
                # Verify prime key in keystone is in keystone format
                if json.loads(r.text)['keys']:
                    assert re.match(self.KEYSTONE_REGEX, json.loads(r.text)['keys'][0]['license_key']) != None
                
                    for i in json.loads(r.text)['keys']:
                        for k in i['entitlements']:
                            for l in k['products']:
                                out[l['code']] = {}
                                out[l['code']]['termEndDate'] = self._add_today(k['term_length'])
                                out[l['code']]['volumePurchased'] = k['volume_purchased']
                                out[l['code']]['termType'] = k['term_type']
                            
                if out != {}:
                    break
                else:
                    if failureCount > self.TIMEOUT:
                        raise Exception('Timed out. Couldn\'t retrieve any entitlements.')
                    else:
                        # Waiting for Keystone
                        time.sleep(5)
                        failureCount += 5
                        
                    
            if r.ok:
                print 'Successfully retrieved %s from Keystone: %s' % (type, id)
                return out
            else:
                print 'Failed to retrieve %s from Keystone: %s' % (type, id)
                return
        except requests.exceptions.RequestException as e:
            print 'Request failed'
            print e
            raise
        
    def searchZuoraForEntitlements(self, subName):
        try:
            r = requests.get(self.GET_SUB_URL % subName, data=None, 
                headers = self.CONNECTION_INPUT, timeout = self.TIMEOUT)
            
            failCounter = self.TIMEOUT
            # Wait until License Key field is populated
            while True:
                r = requests.get(self.GET_SUB_URL % subName, data=None, 
                    headers = self.CONNECTION_INPUT, timeout = self.TIMEOUT)
                
                # Break when field is populated
                hash = json.loads(r.text)
                shared = hash[u'SHAREDLicenseKey__c']
                mbae = hash[u'MBAELicenseKey__c']
                mbam = hash[u'MBAMLicenseKey__c']
                if shared:
                    # addedKey = []
                    if mbae:
                        for i in mbae.split(' '):
                            print 'Searched key in Zuora: ' + i
                            assert re.match(self.MBAE_REGEX, i) != None
                            print 'Verified to be an MBAE key: ' + i
                        # addedKey = mbae.split(' ')[0]
                    if mbam:
                        for i in mbam.split(' '):
                            print 'Searched key in Zuora: ' + i
                            assert re.match(self.MBAM_REGEX, i) != None
                            print 'Verified to be an MBAM key: ' + i
                        # addedKey = mbam.split(' ')[0]
                    if shared:
                        for i in shared.split(' '):
                            print 'Searched key in Zuora: ' + i
                            assert re.match(self.KEYSTONE_REGEX, i) != None
                            print 'Verified to be an Keystone key: ' + i
                        # addedKey = shared.split(' ')[0]
                    # self.CREATED_KEYS = [addedKey]
                    break
                else:
                    # Continue waiting for it
                    failCounter += 5
                    if failCounter < self.TIMEOUT :
                        time.sleep(5)
                    else:
                        raise Exception('Zuora shared key field not populated.')
            
            # Convert string into hash
            out = {}
            time.sleep(5)
            zuoraJson = json.loads(r.text)
            
            for i in zuoraJson['ratePlans']:
                if i['productSku'] == 'MBES-B':
                    out[u'MBAM-B'] = {
                        'volumePurchased': int(i['ratePlanCharges'][0]['quantity']),
                        'termEndDate': i['ratePlanCharges'][0]['effectiveEndDate'],
                        'termType': u'subscription',
                    }
                    out[u'MBAE-B'] = {
                        'volumePurchased': int(i['ratePlanCharges'][0]['quantity']),
                        'termEndDate': i['ratePlanCharges'][0]['effectiveEndDate'],
                        'termType': u'subscription',
                    }
                    out[u'MBRX-B'] = {
                        'volumePurchased': int(i['ratePlanCharges'][0]['quantity']),
                        'termEndDate': i['ratePlanCharges'][0]['effectiveEndDate'],
                        'termType': u'subscription',
                    }
                elif i['productSku'] == 'MBMR-B':
                    out[u'MBMR-B'] = {
                        'volumePurchased': int(i['ratePlanCharges'][0]['quantity']),
                        'termEndDate': i['ratePlanCharges'][0]['effectiveEndDate'],
                        'termType': u'subscription',
                    }
                elif i['productSku'] in ['PRBS-B']:
                    pass
                else:
                    out[i['productSku']] = {
                        'volumePurchased': int(i['ratePlanCharges'][0]['quantity']),
                        'termEndDate': i['ratePlanCharges'][0]['effectiveEndDate'],
                        'termType': u'subscription',
                    }
                
            if r.ok:
                print 'Successfully retrieved subscription from Zuora: %s' % subName
            else:
                print 'Failed to retrieve subscription from Zuora: %s' % subName
            return out
        except requests.exceptions.RequestException as e:
            print 'Errored trying to retrieve subscription from Zuora: %s' % subName
        return {}
    
    def subscriptionTest(self, productRatePlan, entitledProducts, termLength):
        print 'Creating ' + str(entitledProducts.keys()[0])
        
        # Set product by rateplan
        self.CREATE_SUB_INPUT['subscribeToRatePlans'][0]['productRatePlanId'] = \
            self.PRPID[productRatePlan]
    
        # Create an account
        accountID = self.createAccount()
        
        # Create a subscription for the account
        subName = self.createSubscription(accountID, termLength)
        
        # Compare subscriptions in Zuora match Keystone
        assert self.compareKeystoneZuora(subName, entitledProducts)
        
        return subName
    
    def test_01_generate_catalog(self):
        self.getCatalog()
        
    @unittest.skipIf(skip, 'Off')
    def test_02_mbae_oneYear(self):
        years = 1
        prod = u'MBAE-B'
        for i in self.PRPID:
            if prod in i and str(years) + ' Year' in i and 'Discount' not in i and '(Int\'l)' not in i:
                print i
                self.subscriptionTest(i, {
                    prod: {
                        'termEndDate':self._add_today(years * 365), 
                        'volumePurchased': 1,
                        'termType': u'subscription'}},
                    years * 12)
        
    @unittest.skipIf(skip, 'Off')
    def test_03_mbae_twoYear(self):
        years = 2
        prod = u'MBAE-B'
        for i in self.PRPID:
            if prod in i and str(years) + ' Year' in i and 'Discount' not in i and '(Int\'l)' not in i:
                print i
                self.subscriptionTest(i, {
                    prod: {
                        'termEndDate':self._add_today(years * 365), 
                        'volumePurchased': 1,
                        'termType': u'subscription'}},
                    years * 12)
        
    @unittest.skipIf(skip, 'Off')
    def test_04_mbae_threeYear(self):
        years = 3
        prod = u'MBAE-B'
        for i in self.PRPID:
            if prod in i and str(years) + ' Year' in i and 'Discount' not in i and '(Int\'l)' not in i and 'Annual' not in i:
                print i
                self.subscriptionTest(i, {
                    prod: {
                        'termEndDate':self._add_today(years * 365), 
                        'volumePurchased': 1,
                        'termType': u'subscription'}},
                    years * 12)
                    
    @unittest.skipIf(skip, 'Off')
    def test_05_mbam_oneYear(self):
        years = 1
        prod = u'MBAM-B'
        for i in self.PRPID:
            if prod in i and str(years) + ' Year' in i and 'Discount' not in i and '(Int\'l)' not in i:
                print i
                self.subscriptionTest(i, {
                    prod: {
                        'termEndDate':self._add_today(years * 365), 
                        'volumePurchased': 1,
                        'termType': u'subscription'}},
                    years * 12)
        
    @unittest.skipIf(skip, 'Off')
    def test_06_mbam_twoYear(self):
        years = 2
        prod = u'MBAM-B'
        for i in self.PRPID:
            if prod in i and str(years) + ' Year' in i and 'Discount' not in i and '(Int\'l)' not in i:
                print i
                self.subscriptionTest(i, {
                    prod: {
                        'termEndDate':self._add_today(years * 365), 
                        'volumePurchased': 1,
                        'termType': u'subscription'}},
                    years * 12)
        
    @unittest.skipIf(skip, 'Off')
    def test_07_mbam_threeYear(self):
        years = 3
        prod = u'MBAM-B'
        for i in self.PRPID:
            if prod in i and str(years) + ' Year' in i and 'Discount' not in i and '(Int\'l)' not in i and 'Annual' not in i:
                print i
                self.subscriptionTest(i, {
                    prod: {
                        'termEndDate':self._add_today(years * 365), 
                        'volumePurchased': 1,
                        'termType': u'subscription'}},
                    years * 12)
                  
    @unittest.skipIf(skip, 'Off')  
    def test_08_mbes_oneYear(self):
        years = 1
        prod = u'MBES-B'
        for i in self.PRPID:
            if prod in i and str(years) + ' Year' in i and 'Discount' not in i and '(Int\'l)' not in i:
                print i
                self.subscriptionTest(i, {
                    'MBAM-B': {
                        'termEndDate':self._add_today(years * 365), 
                        'volumePurchased': 1,
                        'termType': u'subscription'},
                    'MBAE-B': {
                        'termEndDate':self._add_today(years * 365), 
                        'volumePurchased': 1,
                        'termType': u'subscription'},
                    'MBRX-B': {
                        'termEndDate':self._add_today(years * 365), 
                        'volumePurchased': 1,
                        'termType': u'subscription'},},
                    years * 12)
        
    @unittest.skipIf(skip, 'Off')
    def test_09_mbes_twoYear(self):
        years = 2
        prod = u'MBES-B'
        for i in self.PRPID:
            if prod in i and str(years) + ' Year' in i and 'Discount' not in i and '(Int\'l)' not in i:
                print i
                self.subscriptionTest(i, {
                    'MBAM-B': {
                        'termEndDate':self._add_today(years * 365), 
                        'volumePurchased': 1,
                        'termType': u'subscription'},
                    'MBAE-B': {
                        'termEndDate':self._add_today(years * 365), 
                        'volumePurchased': 1,
                        'termType': u'subscription'},
                    'MBRX-B': {
                        'termEndDate':self._add_today(years * 365), 
                        'volumePurchased': 1,
                        'termType': u'subscription'},},
                    years * 12)
        
    @unittest.skipIf(skip, 'Off')
    def test_10_mbes_threeYear(self):
        years = 3
        prod = u'MBES-B'
        for i in self.PRPID:
            if prod in i and str(years) + ' Year' in i and 'Discount' not in i and '(Int\'l)' not in i and 'Annual' not in i:
                print i
                self.subscriptionTest(i, {
                    'MBAM-B': {
                        'termEndDate':self._add_today(years * 365), 
                        'volumePurchased': 1,
                        'termType': u'subscription'},
                    'MBAE-B': {
                        'termEndDate':self._add_today(years * 365), 
                        'volumePurchased': 1,
                        'termType': u'subscription'},
                    'MBRX-B': {
                        'termEndDate':self._add_today(years * 365), 
                        'volumePurchased': 1,
                        'termType': u'subscription'},},
                    years * 12)
        
    @unittest.skipIf(skip, 'Off')
    def test_13_mbbr_oneYear(self):
        self.CREATE_SUB_INPUT[0]['subscribeToRatePlans']['chargeOverrides'] = [{
                'quantity': 1,
                'productRatePlanChargeId': '2c92c0f852b47fa10152db70efb94194',
            }]
        
        years = 1
        prod = u'MBBR-B'
        for i in self.PRPID:
            if prod in i and str(years) + ' Year' in i and 'Discount' not in i and '(Int\'l)' not in i:
                print i
                self.subscriptionTest(i, {
                    prod: {
                        'termEndDate':self._add_today(years * 365), 
                        'volumePurchased': 1}},
                    years * 12)
    
        
if __name__ == "__main__":
    # ed = EnvDict.ED()
    # ed['phase'] = utils.getKeyArg('phase', 'dev')
    # ed['outpath'] = utils.getKeyArg("outpath","test_results")
    # print ed['dev.CREATE_SUB_URL']
    
    
    # Setup output to xml for Jenkins
    t = datetime.utcnow()
    s = '{:>4}-{:>02}-{:>02}-{:>02}-{:>02}-{:>02}'.format(t.year, t.month,
        t.day, t.hour - 6, t.minute, t.second)
        
    tr=xmlrunner.XMLTestRunner(output = 'test_results', outsuffix = s,
        verbosity = 2)
    
    # Load test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(Stonez)
    
    # Run test suite
    tr.run(suite)
    
    '''
    search by transaction id
    check all keys that come back
    iterate through product listing in zuora
    product SKU (code), quantity, term end date -> compare with keystone keys/entitlements    
    '''

