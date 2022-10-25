from owslib.wms import WebMapService

adres_wms = 'https://mapserver.bdl.lasy.gov.pl/ArcGIS/services/WMS_BDL_Mapa_turystyczna/MapServer/WMSServer'
wms = WebMapService(adres_wms)

title = wms.identification.title
type = wms.identification.type
version = wms.identification.version
layer_names = list(wms.contents)
abstract = wms.identification.abstract

print(f'{title}\n{type}\n{version}\n{layer_names}\n')

header = 'title;index\n'
with open('output.csv', 'w') as output_file:
    output_file.write(header)


output_file = open('output.csv', 'a')
for layer_instance in layer_names:
    layer_title = wms[layer_instance].title
    layer_query = wms[layer_instance].queryable
    layer_opaque = wms[layer_instance].opaque
    layer_bbox = wms[layer_instance].boundingBox
    layer_bbox84 = wms[layer_instance].boundingBoxWGS84
    layer_crs = wms[layer_instance].crsOptions
    layer_styles = wms[layer_instance].styles
    output_file.write(f'{layer_title};{layer_instance}\n')
    print(layer_title)

output_file.close()
