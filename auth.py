def login(username, password):
    if not username or not password:
        return False

    if len(password) < 8:
        return False

    if username == "admin" and password == "admin123":
        return True

    return False


def logout():
    return "User logged out successfully"


def validate_password(password):
    if len(password) < 8:
        return "Password must contain at least 8 characters"

    return "Password length is valid"
