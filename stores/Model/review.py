import json


class Review:
    def __init__(self, app_id, review_id, author, date, stars, title, body, raw_review):
        self.id = review_id
        self.date = date
        self.title = title
        self.body = body
        self.app_id = app_id
        self.stars = stars
        self.author = author
        self.raw_review = raw_review

    # NICE TO HAVE implement __eq__ and __hash__ to drop duplicates form countries that return the same reviews
    # def __eq__(self, other):
    #    return self.__dict__ == other.__dict__

    def to_json(self):
        return json.dumps({k: v for k, v in self.__dict__.items() if not isinstance(v, bytes)})


class GooglePlayReview(Review):

    def __init__(self, app_id, review_id, author, date, stars, title, body, perma_link, raw_review):
        super().__init__(app_id, review_id, author, date, stars, title, body, raw_review)
        self.perma_link = perma_link


class AppStoreReview(Review):

    def __init__(self, app_id, review_id, author, date, stars, title, body, version, raw_review):
        super().__init__(app_id, review_id, author, date, stars, title, body, raw_review)
        self.version = version
