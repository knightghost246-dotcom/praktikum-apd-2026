import storage

def cek_login(username, password):
    for x in storage.USERS:
        if x[0] == username and x[1] == password:
            return x[2]
    return None

def username_terdaftar(username):
    for x in storage.USERS:
        if x[0] == username:
            return True
    return False

def registrasi_user(username, password):
    username = username.strip().lower()
    password = password.strip().lower()
    if username == "":
        raise ValueError("Username tidak boleh kosong")
    if password == "":
        raise ValueError("Password tidak boleh kosong")
    if username_terdaftar(username):
        raise ValueError("Username sudah dipakai, cari yang lain")
    
    storage.USERS.append([username, password, "user"])
    return username
