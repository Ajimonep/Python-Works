email_id="jeramiah@gmail.com"

at_index_pos=email_id.index("@")

username=email_id[:at_index_pos]

print(username)

domain=email_id[at_index_pos:]

print(domain)