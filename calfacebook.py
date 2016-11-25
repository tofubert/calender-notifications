import facebook

class FaceBookPoster(object):
    def __init__(self, tokenpath):
        self._token = open(tokenpath).read()
        self._graph = facebook.GraphAPI(access_token=self._token, version='2.2')
        self.group = self._graph.get_objects(ids=["728040737345863"])
        print(self.group["728040737345863"])

    def post_to_wall(self, message):
        self._graph.put_object(parent_object="728040737345863", connection_name='feed',
                               message="[BOTTESTING] "+message)
