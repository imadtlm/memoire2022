from nomad import *
config.client.url = 'http://nomad-lab.eu/prod/rae/api'
results = client.query_archive(query={
    'upload_id': ['4xjU-M2pT4yAaFpKIT0ZPg'],
    'calc_id': ['aQ-9vE9bXJLG-KFC0A0oTmTemEHs']})
print(results)
