class FeedBack :
    def __init__(self, user_id, movie_id, rating, comments = None):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating
        self.comments = comments
        self.feedback_dict = {}

    def __str__(self):
        return f"user {self.user_id} rate movie {self.movie_id} : {self.rating} and comments : {self.comments}"

    def create_feedback(Self, obj):
        Self.feedback_dict[obj.user_id] = obj
        print("created!")
        
    def add_fedback(self) :
        with open("feedbacks.json", "w") as file:
            json.dump(self.feedback_dict, file, indent=4, sort_keys=True)
        print("done")

    def show_feedbacks(self):
        try:
            with open("feedbacks.json", "r") as file1:
                res = json.load(file1)
            print(res)
        except EOFError:
            print("file is empty")