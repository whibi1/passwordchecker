def password_check(password):
    
    min_length = 8
    
   
    if len(password) < min_length:
        return "Password must be at least 8 characters long"
    
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    if not has_upper:
        return "Password must contain at least one uppercase letter"
    if not has_lower:
        return "Password must contain at least one lowercase letter"
    
    
    has_digit = any(c.isdigit() for c in password)
    if not has_digit:
        return "Password must contain at least one digit"
    
   
    special_chars = list("!@#$%^&*(),.?\":{}|<>")
    has_special = any(c in special_chars for c in password)
    if not has_special:
        return "Password must contain at least one special character: !@#$%^&*(),.?\":{}|<>"
    
   
    return "Password is valid"

password = input("Enter your password: ")
while True:
    check = password_check(password)
    if check == "Password is valid":
        print(check)
        break
    else:
        print(check)
        password = input("Enter your password: ")
