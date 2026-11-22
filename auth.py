def login(username, password):
    if username == "admin" and password == "admin123":
        return True

    return False


def logout():
    return "User logged out successfully"
