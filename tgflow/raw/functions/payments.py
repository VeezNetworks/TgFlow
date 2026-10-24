from ...tl import functions as _fn


GetPaymentForm = getattr(_fn, 'GetPaymentForm', getattr(_fn, 'PaymentsGetPaymentForm', None))
PaymentsGetPaymentForm = getattr(_fn, 'PaymentsGetPaymentForm', None)
GetPaymentReceipt = getattr(_fn, 'GetPaymentReceipt', getattr(_fn, 'PaymentsGetPaymentReceipt', None))
PaymentsGetPaymentReceipt = getattr(_fn, 'PaymentsGetPaymentReceipt', None)
ValidateRequestedInfo = getattr(_fn, 'ValidateRequestedInfo', getattr(_fn, 'PaymentsValidateRequestedInfo', None))
PaymentsValidateRequestedInfo = getattr(_fn, 'PaymentsValidateRequestedInfo', None)
SendPaymentForm = getattr(_fn, 'SendPaymentForm', getattr(_fn, 'PaymentsSendPaymentForm', None))
PaymentsSendPaymentForm = getattr(_fn, 'PaymentsSendPaymentForm', None)
GetSavedInfo = getattr(_fn, 'GetSavedInfo', getattr(_fn, 'PaymentsGetSavedInfo', None))
PaymentsGetSavedInfo = getattr(_fn, 'PaymentsGetSavedInfo', None)
ClearSavedInfo = getattr(_fn, 'ClearSavedInfo', getattr(_fn, 'PaymentsClearSavedInfo', None))
PaymentsClearSavedInfo = getattr(_fn, 'PaymentsClearSavedInfo', None)
GetBankCardData = getattr(_fn, 'GetBankCardData', getattr(_fn, 'PaymentsGetBankCardData', None))
PaymentsGetBankCardData = getattr(_fn, 'PaymentsGetBankCardData', None)
ExportInvoice = getattr(_fn, 'ExportInvoice', getattr(_fn, 'PaymentsExportInvoice', None))
PaymentsExportInvoice = getattr(_fn, 'PaymentsExportInvoice', None)
AssignAppStoreTransaction = getattr(_fn, 'AssignAppStoreTransaction', getattr(_fn, 'PaymentsAssignAppStoreTransaction', None))
PaymentsAssignAppStoreTransaction = getattr(_fn, 'PaymentsAssignAppStoreTransaction', None)
AssignPlayMarketTransaction = getattr(_fn, 'AssignPlayMarketTransaction', getattr(_fn, 'PaymentsAssignPlayMarketTransaction', None))
PaymentsAssignPlayMarketTransaction = getattr(_fn, 'PaymentsAssignPlayMarketTransaction', None)
GetPremiumGiftCodeOptions = getattr(_fn, 'GetPremiumGiftCodeOptions', getattr(_fn, 'PaymentsGetPremiumGiftCodeOptions', None))
PaymentsGetPremiumGiftCodeOptions = getattr(_fn, 'PaymentsGetPremiumGiftCodeOptions', None)
CheckGiftCode = getattr(_fn, 'CheckGiftCode', getattr(_fn, 'PaymentsCheckGiftCode', None))
PaymentsCheckGiftCode = getattr(_fn, 'PaymentsCheckGiftCode', None)
ApplyGiftCode = getattr(_fn, 'ApplyGiftCode', getattr(_fn, 'PaymentsApplyGiftCode', None))
PaymentsApplyGiftCode = getattr(_fn, 'PaymentsApplyGiftCode', None)
GetGiveawayInfo = getattr(_fn, 'GetGiveawayInfo', getattr(_fn, 'PaymentsGetGiveawayInfo', None))
PaymentsGetGiveawayInfo = getattr(_fn, 'PaymentsGetGiveawayInfo', None)
LaunchPrepaidGiveaway = getattr(_fn, 'LaunchPrepaidGiveaway', getattr(_fn, 'PaymentsLaunchPrepaidGiveaway', None))
PaymentsLaunchPrepaidGiveaway = getattr(_fn, 'PaymentsLaunchPrepaidGiveaway', None)
GetStarsTopupOptions = getattr(_fn, 'GetStarsTopupOptions', getattr(_fn, 'PaymentsGetStarsTopupOptions', None))
PaymentsGetStarsTopupOptions = getattr(_fn, 'PaymentsGetStarsTopupOptions', None)
GetStarsStatus = getattr(_fn, 'GetStarsStatus', getattr(_fn, 'PaymentsGetStarsStatus', None))
PaymentsGetStarsStatus = getattr(_fn, 'PaymentsGetStarsStatus', None)
GetStarsTransactions = getattr(_fn, 'GetStarsTransactions', getattr(_fn, 'PaymentsGetStarsTransactions', None))
PaymentsGetStarsTransactions = getattr(_fn, 'PaymentsGetStarsTransactions', None)
SendStarsForm = getattr(_fn, 'SendStarsForm', getattr(_fn, 'PaymentsSendStarsForm', None))
PaymentsSendStarsForm = getattr(_fn, 'PaymentsSendStarsForm', None)
RefundStarsCharge = getattr(_fn, 'RefundStarsCharge', getattr(_fn, 'PaymentsRefundStarsCharge', None))
PaymentsRefundStarsCharge = getattr(_fn, 'PaymentsRefundStarsCharge', None)
GetStarsRevenueStats = getattr(_fn, 'GetStarsRevenueStats', getattr(_fn, 'PaymentsGetStarsRevenueStats', None))
PaymentsGetStarsRevenueStats = getattr(_fn, 'PaymentsGetStarsRevenueStats', None)
GetStarsRevenueWithdrawalUrl = getattr(_fn, 'GetStarsRevenueWithdrawalUrl', getattr(_fn, 'PaymentsGetStarsRevenueWithdrawalUrl', None))
PaymentsGetStarsRevenueWithdrawalUrl = getattr(_fn, 'PaymentsGetStarsRevenueWithdrawalUrl', None)
GetStarsRevenueAdsAccountUrl = getattr(_fn, 'GetStarsRevenueAdsAccountUrl', getattr(_fn, 'PaymentsGetStarsRevenueAdsAccountUrl', None))
PaymentsGetStarsRevenueAdsAccountUrl = getattr(_fn, 'PaymentsGetStarsRevenueAdsAccountUrl', None)
GetStarsTransactionsByID = getattr(_fn, 'GetStarsTransactionsByID', getattr(_fn, 'PaymentsGetStarsTransactionsByID', None))
PaymentsGetStarsTransactionsByID = getattr(_fn, 'PaymentsGetStarsTransactionsByID', None)
GetStarsGiftOptions = getattr(_fn, 'GetStarsGiftOptions', getattr(_fn, 'PaymentsGetStarsGiftOptions', None))
PaymentsGetStarsGiftOptions = getattr(_fn, 'PaymentsGetStarsGiftOptions', None)
GetStarsSubscriptions = getattr(_fn, 'GetStarsSubscriptions', getattr(_fn, 'PaymentsGetStarsSubscriptions', None))
PaymentsGetStarsSubscriptions = getattr(_fn, 'PaymentsGetStarsSubscriptions', None)
ChangeStarsSubscription = getattr(_fn, 'ChangeStarsSubscription', getattr(_fn, 'PaymentsChangeStarsSubscription', None))
PaymentsChangeStarsSubscription = getattr(_fn, 'PaymentsChangeStarsSubscription', None)
FulfillStarsSubscription = getattr(_fn, 'FulfillStarsSubscription', getattr(_fn, 'PaymentsFulfillStarsSubscription', None))
PaymentsFulfillStarsSubscription = getattr(_fn, 'PaymentsFulfillStarsSubscription', None)
GetStarsGiveawayOptions = getattr(_fn, 'GetStarsGiveawayOptions', getattr(_fn, 'PaymentsGetStarsGiveawayOptions', None))
PaymentsGetStarsGiveawayOptions = getattr(_fn, 'PaymentsGetStarsGiveawayOptions', None)
GetStarGifts = getattr(_fn, 'GetStarGifts', getattr(_fn, 'PaymentsGetStarGifts', None))
PaymentsGetStarGifts = getattr(_fn, 'PaymentsGetStarGifts', None)
SaveStarGift = getattr(_fn, 'SaveStarGift', getattr(_fn, 'PaymentsSaveStarGift', None))
PaymentsSaveStarGift = getattr(_fn, 'PaymentsSaveStarGift', None)
ConvertStarGift = getattr(_fn, 'ConvertStarGift', getattr(_fn, 'PaymentsConvertStarGift', None))
PaymentsConvertStarGift = getattr(_fn, 'PaymentsConvertStarGift', None)
BotCancelStarsSubscription = getattr(_fn, 'BotCancelStarsSubscription', getattr(_fn, 'PaymentsBotCancelStarsSubscription', None))
PaymentsBotCancelStarsSubscription = getattr(_fn, 'PaymentsBotCancelStarsSubscription', None)
GetConnectedStarRefBots = getattr(_fn, 'GetConnectedStarRefBots', getattr(_fn, 'PaymentsGetConnectedStarRefBots', None))
PaymentsGetConnectedStarRefBots = getattr(_fn, 'PaymentsGetConnectedStarRefBots', None)
GetConnectedStarRefBot = getattr(_fn, 'GetConnectedStarRefBot', getattr(_fn, 'PaymentsGetConnectedStarRefBot', None))
PaymentsGetConnectedStarRefBot = getattr(_fn, 'PaymentsGetConnectedStarRefBot', None)
GetSuggestedStarRefBots = getattr(_fn, 'GetSuggestedStarRefBots', getattr(_fn, 'PaymentsGetSuggestedStarRefBots', None))
PaymentsGetSuggestedStarRefBots = getattr(_fn, 'PaymentsGetSuggestedStarRefBots', None)
ConnectStarRefBot = getattr(_fn, 'ConnectStarRefBot', getattr(_fn, 'PaymentsConnectStarRefBot', None))
PaymentsConnectStarRefBot = getattr(_fn, 'PaymentsConnectStarRefBot', None)
EditConnectedStarRefBot = getattr(_fn, 'EditConnectedStarRefBot', getattr(_fn, 'PaymentsEditConnectedStarRefBot', None))
PaymentsEditConnectedStarRefBot = getattr(_fn, 'PaymentsEditConnectedStarRefBot', None)
GetStarGiftUpgradePreview = getattr(_fn, 'GetStarGiftUpgradePreview', getattr(_fn, 'PaymentsGetStarGiftUpgradePreview', None))
PaymentsGetStarGiftUpgradePreview = getattr(_fn, 'PaymentsGetStarGiftUpgradePreview', None)
UpgradeStarGift = getattr(_fn, 'UpgradeStarGift', getattr(_fn, 'PaymentsUpgradeStarGift', None))
PaymentsUpgradeStarGift = getattr(_fn, 'PaymentsUpgradeStarGift', None)
TransferStarGift = getattr(_fn, 'TransferStarGift', getattr(_fn, 'PaymentsTransferStarGift', None))
PaymentsTransferStarGift = getattr(_fn, 'PaymentsTransferStarGift', None)
GetUniqueStarGift = getattr(_fn, 'GetUniqueStarGift', getattr(_fn, 'PaymentsGetUniqueStarGift', None))
PaymentsGetUniqueStarGift = getattr(_fn, 'PaymentsGetUniqueStarGift', None)
GetSavedStarGifts = getattr(_fn, 'GetSavedStarGifts', getattr(_fn, 'PaymentsGetSavedStarGifts', None))
PaymentsGetSavedStarGifts = getattr(_fn, 'PaymentsGetSavedStarGifts', None)
GetSavedStarGift = getattr(_fn, 'GetSavedStarGift', getattr(_fn, 'PaymentsGetSavedStarGift', None))
PaymentsGetSavedStarGift = getattr(_fn, 'PaymentsGetSavedStarGift', None)
GetStarGiftWithdrawalUrl = getattr(_fn, 'GetStarGiftWithdrawalUrl', getattr(_fn, 'PaymentsGetStarGiftWithdrawalUrl', None))
PaymentsGetStarGiftWithdrawalUrl = getattr(_fn, 'PaymentsGetStarGiftWithdrawalUrl', None)
ToggleChatStarGiftNotifications = getattr(_fn, 'ToggleChatStarGiftNotifications', getattr(_fn, 'PaymentsToggleChatStarGiftNotifications', None))
PaymentsToggleChatStarGiftNotifications = getattr(_fn, 'PaymentsToggleChatStarGiftNotifications', None)
ToggleStarGiftsPinnedToTop = getattr(_fn, 'ToggleStarGiftsPinnedToTop', getattr(_fn, 'PaymentsToggleStarGiftsPinnedToTop', None))
PaymentsToggleStarGiftsPinnedToTop = getattr(_fn, 'PaymentsToggleStarGiftsPinnedToTop', None)
CanPurchaseStore = getattr(_fn, 'CanPurchaseStore', getattr(_fn, 'PaymentsCanPurchaseStore', None))
PaymentsCanPurchaseStore = getattr(_fn, 'PaymentsCanPurchaseStore', None)
GetResaleStarGifts = getattr(_fn, 'GetResaleStarGifts', getattr(_fn, 'PaymentsGetResaleStarGifts', None))
PaymentsGetResaleStarGifts = getattr(_fn, 'PaymentsGetResaleStarGifts', None)
UpdateStarGiftPrice = getattr(_fn, 'UpdateStarGiftPrice', getattr(_fn, 'PaymentsUpdateStarGiftPrice', None))
PaymentsUpdateStarGiftPrice = getattr(_fn, 'PaymentsUpdateStarGiftPrice', None)
CreateStarGiftCollection = getattr(_fn, 'CreateStarGiftCollection', getattr(_fn, 'PaymentsCreateStarGiftCollection', None))
PaymentsCreateStarGiftCollection = getattr(_fn, 'PaymentsCreateStarGiftCollection', None)
UpdateStarGiftCollection = getattr(_fn, 'UpdateStarGiftCollection', getattr(_fn, 'PaymentsUpdateStarGiftCollection', None))
PaymentsUpdateStarGiftCollection = getattr(_fn, 'PaymentsUpdateStarGiftCollection', None)
ReorderStarGiftCollections = getattr(_fn, 'ReorderStarGiftCollections', getattr(_fn, 'PaymentsReorderStarGiftCollections', None))
PaymentsReorderStarGiftCollections = getattr(_fn, 'PaymentsReorderStarGiftCollections', None)
DeleteStarGiftCollection = getattr(_fn, 'DeleteStarGiftCollection', getattr(_fn, 'PaymentsDeleteStarGiftCollection', None))
PaymentsDeleteStarGiftCollection = getattr(_fn, 'PaymentsDeleteStarGiftCollection', None)
GetStarGiftCollections = getattr(_fn, 'GetStarGiftCollections', getattr(_fn, 'PaymentsGetStarGiftCollections', None))
PaymentsGetStarGiftCollections = getattr(_fn, 'PaymentsGetStarGiftCollections', None)
GetUniqueStarGiftValueInfo = getattr(_fn, 'GetUniqueStarGiftValueInfo', getattr(_fn, 'PaymentsGetUniqueStarGiftValueInfo', None))
PaymentsGetUniqueStarGiftValueInfo = getattr(_fn, 'PaymentsGetUniqueStarGiftValueInfo', None)
CheckCanSendGift = getattr(_fn, 'CheckCanSendGift', getattr(_fn, 'PaymentsCheckCanSendGift', None))
PaymentsCheckCanSendGift = getattr(_fn, 'PaymentsCheckCanSendGift', None)
GetStarGiftAuctionState = getattr(_fn, 'GetStarGiftAuctionState', getattr(_fn, 'PaymentsGetStarGiftAuctionState', None))
PaymentsGetStarGiftAuctionState = getattr(_fn, 'PaymentsGetStarGiftAuctionState', None)
GetStarGiftAuctionAcquiredGifts = getattr(_fn, 'GetStarGiftAuctionAcquiredGifts', getattr(_fn, 'PaymentsGetStarGiftAuctionAcquiredGifts', None))
PaymentsGetStarGiftAuctionAcquiredGifts = getattr(_fn, 'PaymentsGetStarGiftAuctionAcquiredGifts', None)
GetStarGiftActiveAuctions = getattr(_fn, 'GetStarGiftActiveAuctions', getattr(_fn, 'PaymentsGetStarGiftActiveAuctions', None))
PaymentsGetStarGiftActiveAuctions = getattr(_fn, 'PaymentsGetStarGiftActiveAuctions', None)
ResolveStarGiftOffer = getattr(_fn, 'ResolveStarGiftOffer', getattr(_fn, 'PaymentsResolveStarGiftOffer', None))
PaymentsResolveStarGiftOffer = getattr(_fn, 'PaymentsResolveStarGiftOffer', None)
SendStarGiftOffer = getattr(_fn, 'SendStarGiftOffer', getattr(_fn, 'PaymentsSendStarGiftOffer', None))
PaymentsSendStarGiftOffer = getattr(_fn, 'PaymentsSendStarGiftOffer', None)
GetStarGiftUpgradeAttributes = getattr(_fn, 'GetStarGiftUpgradeAttributes', getattr(_fn, 'PaymentsGetStarGiftUpgradeAttributes', None))
PaymentsGetStarGiftUpgradeAttributes = getattr(_fn, 'PaymentsGetStarGiftUpgradeAttributes', None)
GetCraftStarGifts = getattr(_fn, 'GetCraftStarGifts', getattr(_fn, 'PaymentsGetCraftStarGifts', None))
PaymentsGetCraftStarGifts = getattr(_fn, 'PaymentsGetCraftStarGifts', None)
CraftStarGift = getattr(_fn, 'CraftStarGift', getattr(_fn, 'PaymentsCraftStarGift', None))
PaymentsCraftStarGift = getattr(_fn, 'PaymentsCraftStarGift', None)

__all__ = [
    "GetPaymentForm",
    "PaymentsGetPaymentForm",
    "GetPaymentReceipt",
    "PaymentsGetPaymentReceipt",
    "ValidateRequestedInfo",
    "PaymentsValidateRequestedInfo",
    "SendPaymentForm",
    "PaymentsSendPaymentForm",
    "GetSavedInfo",
    "PaymentsGetSavedInfo",
    "ClearSavedInfo",
    "PaymentsClearSavedInfo",
    "GetBankCardData",
    "PaymentsGetBankCardData",
    "ExportInvoice",
    "PaymentsExportInvoice",
    "AssignAppStoreTransaction",
    "PaymentsAssignAppStoreTransaction",
    "AssignPlayMarketTransaction",
    "PaymentsAssignPlayMarketTransaction",
    "GetPremiumGiftCodeOptions",
    "PaymentsGetPremiumGiftCodeOptions",
    "CheckGiftCode",
    "PaymentsCheckGiftCode",
    "ApplyGiftCode",
    "PaymentsApplyGiftCode",
    "GetGiveawayInfo",
    "PaymentsGetGiveawayInfo",
    "LaunchPrepaidGiveaway",
    "PaymentsLaunchPrepaidGiveaway",
    "GetStarsTopupOptions",
    "PaymentsGetStarsTopupOptions",
    "GetStarsStatus",
    "PaymentsGetStarsStatus",
    "GetStarsTransactions",
    "PaymentsGetStarsTransactions",
    "SendStarsForm",
    "PaymentsSendStarsForm",
    "RefundStarsCharge",
    "PaymentsRefundStarsCharge",
    "GetStarsRevenueStats",
    "PaymentsGetStarsRevenueStats",
    "GetStarsRevenueWithdrawalUrl",
    "PaymentsGetStarsRevenueWithdrawalUrl",
    "GetStarsRevenueAdsAccountUrl",
    "PaymentsGetStarsRevenueAdsAccountUrl",
    "GetStarsTransactionsByID",
    "PaymentsGetStarsTransactionsByID",
    "GetStarsGiftOptions",
    "PaymentsGetStarsGiftOptions",
    "GetStarsSubscriptions",
    "PaymentsGetStarsSubscriptions",
    "ChangeStarsSubscription",
    "PaymentsChangeStarsSubscription",
    "FulfillStarsSubscription",
    "PaymentsFulfillStarsSubscription",
    "GetStarsGiveawayOptions",
    "PaymentsGetStarsGiveawayOptions",
    "GetStarGifts",
    "PaymentsGetStarGifts",
    "SaveStarGift",
    "PaymentsSaveStarGift",
    "ConvertStarGift",
    "PaymentsConvertStarGift",
    "BotCancelStarsSubscription",
    "PaymentsBotCancelStarsSubscription",
    "GetConnectedStarRefBots",
    "PaymentsGetConnectedStarRefBots",
    "GetConnectedStarRefBot",
    "PaymentsGetConnectedStarRefBot",
    "GetSuggestedStarRefBots",
    "PaymentsGetSuggestedStarRefBots",
    "ConnectStarRefBot",
    "PaymentsConnectStarRefBot",
    "EditConnectedStarRefBot",
    "PaymentsEditConnectedStarRefBot",
    "GetStarGiftUpgradePreview",
    "PaymentsGetStarGiftUpgradePreview",
    "UpgradeStarGift",
    "PaymentsUpgradeStarGift",
    "TransferStarGift",
    "PaymentsTransferStarGift",
    "GetUniqueStarGift",
    "PaymentsGetUniqueStarGift",
    "GetSavedStarGifts",
    "PaymentsGetSavedStarGifts",
    "GetSavedStarGift",
    "PaymentsGetSavedStarGift",
    "GetStarGiftWithdrawalUrl",
    "PaymentsGetStarGiftWithdrawalUrl",
    "ToggleChatStarGiftNotifications",
    "PaymentsToggleChatStarGiftNotifications",
    "ToggleStarGiftsPinnedToTop",
    "PaymentsToggleStarGiftsPinnedToTop",
    "CanPurchaseStore",
    "PaymentsCanPurchaseStore",
    "GetResaleStarGifts",
    "PaymentsGetResaleStarGifts",
    "UpdateStarGiftPrice",
    "PaymentsUpdateStarGiftPrice",
    "CreateStarGiftCollection",
    "PaymentsCreateStarGiftCollection",
    "UpdateStarGiftCollection",
    "PaymentsUpdateStarGiftCollection",
    "ReorderStarGiftCollections",
    "PaymentsReorderStarGiftCollections",
    "DeleteStarGiftCollection",
    "PaymentsDeleteStarGiftCollection",
    "GetStarGiftCollections",
    "PaymentsGetStarGiftCollections",
    "GetUniqueStarGiftValueInfo",
    "PaymentsGetUniqueStarGiftValueInfo",
    "CheckCanSendGift",
    "PaymentsCheckCanSendGift",
    "GetStarGiftAuctionState",
    "PaymentsGetStarGiftAuctionState",
    "GetStarGiftAuctionAcquiredGifts",
    "PaymentsGetStarGiftAuctionAcquiredGifts",
    "GetStarGiftActiveAuctions",
    "PaymentsGetStarGiftActiveAuctions",
    "ResolveStarGiftOffer",
    "PaymentsResolveStarGiftOffer",
    "SendStarGiftOffer",
    "PaymentsSendStarGiftOffer",
    "GetStarGiftUpgradeAttributes",
    "PaymentsGetStarGiftUpgradeAttributes",
    "GetCraftStarGifts",
    "PaymentsGetCraftStarGifts",
    "CraftStarGift",
    "PaymentsCraftStarGift"
]
