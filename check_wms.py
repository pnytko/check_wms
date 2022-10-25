from owslib.wms import WebMapService

adres_wms = input(str("Podaj adres WMS: "))
wms = WebMapService(adres_wms)

title = wms.identification.title
type = wms.identification.type
version = wms.identification.version
layer_names = list(wms.contents)
abstract = wms.identification.abstract

print(f'{title}\n{type}\n{version}\n{layer_names}\n')

for layer_instance in layer_names:
    layer_title = wms[layer_instance].title
    layer_query = wms[layer_instance].queryable
    layer_opaque = wms[layer_instance].opaque
    layer_bbox = wms[layer_instance].boundingBox
    layer_bbox84 = wms[layer_instance].boundingBoxWGS84
    layer_crs = wms[layer_instance].crsOptions
    layer_styles = wms[layer_instance].styles
    print(layer_title)

print(layer_names)