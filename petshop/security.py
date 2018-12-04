from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager

import credenciais

passw = credenciais.mypass
hpass = generate_password_hash(passw)

check = check_password_hash(hpass, credenciais.mypass)
