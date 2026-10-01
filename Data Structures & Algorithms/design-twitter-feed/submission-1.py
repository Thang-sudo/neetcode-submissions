class Twitter:

    def __init__(self):
        self.follow_map = defaultdict(set) # Track which user is following which user
        self.tweet_map = defaultdict(list) # Track an user posts which tweet
        self.timestamp = 0 # Decrement whenever an user post a tweet. Tweet with smallest time stamp would be on top of the tweet.

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp -= 1
        # If user never posts a tweet before
        self.tweet_map[userId].append((self.timestamp, tweetId)) # a tweet is a tuple of (timestamp, tweetId). The list is a stack of tweets ordered from oldest to newest

    def getNewsFeed(self, userId: int) -> List[int]:
        news_feed = [] # news feed is a list of tweet id
        min_heap = []
        # Iterate the list of followee of this user and pick their latest tweets as seeds to generate a min heap
        self.follow_map[userId].add(userId)
        for followee in self.follow_map[userId]:
            # The followee must have at least one tweet for seeding
            tweets = self.tweet_map[followee]
            if len(tweets):
                i = len(tweets) - 1
                recency, tweet_id = tweets[i]
                min_heap.append((recency, tweet_id, followee, i)) # Last element of tuple is the index of the followee's tweet list. Need to check if this user has any older tweet. Any older tweet potentially newer than seeding tweets. So they might be return in the newsfeed list
        # heapify the generated list
        heapq.heapify(min_heap)
        while min_heap and len(news_feed) < 10:
            recency, tweet_id, followee, i = heapq.heappop(min_heap)
            news_feed.append(tweet_id)
            if i - 1 >= 0: # Meaning there's an older tweet for this followee
                # Get that older tweet and push it to the heap
                recency, tweet_id = self.tweet_map[followee][i - 1]
                heapq.heappush(min_heap, (recency, tweet_id, followee, i - 1))
        return news_feed


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)

        
