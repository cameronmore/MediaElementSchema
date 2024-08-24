import json
import jsonschema

MediaElementSchema = "src/schema/MediaElementSchema.json"

def MediaElementSchemaValidator(jsonData):
    try:
        jsonschema.validate(json.loads(jsonData), MediaElementSchema)
        return True
    except jsonschema.ValidationError:
        return False

JSON_instance_sample = """{"title":"Love and Hate","author":{"firstName":"Robert","lastName":"Robertson"},"publisher":{"publisherName":"Penguin","location":"London"},"mediaType":"book","time":{"year":"2004"}}"""

MediaElementSchemaValidator(JSON_instance_sample)