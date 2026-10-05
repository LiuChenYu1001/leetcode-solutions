from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.follower = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []
        users = self.follower[userId] | {userId}

        for user in users:
            if not self.tweets[user]:
                continue

            idx = len(self.tweets[user]) - 1
            time, tweet_id = self.tweets[user][idx]
            heap.append((-time, tweet_id, user, idx))

        heapq.heapify(heap)
        result = []

        while heap and len(result) < 10:
            _, tweet_id, user, idx = heapq.heappop(heap)
            result.append(tweet_id)

            if idx > 0:
                pre_idx = idx - 1
                time, tweet_id = self.tweets[user][pre_idx]
                heapq.heappush(heap, (-time, tweet_id, user, pre_idx))

        return result 

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)