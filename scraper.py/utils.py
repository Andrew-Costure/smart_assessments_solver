def cleanup_cookie(cookie: dict[str, str]):
    if (
        cookie["sameSite"] == "unspecified"
        or cookie["sameSite"] == "no_restriction"
    ):
        cookie["sameSite"] = "None"
    elif cookie["sameSite"] == "lax":
        cookie["sameSite"] = "Lax"
    elif cookie["sameSite"] == "strict":
        cookie["sameSite"] = "Strict"
    return cookie