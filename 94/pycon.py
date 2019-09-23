from collections import namedtuple
import os
import pickle
import urllib.request

# prework
# download pickle file and store it in a tmp file
pkl_file = "pycon_videos.pkl"
data = "http://projects.bobbelderbos.com/pcc/{}".format(pkl_file)
pycon_videos = os.path.join("/tmp", pkl_file)
urllib.request.urlretrieve(data, pycon_videos)

# the pkl contains a list of Video namedtuples
Video = namedtuple("Video", "id title duration metrics")


def load_pycon_data(pycon_videos=pycon_videos):
    """Load the pickle file (pycon_videos) and return the data structure
       it holds"""
    pickle_in = open(pycon_videos, "rb")
    videos = pickle.load(pickle_in)
    pickle_in.close()
    return videos


def get_most_popular_talks_by_views(videos):
    """Return the pycon video list sorted by viewCount"""
    return sorted(
        videos, key=lambda Video: int(Video.metrics["viewCount"]), reverse=True
    )


def _calculate_popularity_ratio(video):
    view_count = float(video.metrics["viewCount"])
    like_count = float(video.metrics["likeCount"])
    dislike_count = float(video.metrics["dislikeCount"])
    return (like_count - dislike_count) / view_count


def get_most_popular_talks_by_like_ratio(videos):
    """Return the pycon video list sorted by most likes relative to
       number of views, so 10 likes on 175 views ranks higher than
       12 likes on 300 views. Discount the dislikeCount from the likeCount.
       Return the filtered list"""
    return sorted(
        videos, key=lambda Video: _calculate_popularity_ratio(Video), reverse=True
    )


def get_talks_gt_one_hour(videos):
    """Filter the videos list down to videos of > 1 hour"""
    pass


def get_talks_lt_twentyfour_min(videos):
    """Filter videos list down to videos that have a duration of less than
       24 minutes"""
    pass
