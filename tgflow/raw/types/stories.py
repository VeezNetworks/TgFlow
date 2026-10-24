from ...tl import types as _tp


AllStoriesNotModified = getattr(_tp, 'StoriesAllStoriesNotModified', getattr(_tp, 'AllStoriesNotModified', None))
StoriesAllStoriesNotModified = getattr(_tp, 'StoriesAllStoriesNotModified', None)
AllStories = getattr(_tp, 'StoriesAllStories', getattr(_tp, 'AllStories', None))
StoriesAllStories = getattr(_tp, 'StoriesAllStories', None)
Stories = getattr(_tp, 'StoriesStories', getattr(_tp, 'Stories', None))
StoriesStories = getattr(_tp, 'StoriesStories', None)
StoryViewsList = getattr(_tp, 'StoriesStoryViewsList', getattr(_tp, 'StoryViewsList', None))
StoriesStoryViewsList = getattr(_tp, 'StoriesStoryViewsList', None)
StoryViews = getattr(_tp, 'StoriesStoryViews', getattr(_tp, 'StoryViews', None))
StoriesStoryViews = getattr(_tp, 'StoriesStoryViews', None)
PeerStories = getattr(_tp, 'StoriesPeerStories', getattr(_tp, 'PeerStories', None))
StoriesPeerStories = getattr(_tp, 'StoriesPeerStories', None)
StoryReactionsList = getattr(_tp, 'StoriesStoryReactionsList', getattr(_tp, 'StoryReactionsList', None))
StoriesStoryReactionsList = getattr(_tp, 'StoriesStoryReactionsList', None)
FoundStories = getattr(_tp, 'StoriesFoundStories', getattr(_tp, 'FoundStories', None))
StoriesFoundStories = getattr(_tp, 'StoriesFoundStories', None)
CanSendStoryCount = getattr(_tp, 'StoriesCanSendStoryCount', getattr(_tp, 'CanSendStoryCount', None))
StoriesCanSendStoryCount = getattr(_tp, 'StoriesCanSendStoryCount', None)
AlbumsNotModified = getattr(_tp, 'StoriesAlbumsNotModified', getattr(_tp, 'AlbumsNotModified', None))
StoriesAlbumsNotModified = getattr(_tp, 'StoriesAlbumsNotModified', None)
Albums = getattr(_tp, 'StoriesAlbums', getattr(_tp, 'Albums', None))
StoriesAlbums = getattr(_tp, 'StoriesAlbums', None)

__all__ = [
    "AllStoriesNotModified",
    "StoriesAllStoriesNotModified",
    "AllStories",
    "StoriesAllStories",
    "Stories",
    "StoriesStories",
    "StoryViewsList",
    "StoriesStoryViewsList",
    "StoryViews",
    "StoriesStoryViews",
    "PeerStories",
    "StoriesPeerStories",
    "StoryReactionsList",
    "StoriesStoryReactionsList",
    "FoundStories",
    "StoriesFoundStories",
    "CanSendStoryCount",
    "StoriesCanSendStoryCount",
    "AlbumsNotModified",
    "StoriesAlbumsNotModified",
    "Albums",
    "StoriesAlbums"
]
