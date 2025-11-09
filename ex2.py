def email_addresses(first, last,domain="@exeter.ac.uk"):
    email = []
    for i in range(len(first)):
        email.append(first[i][0].casefold()+"."+last[i].casefold()+domain)
    return email
    
