def login(username, password):

    if not username or not password:
        return "Fields cannot be empty"

    if len(password) < 4:
        return "Password too short"

    if username == "admin" and password == "1234":
        return "Login Successful"

    return "Invalid Credentials"
