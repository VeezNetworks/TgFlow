from ...tl import functions as _fn


CanSendStory = getattr(_fn, 'CanSendStory', getattr(_fn, 'StoriesCanSendStory', None))
StoriesCanSendStory = getattr(_fn, 'StoriesCanSendStory', None)
SendStory = getattr(_fn, 'SendStory', getattr(_fn, 'StoriesSendStory', None))
StoriesSendStory = getattr(_fn, 'StoriesSendStory', None)
EditStory = getattr(_fn, 'EditStory', getattr(_fn, 'StoriesEditStory', None))
StoriesEditStory = getattr(_fn, 'StoriesEditStory', None)
DeleteStories = getattr(_fn, 'DeleteStories', getattr(_fn, 'StoriesDeleteStories', None))
StoriesDeleteStories = getattr(_fn, 'StoriesDeleteStories', None)
TogglePinned = getattr(_fn, 'TogglePinned', getattr(_fn, 'StoriesTogglePinned', None))
StoriesTogglePinned = getattr(_fn, 'StoriesTogglePinned', None)
GetAllStories = getattr(_fn, 'GetAllStories', getattr(_fn, 'StoriesGetAllStories', None))
StoriesGetAllStories = getattr(_fn, 'StoriesGetAllStories', None)
GetPinnedStories = getattr(_fn, 'GetPinnedStories', getattr(_fn, 'StoriesGetPinnedStories', None))
StoriesGetPinnedStories = getattr(_fn, 'StoriesGetPinnedStories', None)
GetStoriesArchive = getattr(_fn, 'GetStoriesArchive', getattr(_fn, 'StoriesGetStoriesArchive', None))
StoriesGetStoriesArchive = getattr(_fn, 'StoriesGetStoriesArchive', None)
GetStoriesByID = getattr(_fn, 'GetStoriesByID', getattr(_fn, 'StoriesGetStoriesByID', None))
StoriesGetStoriesByID = getattr(_fn, 'StoriesGetStoriesByID', None)
ToggleAllStoriesHidden = getattr(_fn, 'ToggleAllStoriesHidden', getattr(_fn, 'StoriesToggleAllStoriesHidden', None))
StoriesToggleAllStoriesHidden = getattr(_fn, 'StoriesToggleAllStoriesHidden', None)
ReadStories = getattr(_fn, 'ReadStories', getattr(_fn, 'StoriesReadStories', None))
StoriesReadStories = getattr(_fn, 'StoriesReadStories', None)
IncrementStoryViews = getattr(_fn, 'IncrementStoryViews', getattr(_fn, 'StoriesIncrementStoryViews', None))
StoriesIncrementStoryViews = getattr(_fn, 'StoriesIncrementStoryViews', None)
GetStoryViewsList = getattr(_fn, 'GetStoryViewsList', getattr(_fn, 'StoriesGetStoryViewsList', None))
StoriesGetStoryViewsList = getattr(_fn, 'StoriesGetStoryViewsList', None)
GetStoriesViews = getattr(_fn, 'GetStoriesViews', getattr(_fn, 'StoriesGetStoriesViews', None))
StoriesGetStoriesViews = getattr(_fn, 'StoriesGetStoriesViews', None)
ExportStoryLink = getattr(_fn, 'ExportStoryLink', getattr(_fn, 'StoriesExportStoryLink', None))
StoriesExportStoryLink = getattr(_fn, 'StoriesExportStoryLink', None)
Report = getattr(_fn, 'Report', getattr(_fn, 'StoriesReport', None))
StoriesReport = getattr(_fn, 'StoriesReport', None)
ActivateStealthMode = getattr(_fn, 'ActivateStealthMode', getattr(_fn, 'StoriesActivateStealthMode', None))
StoriesActivateStealthMode = getattr(_fn, 'StoriesActivateStealthMode', None)
SendReaction = getattr(_fn, 'SendReaction', getattr(_fn, 'StoriesSendReaction', None))
StoriesSendReaction = getattr(_fn, 'StoriesSendReaction', None)
GetPeerStories = getattr(_fn, 'GetPeerStories', getattr(_fn, 'StoriesGetPeerStories', None))
StoriesGetPeerStories = getattr(_fn, 'StoriesGetPeerStories', None)
GetAllReadPeerStories = getattr(_fn, 'GetAllReadPeerStories', getattr(_fn, 'StoriesGetAllReadPeerStories', None))
StoriesGetAllReadPeerStories = getattr(_fn, 'StoriesGetAllReadPeerStories', None)
GetPeerMaxIDs = getattr(_fn, 'GetPeerMaxIDs', getattr(_fn, 'StoriesGetPeerMaxIDs', None))
StoriesGetPeerMaxIDs = getattr(_fn, 'StoriesGetPeerMaxIDs', None)
GetChatsToSend = getattr(_fn, 'GetChatsToSend', getattr(_fn, 'StoriesGetChatsToSend', None))
StoriesGetChatsToSend = getattr(_fn, 'StoriesGetChatsToSend', None)
TogglePeerStoriesHidden = getattr(_fn, 'TogglePeerStoriesHidden', getattr(_fn, 'StoriesTogglePeerStoriesHidden', None))
StoriesTogglePeerStoriesHidden = getattr(_fn, 'StoriesTogglePeerStoriesHidden', None)
GetStoryReactionsList = getattr(_fn, 'GetStoryReactionsList', getattr(_fn, 'StoriesGetStoryReactionsList', None))
StoriesGetStoryReactionsList = getattr(_fn, 'StoriesGetStoryReactionsList', None)
TogglePinnedToTop = getattr(_fn, 'TogglePinnedToTop', getattr(_fn, 'StoriesTogglePinnedToTop', None))
StoriesTogglePinnedToTop = getattr(_fn, 'StoriesTogglePinnedToTop', None)
SearchPosts = getattr(_fn, 'SearchPosts', getattr(_fn, 'StoriesSearchPosts', None))
StoriesSearchPosts = getattr(_fn, 'StoriesSearchPosts', None)
CreateAlbum = getattr(_fn, 'CreateAlbum', getattr(_fn, 'StoriesCreateAlbum', None))
StoriesCreateAlbum = getattr(_fn, 'StoriesCreateAlbum', None)
UpdateAlbum = getattr(_fn, 'UpdateAlbum', getattr(_fn, 'StoriesUpdateAlbum', None))
StoriesUpdateAlbum = getattr(_fn, 'StoriesUpdateAlbum', None)
ReorderAlbums = getattr(_fn, 'ReorderAlbums', getattr(_fn, 'StoriesReorderAlbums', None))
StoriesReorderAlbums = getattr(_fn, 'StoriesReorderAlbums', None)
DeleteAlbum = getattr(_fn, 'DeleteAlbum', getattr(_fn, 'StoriesDeleteAlbum', None))
StoriesDeleteAlbum = getattr(_fn, 'StoriesDeleteAlbum', None)
GetAlbums = getattr(_fn, 'GetAlbums', getattr(_fn, 'StoriesGetAlbums', None))
StoriesGetAlbums = getattr(_fn, 'StoriesGetAlbums', None)
GetAlbumStories = getattr(_fn, 'GetAlbumStories', getattr(_fn, 'StoriesGetAlbumStories', None))
StoriesGetAlbumStories = getattr(_fn, 'StoriesGetAlbumStories', None)
StartLive = getattr(_fn, 'StartLive', getattr(_fn, 'StoriesStartLive', None))
StoriesStartLive = getattr(_fn, 'StoriesStartLive', None)

__all__ = [
    "CanSendStory",
    "StoriesCanSendStory",
    "SendStory",
    "StoriesSendStory",
    "EditStory",
    "StoriesEditStory",
    "DeleteStories",
    "StoriesDeleteStories",
    "TogglePinned",
    "StoriesTogglePinned",
    "GetAllStories",
    "StoriesGetAllStories",
    "GetPinnedStories",
    "StoriesGetPinnedStories",
    "GetStoriesArchive",
    "StoriesGetStoriesArchive",
    "GetStoriesByID",
    "StoriesGetStoriesByID",
    "ToggleAllStoriesHidden",
    "StoriesToggleAllStoriesHidden",
    "ReadStories",
    "StoriesReadStories",
    "IncrementStoryViews",
    "StoriesIncrementStoryViews",
    "GetStoryViewsList",
    "StoriesGetStoryViewsList",
    "GetStoriesViews",
    "StoriesGetStoriesViews",
    "ExportStoryLink",
    "StoriesExportStoryLink",
    "Report",
    "StoriesReport",
    "ActivateStealthMode",
    "StoriesActivateStealthMode",
    "SendReaction",
    "StoriesSendReaction",
    "GetPeerStories",
    "StoriesGetPeerStories",
    "GetAllReadPeerStories",
    "StoriesGetAllReadPeerStories",
    "GetPeerMaxIDs",
    "StoriesGetPeerMaxIDs",
    "GetChatsToSend",
    "StoriesGetChatsToSend",
    "TogglePeerStoriesHidden",
    "StoriesTogglePeerStoriesHidden",
    "GetStoryReactionsList",
    "StoriesGetStoryReactionsList",
    "TogglePinnedToTop",
    "StoriesTogglePinnedToTop",
    "SearchPosts",
    "StoriesSearchPosts",
    "CreateAlbum",
    "StoriesCreateAlbum",
    "UpdateAlbum",
    "StoriesUpdateAlbum",
    "ReorderAlbums",
    "StoriesReorderAlbums",
    "DeleteAlbum",
    "StoriesDeleteAlbum",
    "GetAlbums",
    "StoriesGetAlbums",
    "GetAlbumStories",
    "StoriesGetAlbumStories",
    "StartLive",
    "StoriesStartLive"
]
