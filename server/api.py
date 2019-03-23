import settings
import models
import responder
from handlers import WineAttributeResource, PredictionResource

models.main()
api = responder.API(
    cors=True,
    allowed_hosts=["*"],
)

api.add_route('/api/wine_attributes', WineAttributeResource)
api.add_route('/api/predict', PredictionResource)

if __name__ == '__main__':
    api.run(address="0.0.0.0", port=5432, debug=True)
