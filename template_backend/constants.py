ALLOW_ORIGINS: list[str] = ["*"]
ALLOW_CREDENTIALS: bool = True
ALLOW_METHODS: list[str] = ["GET", "POST", "PUT", "DELETE", "OPTION"]
ALLOW_HEADERS: list[str] = [
    "Content-Type",
    "Set-Cookie",
    "Access-Control-Allow-Headers",
    "Access-Control-Allow-Origin",
    "Authorization",
]
