import  pymysql
import requests
import unittest
import os

db = pymysql.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="Bigcommerce@2021",  # your password
                     db="UnitTest")

cur = db.cursor()
query = ("SELECT * FROM visitor")
cur.execute(query)
res =  cur.fetchall()
length = len(res)
db.close()

query_output = []
for i in (res):
    query_output.append(i)




#RUN_UNIT_TEST = os.environ.get('RUN_UNIT_TEST', False)
RUN_UNIT_TEST = True
class TestAPI(unittest.TestCase):
    bc_auth = 'bc_auth_session=bc%3Aoauth_session%3A9698d416c7a133d73c3fd8b80a8770283e042b60cb35ade08c48f32dece2b3d6'
    STORESUITE_TOKEN = 'STORESUITE_CP_TOKEN=63W2895DSQUKC59R6P40W5QPX5G'

    headers = {
        'Cookie': bc_auth + ';' + STORESUITE_TOKEN
    }
    r = requests.get('https://store-xhuahctw45.my-integration.zone/manage/analytics-code', headers=headers)
    response_body = r.json()
    #print(response_body["code"])
    payload = response_body["code"]
    header_json = {'BC-SignedPayload': payload}
    store_id = '14984474'
    base_url = 'https://blaze-api-integration.bigcommerce.net/visitors'
    compare_date = '2021-09-29,2021-10-29'
    observe_date = '2021-09-30'
    limit = '10'
    page = '1'
    sortby = 'revenue'
    sortdir = 'None'
    request_url = '{base_url}/{store_id}?compare={compare_date}&observe={observe_date}&limit={limit}&page={page}&sortby={sortby}&sortdir={sortdir}'.format(
        base_url=base_url, store_id=store_id, compare_date=compare_date, observe_date=observe_date, limit=limit,
        page=page, sortby=sortby, sortdir=sortdir)

    @unittest.skipUnless(RUN_UNIT_TEST == True, reason="unit test not required")
    def test_visitor_endpoint_status_code_equals_200(self):

        response = requests.get(TestAPI.request_url, headers=TestAPI.header_json)
        assert response.status_code == 200

    @unittest.skipUnless(RUN_UNIT_TEST == True, reason="unit test not required")
    def test_visitor_endpoint_length_matches_res(self):
        response = requests.get(TestAPI.request_url, headers=TestAPI.header_json)
        response_body = response.json()
        #print("Endpoint Data", len(response_body["data"]))
        assert len(response_body["data"]) == len(res)

    @unittest.skipUnless(RUN_UNIT_TEST == True and length != 0, reason="unit test not required")
    def test_visitor_endpoint_validate_data_after_sorting_rev_desc(self):
        request_url = '{base_url}/{store_id}?compare={compare_date}&observe={observe_date}&limit={limit}&page={page}&sortby={sortby}&sortdir={sortdir}'.format(
            base_url=TestAPI.base_url, store_id=TestAPI.store_id, compare_date=TestAPI.compare_date,observe_date=TestAPI.observe_date, limit=TestAPI.limit,
            page=TestAPI.page, sortby="revenue", sortdir="desc")
        response = requests.get(request_url, headers=TestAPI.header_json)
        response_body = response.json()
        #print(response_body["data"])
        sort_by_rev = sorted(query_output, key=lambda x: x[1], reverse=True)

        #print("here",sort_by_rev)
        for i in range(length):

            assert response_body["data"][i]["origin"].encode("ascii") == sort_by_rev[i][0]
            assert round(response_body["data"][i]["revenue"],2) == round(float(sort_by_rev[i][1]),2)
            assert response_body["data"][i]["visits"] == sort_by_rev[i][2]
            assert response_body["data"][i]["orders"] == sort_by_rev[i][3]
            assert round(response_body["data"][i]["conv_rate"],2) == round(float(sort_by_rev[i][4]*100),2)
            assert round(response_body["data"][i]["aov"],4) == round(float(sort_by_rev[i][5]),4)
            assert round(response_body["data"][i]["rpv"],4) == round(float(sort_by_rev[i][6]),4)
            assert response_body["data"][i]["children"] == sort_by_rev[i][7]

    @unittest.skipUnless(RUN_UNIT_TEST == True and length != 0, reason="unit test not required")
    def test_visitor_endpoint_validate_data_after_sorting_rev_asc(self):
        request_url = '{base_url}/{store_id}?compare={compare_date}&observe={observe_date}&limit={limit}&page={page}&sortby={sortby}&sortdir={sortdir}'.format(
            base_url=TestAPI.base_url, store_id=TestAPI.store_id, compare_date=TestAPI.compare_date, observe_date=TestAPI.observe_date, limit=TestAPI.limit,
            page=TestAPI.page, sortby="revenue", sortdir="asc")
        #print("responseapi", request_url)
        response = requests.get(request_url, headers=TestAPI.header_json)
        response_body = response.json()
        #print(response_body["data"])
        sort_by_rev = sorted(query_output, key=lambda x: x[1], reverse=False)

        #print("here",sort_by_rev)
        for i in range(length):

            assert response_body["data"][i]["origin"].encode("ascii") == sort_by_rev[i][0]
            assert round(response_body["data"][i]["revenue"],2) == round(float(sort_by_rev[i][1]),2)
            assert response_body["data"][i]["visits"] == sort_by_rev[i][2]
            assert response_body["data"][i]["orders"] == sort_by_rev[i][3]
            assert round(response_body["data"][i]["conv_rate"],2) == round(float(sort_by_rev[i][4]*100),2)
            assert round(response_body["data"][i]["aov"],4) == round(float(sort_by_rev[i][5]),4)
            assert round(response_body["data"][i]["rpv"],4) == round(float(sort_by_rev[i][6]),4)
            assert response_body["data"][i]["children"] == sort_by_rev[i][7]

    @unittest.skipUnless(RUN_UNIT_TEST == True and length != 0, reason="unit test not required")
    def test_visitor_endpoint_validate_data_after_sorting_origin_desc(self):
        request_url = '{base_url}/{store_id}?compare={compare_date}&observe={observe_date}&limit={limit}&page={page}&sortby={sortby}&sortdir={sortdir}'.format(
            base_url=TestAPI.base_url, store_id=TestAPI.store_id, compare_date=TestAPI.compare_date,
            observe_date=TestAPI.observe_date, limit=TestAPI.limit,
            page=TestAPI.page, sortby="origin", sortdir="desc")
        response = requests.get(request_url, headers=TestAPI.header_json)
        response_body = response.json()
        #print("api data", response_body["data"])
        sort_by_org = sorted(query_output, key=lambda x: x[0], reverse=True)

        #print("query data", sort_by_org)
        for i in range(length):
            assert response_body["data"][i]["origin"].encode("ascii") == sort_by_org[i][0]
            assert round(response_body["data"][i]["revenue"], 2) == round(float(sort_by_org[i][1]), 2)
            assert response_body["data"][i]["visits"] == sort_by_org[i][2]
            assert response_body["data"][i]["orders"] == sort_by_org[i][3]
            assert round(response_body["data"][i]["conv_rate"], 2) == round(float(sort_by_org[i][4] * 100), 2)
            assert round(response_body["data"][i]["aov"], 4) == round(float(sort_by_org[i][5]), 4)
            assert round(response_body["data"][i]["rpv"], 4) == round(float(sort_by_org[i][6]), 4)
            assert response_body["data"][i]["children"] == sort_by_org[i][7]

    def test_visitor_endpoint_validate_data_after_sorting_origin_asc(self):
        request_url = '{base_url}/{store_id}?compare={compare_date}&observe={observe_date}&limit={limit}&page={page}&sortby={sortby}&sortdir={sortdir}'.format(
            base_url=TestAPI.base_url, store_id=TestAPI.store_id, compare_date=TestAPI.compare_date,
            observe_date=TestAPI.observe_date, limit=TestAPI.limit,
            page=TestAPI.page, sortby="origin", sortdir="asc")
        response = requests.get(request_url, headers=TestAPI.header_json)
        response_body = response.json()
        #print("api data", response_body["data"])
        sort_by_org = sorted(query_output, key=lambda x: x[0], reverse=False)

        #print("query data", sort_by_org)
        for i in range(length):
            assert response_body["data"][i]["origin"].encode("ascii") == sort_by_org[i][0]
            assert round(response_body["data"][i]["revenue"], 2) == round(float(sort_by_org[i][1]), 2)
            assert response_body["data"][i]["visits"] == sort_by_org[i][2]
            assert response_body["data"][i]["orders"] == sort_by_org[i][3]
            assert round(response_body["data"][i]["conv_rate"], 2) == round(float(sort_by_org[i][4] * 100), 2)
            assert round(response_body["data"][i]["aov"], 4) == round(float(sort_by_org[i][5]), 4)
            assert round(response_body["data"][i]["rpv"], 4) == round(float(sort_by_org[i][6]), 4)
            assert response_body["data"][i]["children"] == sort_by_org[i][7]

    @unittest.skipUnless(RUN_UNIT_TEST == True and length != 0, reason="unit test not required")
    def test_visitor_endpoint_validate_data_after_sorting_visits_desc(self):
        request_url = '{base_url}/{store_id}?compare={compare_date}&observe={observe_date}&limit={limit}&page={page}&sortby={sortby}&sortdir={sortdir}'.format(
            base_url=TestAPI.base_url, store_id=TestAPI.store_id, compare_date=TestAPI.compare_date,
            observe_date=TestAPI.observe_date, limit=TestAPI.limit,
            page=TestAPI.page, sortby="visits", sortdir="desc")
        response = requests.get(request_url, headers=TestAPI.header_json)
        response_body = response.json()
        #print("api data", response_body["data"])
        sort_by_visits = sorted(query_output, key=lambda x: x[2], reverse=True)

        #print("query data", sort_by_visits)
        for i in range(length):
            assert response_body["data"][i]["origin"].encode("ascii") == sort_by_visits[i][0]
            assert round(response_body["data"][i]["revenue"], 2) == round(float(sort_by_visits[i][1]), 2)
            assert response_body["data"][i]["visits"] == sort_by_visits[i][2]
            assert response_body["data"][i]["orders"] == sort_by_visits[i][3]
            assert round(response_body["data"][i]["conv_rate"], 2) == round(float(sort_by_visits[i][4] * 100), 2)
            assert round(response_body["data"][i]["aov"], 4) == round(float(sort_by_visits[i][5]), 4)
            assert round(response_body["data"][i]["rpv"], 4) == round(float(sort_by_visits[i][6]), 4)
            assert response_body["data"][i]["children"] == sort_by_visits[i][7]

    @unittest.skipUnless(RUN_UNIT_TEST == True and length != 0, reason="unit test not required")
    def test_visitor_endpoint_validate_data_after_sorting_visits_asc(self):
        request_url = '{base_url}/{store_id}?compare={compare_date}&observe={observe_date}&limit={limit}&page={page}&sortby={sortby}&sortdir={sortdir}'.format(
            base_url=TestAPI.base_url, store_id=TestAPI.store_id, compare_date=TestAPI.compare_date,
            observe_date=TestAPI.observe_date, limit=TestAPI.limit,
            page=TestAPI.page, sortby="visits", sortdir="asc")
        response = requests.get(request_url, headers=TestAPI.header_json)
        response_body = response.json()
        #print("api data", response_body["data"])
        sort_by_visits = sorted(query_output, key=lambda x: x[2], reverse=False)

        #print("query data", sort_by_visits)
        for i in range(length):
            assert response_body["data"][i]["origin"].encode("ascii") == sort_by_visits[i][0]
            assert round(response_body["data"][i]["revenue"], 2) == round(float(sort_by_visits[i][1]), 2)
            assert response_body["data"][i]["visits"] == sort_by_visits[i][2]
            assert response_body["data"][i]["orders"] == sort_by_visits[i][3]
            assert round(response_body["data"][i]["conv_rate"], 2) == round(float(sort_by_visits[i][4] * 100), 2)
            assert round(response_body["data"][i]["aov"], 4) == round(float(sort_by_visits[i][5]), 4)
            assert round(response_body["data"][i]["rpv"], 4) == round(float(sort_by_visits[i][6]), 4)
            assert response_body["data"][i]["children"] == sort_by_visits[i][7]

    @unittest.skipUnless(RUN_UNIT_TEST == True and length != 0, reason="unit test not required")
    def test_visitor_endpoint_validate_data_after_sorting_orders_desc(self):
        request_url = '{base_url}/{store_id}?compare={compare_date}&observe={observe_date}&limit={limit}&page={page}&sortby={sortby}&sortdir={sortdir}'.format(
            base_url=TestAPI.base_url, store_id=TestAPI.store_id, compare_date=TestAPI.compare_date,
            observe_date=TestAPI.observe_date, limit=TestAPI.limit,
            page=TestAPI.page, sortby="orders", sortdir="desc")
        response = requests.get(request_url, headers=TestAPI.header_json)
        response_body = response.json()
        #print("api data", response_body["data"])
        sort_by_orders = sorted(query_output, key=lambda x: x[3], reverse=True)

        #print("query data", sort_by_orders)
        for i in range(length):
            assert response_body["data"][i]["origin"].encode("ascii") == sort_by_orders[i][0]
            assert round(response_body["data"][i]["revenue"], 2) == round(float(sort_by_orders[i][1]), 2)
            assert response_body["data"][i]["visits"] == sort_by_orders[i][2]
            assert response_body["data"][i]["orders"] == sort_by_orders[i][3]
            assert round(response_body["data"][i]["conv_rate"], 2) == round(float(sort_by_orders[i][4] * 100), 2)
            assert round(response_body["data"][i]["aov"], 4) == round(float(sort_by_orders[i][5]), 4)
            assert round(response_body["data"][i]["rpv"], 4) == round(float(sort_by_orders[i][6]), 4)
            assert response_body["data"][i]["children"] == sort_by_orders[i][7]

    @unittest.skipUnless(RUN_UNIT_TEST == True and length != 0, reason="unit test not required")
    def test_visitor_endpoint_validate_data_after_sorting_orders_asc(self):
        request_url = '{base_url}/{store_id}?compare={compare_date}&observe={observe_date}&limit={limit}&page={page}&sortby={sortby}&sortdir={sortdir}'.format(
            base_url=TestAPI.base_url, store_id=TestAPI.store_id, compare_date=TestAPI.compare_date,
            observe_date=TestAPI.observe_date, limit=TestAPI.limit,
            page=TestAPI.page, sortby="orders", sortdir="asc")
        response = requests.get(request_url, headers=TestAPI.header_json)
        response_body = response.json()
        #print("api data", response_body["data"])
        sort_by_orders = sorted(query_output, key=lambda x: x[3], reverse=False)

        #print("query data", sort_by_orders)
        for i in range(length):
            assert response_body["data"][i]["origin"].encode("ascii") == sort_by_orders[i][0]
            assert round(response_body["data"][i]["revenue"], 2) == round(float(sort_by_orders[i][1]), 2)
            assert response_body["data"][i]["visits"] == sort_by_orders[i][2]
            assert response_body["data"][i]["orders"] == sort_by_orders[i][3]
            assert round(response_body["data"][i]["conv_rate"], 2) == round(float(sort_by_orders[i][4] * 100), 2)
            assert round(response_body["data"][i]["aov"], 4) == round(float(sort_by_orders[i][5]), 4)
            assert round(response_body["data"][i]["rpv"], 4) == round(float(sort_by_orders[i][6]), 4)
            assert response_body["data"][i]["children"] == sort_by_orders[i][7]

    @unittest.skipUnless(RUN_UNIT_TEST == True and length != 0, reason="unit test not required")
    def test_visitor_endpoint_validate_data_after_sorting_conv_rate_desc(self):
        request_url = '{base_url}/{store_id}?compare={compare_date}&observe={observe_date}&limit={limit}&page={page}&sortby={sortby}&sortdir={sortdir}'.format(
            base_url=TestAPI.base_url, store_id=TestAPI.store_id, compare_date=TestAPI.compare_date,
            observe_date=TestAPI.observe_date, limit=TestAPI.limit,
            page=TestAPI.page, sortby="conv_rate", sortdir="desc")
        response = requests.get(request_url, headers=TestAPI.header_json)
        response_body = response.json()
        #print("api data", response_body["data"])
        sort_by_conv_rate = sorted(query_output, key=lambda x: x[4], reverse=True)

        #print("query data", sort_by_conv_rate)
        for i in range(length):
            assert response_body["data"][i]["origin"].encode("ascii") == sort_by_conv_rate[i][0]
            assert round(response_body["data"][i]["revenue"], 2) == round(float(sort_by_conv_rate[i][1]), 2)
            assert response_body["data"][i]["visits"] == sort_by_conv_rate[i][2]
            assert response_body["data"][i]["orders"] == sort_by_conv_rate[i][3]
            assert round(response_body["data"][i]["conv_rate"], 2) == round(float(sort_by_conv_rate[i][4] * 100), 2)
            assert round(response_body["data"][i]["aov"], 4) == round(float(sort_by_conv_rate[i][5]), 4)
            assert round(response_body["data"][i]["rpv"], 4) == round(float(sort_by_conv_rate[i][6]), 4)
            assert response_body["data"][i]["children"] == sort_by_conv_rate[i][7]

    @unittest.skipUnless(RUN_UNIT_TEST == True and length != 0, reason="unit test not required")
    def test_visitor_endpoint_validate_data_after_sorting_conv_rate_asc(self):
        request_url = '{base_url}/{store_id}?compare={compare_date}&observe={observe_date}&limit={limit}&page={page}&sortby={sortby}&sortdir={sortdir}'.format(
            base_url=TestAPI.base_url, store_id=TestAPI.store_id, compare_date=TestAPI.compare_date,
            observe_date=TestAPI.observe_date, limit=TestAPI.limit,
            page=TestAPI.page, sortby="conv_rate", sortdir="asc")
        response = requests.get(request_url, headers=TestAPI.header_json)
        response_body = response.json()
        #print("api data", response_body["data"])
        sort_by_conv_rate = sorted(query_output, key=lambda x: x[4], reverse=False)

        #print("query data", sort_by_conv_rate)
        for i in range(length):
            assert response_body["data"][i]["origin"].encode("ascii") == sort_by_conv_rate[i][0]
            assert round(response_body["data"][i]["revenue"], 2) == round(float(sort_by_conv_rate[i][1]), 2)
            assert response_body["data"][i]["visits"] == sort_by_conv_rate[i][2]
            assert response_body["data"][i]["orders"] == sort_by_conv_rate[i][3]
            assert round(response_body["data"][i]["conv_rate"], 2) == round(float(sort_by_conv_rate[i][4] * 100), 2)
            assert round(response_body["data"][i]["aov"], 4) == round(float(sort_by_conv_rate[i][5]), 4)
            assert round(response_body["data"][i]["rpv"], 4) == round(float(sort_by_conv_rate[i][6]), 4)
            assert response_body["data"][i]["children"] == sort_by_conv_rate[i][7]

    @unittest.skipUnless(RUN_UNIT_TEST == True and length != 0, reason="unit test not required")
    def test_visitor_endpoint_validate_data_after_sorting_aov_desc(self):
        request_url = '{base_url}/{store_id}?compare={compare_date}&observe={observe_date}&limit={limit}&page={page}&sortby={sortby}&sortdir={sortdir}'.format(
            base_url=TestAPI.base_url, store_id=TestAPI.store_id, compare_date=TestAPI.compare_date,
            observe_date=TestAPI.observe_date, limit=TestAPI.limit,
            page=TestAPI.page, sortby="aov", sortdir="desc")
        response = requests.get(request_url, headers=TestAPI.header_json)
        response_body = response.json()
        #print("api data", response_body["data"])
        sort_by_aov = sorted(query_output, key=lambda x: x[5], reverse=True)

        #print("query data", sort_by_aov)
        for i in range(length):
            assert response_body["data"][i]["origin"].encode("ascii") == sort_by_aov[i][0]
            assert round(response_body["data"][i]["revenue"], 2) == round(float(sort_by_aov[i][1]), 2)
            assert response_body["data"][i]["visits"] == sort_by_aov[i][2]
            assert response_body["data"][i]["orders"] == sort_by_aov[i][3]
            assert round(response_body["data"][i]["conv_rate"], 2) == round(float(sort_by_aov[i][4] * 100), 2)
            assert round(response_body["data"][i]["aov"], 4) == round(float(sort_by_aov[i][5]), 4)
            assert round(response_body["data"][i]["rpv"], 4) == round(float(sort_by_aov[i][6]), 4)
            assert response_body["data"][i]["children"] == sort_by_aov[i][7]

    @unittest.skipUnless(RUN_UNIT_TEST == True and length != 0, reason="unit test not required")
    def test_visitor_endpoint_validate_data_after_sorting_aov_asc(self):
        request_url = '{base_url}/{store_id}?compare={compare_date}&observe={observe_date}&limit={limit}&page={page}&sortby={sortby}&sortdir={sortdir}'.format(
            base_url=TestAPI.base_url, store_id=TestAPI.store_id, compare_date=TestAPI.compare_date,
            observe_date=TestAPI.observe_date, limit=TestAPI.limit,
            page=TestAPI.page, sortby="aov", sortdir="asc")
        response = requests.get(request_url, headers=TestAPI.header_json)
        response_body = response.json()
        #print("api data", response_body["data"])
        sort_by_aov = sorted(query_output, key=lambda x: x[5], reverse=False)

        #print("query data", sort_by_aov)
        for i in range(length):
            assert response_body["data"][i]["origin"].encode("ascii") == sort_by_aov[i][0]
            assert round(response_body["data"][i]["revenue"], 2) == round(float(sort_by_aov[i][1]), 2)
            assert response_body["data"][i]["visits"] == sort_by_aov[i][2]
            assert response_body["data"][i]["orders"] == sort_by_aov[i][3]
            assert round(response_body["data"][i]["conv_rate"], 2) == round(float(sort_by_aov[i][4] * 100), 2)
            assert round(response_body["data"][i]["aov"], 4) == round(float(sort_by_aov[i][5]), 4)
            assert round(response_body["data"][i]["rpv"], 4) == round(float(sort_by_aov[i][6]), 4)
            assert response_body["data"][i]["children"] == sort_by_aov[i][7]

    @unittest.skipUnless(RUN_UNIT_TEST == True and length != 0, reason="unit test not required")
    def test_visitor_endpoint_validate_data_after_sorting_rpv_desc(self):
        request_url = '{base_url}/{store_id}?compare={compare_date}&observe={observe_date}&limit={limit}&page={page}&sortby={sortby}&sortdir={sortdir}'.format(
            base_url=TestAPI.base_url, store_id=TestAPI.store_id, compare_date=TestAPI.compare_date,
            observe_date=TestAPI.observe_date, limit=TestAPI.limit,
            page=TestAPI.page, sortby="rpv", sortdir="desc")
        response = requests.get(request_url, headers=TestAPI.header_json)
        response_body = response.json()
        #print("api data", response_body["data"])
        sort_by_rpv = sorted(query_output, key=lambda x: x[6], reverse=True)

        #print("query data", sort_by_rpv)
        for i in range(length):
            assert response_body["data"][i]["origin"].encode("ascii") == sort_by_rpv[i][0]
            assert round(response_body["data"][i]["revenue"], 2) == round(float(sort_by_rpv[i][1]), 2)
            assert response_body["data"][i]["visits"] == sort_by_rpv[i][2]
            assert response_body["data"][i]["orders"] == sort_by_rpv[i][3]
            assert round(response_body["data"][i]["conv_rate"], 2) == round(float(sort_by_rpv[i][4] * 100), 2)
            assert round(response_body["data"][i]["aov"], 4) == round(float(sort_by_rpv[i][5]), 4)
            assert round(response_body["data"][i]["rpv"], 4) == round(float(sort_by_rpv[i][6]), 4)
            assert response_body["data"][i]["children"] == sort_by_rpv[i][7]

    @unittest.skipUnless(RUN_UNIT_TEST == True and length != 0, reason="unit test not required")
    def test_visitor_endpoint_validate_data_after_sorting_rpv_asc(self):
        request_url = '{base_url}/{store_id}?compare={compare_date}&observe={observe_date}&limit={limit}&page={page}&sortby={sortby}&sortdir={sortdir}'.format(
            base_url=TestAPI.base_url, store_id=TestAPI.store_id, compare_date=TestAPI.compare_date,
            observe_date=TestAPI.observe_date, limit=TestAPI.limit,
            page=TestAPI.page, sortby="rpv", sortdir="asc")
        response = requests.get(request_url, headers=TestAPI.header_json)
        response_body = response.json()
        #print("api data", response_body["data"])
        sort_by_rpv = sorted(query_output, key=lambda x: x[6], reverse=False)

        #print("query data", sort_by_rpv)
        for i in range(length):
            assert response_body["data"][i]["origin"].encode("ascii") == sort_by_rpv[i][0]
            assert round(response_body["data"][i]["revenue"], 2) == round(float(sort_by_rpv[i][1]), 2)
            assert response_body["data"][i]["visits"] == sort_by_rpv[i][2]
            assert response_body["data"][i]["orders"] == sort_by_rpv[i][3]
            assert round(response_body["data"][i]["conv_rate"], 2) == round(float(sort_by_rpv[i][4] * 100), 2)
            assert round(response_body["data"][i]["aov"], 4) == round(float(sort_by_rpv[i][5]), 4)
            assert round(response_body["data"][i]["rpv"], 4) == round(float(sort_by_rpv[i][6]), 4)
            assert response_body["data"][i]["children"] == sort_by_rpv[i][7]

    @unittest.skipUnless(RUN_UNIT_TEST == True and length != 0, reason="unit test not required")
    def test_visitor_endpoint_validate_data_with_limit(self):
        request_url = '{base_url}/{store_id}?compare={compare_date}&observe={observe_date}&limit={limit}&page={page}&sortby={sortby}&sortdir={sortdir}'.format(
            base_url=TestAPI.base_url, store_id=TestAPI.store_id, compare_date=TestAPI.compare_date,
            observe_date=TestAPI.observe_date, limit=1,
            page=TestAPI.page, sortby="revenue", sortdir="desc")
        response = requests.get(request_url, headers=TestAPI.header_json)
        response_body = response.json()
        assert len(response_body["data"]) == 1


if __name__ == '__main__':
    unittest.main()
