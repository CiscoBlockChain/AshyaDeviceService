from mimesis.schema import Field, Schema
from mimesis.enums import Gender


def generate():
    _ = Field('en')
    description = (
    lambda: {
        'timestamp': _('timestamp', posix=False),
        'id': _('uuid'),
        'name': _('text.word'),
        'owner': {
                'token': _('token'),
                'creator': _('full_name', gender=Gender.FEMALE),
                },
                }
        )
    schema = Schema(schema=description)
    r = schema.create(iterations=1)
    print(r)
    


        
if __name__ == "__main__":
    generate()