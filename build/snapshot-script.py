import json
from collections import Counter

username = input("Please enter your Facebook username: ").lower().replace(" ", "")
while input("Is this file name correct? facebook-{} (y/n): ".format(username)) != 'y':
    username = input("Please enter your Facebook username: ").lower().replace(" ", "")

print("~Facebook by YOUR numbers.~\n\n-----")
#About you
with open("./facebook-{}/about_you/face_recognition.json".format(username), "r") as read_file:
    face_recognition = json.load(read_file)
print("ABOUT YOU\n-----\n\n• Facebook has used {} pictures to learn to recognize your face.".format(face_recognition['facial_data']['example_count']))

with open("./facebook-{}/about_you/friend_peer_group.json".format(username), "r") as read_file:
    friend_peer_group = json.load(read_file)
print("\n• According to Facebook, you are in the {} 'Friend Peer Group.'".format(friend_peer_group['friend_peer_group']))

with open("./facebook-{}/about_you/your_address_books.json".format(username), "r") as read_file:
    address_books = json.load(read_file)
print(" and have {} of those peers' contact info stored on FB.".format(len(address_books['address_book']['address_book'])))

#Ads
with open("./facebook-{}/ads/ads_interests.json".format(username), "r") as read_file:
    ads_interests = json.load(read_file)
ad_topics = ads_interests['topics']
print("\n-----\nADS\n-----\n\n• Zuck THINKS you're interested in these {} different ad topics: \n\n {}".format(len(ad_topics), ad_topics))

with open("./facebook-{}/ads/advertisers_who_uploaded_a_contact_list_with_your_information.json".format(username), "r") as read_file:
    advertisers_with_info = json.load(read_file)['custom_audiences']
print("\n• But he KNOWS these {} advertisers all have your information: \n\n {}".format(len(advertisers_with_info), advertisers_with_info))
print("\n...hopefully they're using it responsibly...")

with open("./facebook-{}/ads/advertisers_you've_interacted_with.json".format(username), "r") as read_file:
    advertisers_interacted_with = json.load(read_file)
ads_clicked_on = [advertisement['title'] for advertisement in advertisers_interacted_with['history']]
print("\n• Andddd you've clicked on these {} advertisements: \n\n {}".format(len(ads_clicked_on), ads_clicked_on))

#Apps
with open("./facebook-{}/apps/installed_apps.json".format(username), "r") as read_file:
    installed_apps = json.load(read_file)
app_names = [application['name'] for application in installed_apps['installed_apps']]
print("\n-----\nAPPS\n-----\n\nHere's all of the apps you've installed / authorized with FB: \n\n {}".format(app_names))

with open("./facebook-{}/apps/posts_from_apps.json".format(username), "r") as read_file:
    posts_from_apps = json.load(read_file)
source_of_post = []
try:
    for post in posts_from_apps['app_posts']:
        try:
            for attachment in post['attachments']:
                try:
                    for data in attachment['data']:
                        try:
                            source_of_post.append(data['external_context']['source'])
                        except KeyError:
                            source_of_post.append("No info")
                except KeyError:
                    source_of_post.append("No info")
        except KeyError:
            source_of_post.append("No info")
except KeyError:
    source_of_post.append("No info")
for item in Counter(source_of_post).most_common(1):
    print("• Out of all of those apps,",item[0],"has posted the most on your behalf:", item[1],"times to be exact.")
