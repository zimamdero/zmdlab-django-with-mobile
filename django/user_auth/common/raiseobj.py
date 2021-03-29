def email_not_validate():
    return {"info": {
        "detail": "Email not validated.",
        "code": "email_not_validate"
    }}


def password_fields_not_match():
    return {"info": {
        "detail": "Password fields didn't match.",
        "code": "password_fields_not_match"
    }}


def password_not_validate():
    return {"info": {
        "detail": "Password not validated.",
        "code": "password_not_validate"
    }}


def old_password_not_correct():
    return {"info": {
        "detail": "Old password is not correct.",
        "code": "old_password_not_correct"
    }}


def authorize_fail():
    return {"info": {
        "detail": "You don't have permission for this user.",
        "code": "authorize_fail"
    }}


def email_already_use():
    return {"info": {
        "detail": "This email is already in use.",
        "code": "email_already_use"
    }}


def username_already_use():
    return {"info": {
        "detail": "This username is already in use.",
        "code": "username_already_use"
    }}


def uemail_auth_num_incorrect():
    return {"info": {
        "detail": "This email auth number is incorrect.",
        "code": "uemail_auth_num_incorrect"
    }}


def uemail_auth_num_time_over():
    return {"info": {
        "detail": "This email auth number is time over. Retry request auth number",
        "code": "uemail_auth_num_time_over"
    }}


def uemail_auth_num_check_not_complete():
    return {"info": {
        "detail": "This email auth number check not completed. try request auth number",
        "code": "uemail_auth_num_check_not_complete"
    }}


def uemail_has_not_email():
    return {"info": {
        "detail": "need to request email auth number.",
        "code": "uemail_has_not_email"
    }}


def success():
    return {"info": {
        "code": "success"
    }}