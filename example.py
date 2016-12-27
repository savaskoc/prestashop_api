from prestashop_api import PrestashopApi

# Careful, api calls raise PrestashopError if request fails
api = PrestashopApi('http://localhost:8888/api', 'FRMIF6HLPH1ZCUK39MR9RSTDTJPD2K21')

print('Get')
res = api.get('products')
for p in res['products']['product']:
    print(p['@id'], p['@xlink:href'])

print('Search')
res = api.get('search', {'query': 'lorem', 'language': 1})
for p in res['products']['product']:
    print(p['@id'], p['@xlink:href'])

print('Add')
data = {'manufacturer': {'active': 1, 'name': 'Sample Manufacturer'}}  # Delete 'name' to get error
res = api.add('manufacturers', data)['manufacturer']
id = res['id']
print(id, res['name'])

print('Add Image')
res = api.add_image('manufacturers/' + id, 'ps_logo.png')  # set exists=True to replace image
print(res)

print('Edit')
data = {'manufacturer': {'id': id, 'name': 'Sample Manufacturer Edited'}}
res = api.edit('manufacturers', data)['manufacturer']
print(res['id'], res['name'])

print('Delete')
res = api.delete('manufacturers/' + res['id'])
print res
