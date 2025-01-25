from collections import deque

suggested_links = deque(map(int, input().split()))  # FIFO
featured_articles = list(map(int, input().split()))  # LIFO
target_value = int(input())
final_feed = []

while suggested_links and featured_articles:
    link = suggested_links.popleft()
    article = featured_articles.pop()

    if article > link:
        remainder = article % link
        final_feed.append(remainder)
        remainder *= 2
        if remainder != 0:
            featured_articles.append(remainder)

    elif article < link:
        remainder = link % article
        final_feed.append(-remainder)
        remainder *= 2
        if remainder != 0:
            suggested_links.append(remainder)

    else:
        final_feed.append(0)

total_engagement_value = sum(final_feed)
print(f"Final Feed: {', '.join(map(str, final_feed))}")
if total_engagement_value >= target_value:
    print(f"Goal achieved! Engagement Value: {total_engagement_value}")
else:
    shortfall = target_value - total_engagement_value
    print(f"Goal not achieved! Short by: {shortfall}")



##############################################################################################
# from collections import deque

# suggested_links = deque(map(int, input().split()))
# featured_articles = list(map(int, input().split()))
# target_value = int(input())
# final_feed = []

# while suggested_links and featured_articles:
#     link = suggested_links.popleft()
#     article = featured_articles.pop()

#     if article > link:
#         remainder = article % link
#         final_feed.append(remainder)

#         if remainder > 0:
#             featured_articles.append(remainder * 2)

#     elif link > article:
#         remainder = link % article
#         final_feed.append(-remainder)

#         if remainder > 0:
#             suggested_links.append(remainder * 2)

#     else:
#         final_feed.append(0)

# print(f'Final Feed: {", ".join(map(str, final_feed))}')
# total_engagement_value = sum(final_feed)

# if total_engagement_value >= target_value:
#     print(f'Goal achieved! Engagement Value: {total_engagement_value}')
# else:
#     short_by = target_value - total_engagement_value
#     print(f'Goal not achieved! Short by: {short_by}')
