import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "25042879"))
    API_HASH = os.environ.get("API_HASH", "f30c2c781475f28958d121a57a8acc52")
    BOT_TOKEN = os.environ.get("5987770744:AAGg6QYvaCbA5Xwjk_coLIU3XKIiLo2bE4Q", "")
    STRING_SESSION = os.environ.get("BQBMRPvukgQBeOav4_A2h4phM6gMgiuGG4Zz2lEG9zXTCR2zEBkjhzsXoQPodlBrBxq78OXps8E5qcqDb1BsjgisLiCDykmFlomkEdWqCzQlfpxtORcqzGdpW1SSl-8K-atOakARQlE3hbdNL-c5SmOv1Q2H_T5KzsGbusy3lkNtLruvhEIftVvHyNC2DN5jtA62RN8nRTPV7rqDdtDGCPd59FPuhCjNodLIKaqeEhmCjkqaRlMZdq9oa4m6QiVH6F114Zc5ghhWV2nhxWdUfqAmr-8lQb-reBjIewHD5yuvRrkFrtJgNPN1PrekQLIovZLr21RTcBcWmkDIm6nfv5JwAAAAAVp4R4UA", "")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("@DjBabaMusicBot", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("5812799365", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
