from common import *

class ClassifierTest(BasicSkygridTest):
    def upload_ds(self):
        payload = dict(
            name=str(uuid.uuid4().hex),
            type="csv"
        )
        files = {'dataset': open('test_data.csv', 'rb')}

        r = requests.put(
            self.datasets_url,
            data=payload,
            files=files
        ).json()
        return r['data']['id']

    def delete_ds(self, ds_id):
        requests.delete(os.path.join(self.datasets_url, ds_id))

    def test_create(self):
        ds_id = self.upload_ds()
        payload = {
            'description' : str(uuid.uuid4().hex),
            'type' : "mn",
            'parameters' : {'a': 'b'},
            'dataset': ds_id
        }

        r = requests.put(
            self.classifiers_url,
            data=json.dumps(payload),
            headers=self.json_headers
        ).json()

        self.assertTrue(r['success'])
        data = r['data']

        self.assertEqual(data['description'], payload['description'])
        self.assertEqual(data['type'], payload['type'])
        self.assertEqual(data['parameters'], payload['parameters'])


        r = requests.delete(
            os.path.join(self.classifiers_url, data['classifier_id'])
        ).json()

        self.assertTrue(r['success'])

        self.delete_ds(ds_id)

