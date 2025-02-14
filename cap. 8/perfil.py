def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('miguel', 'dos santos', location='teresopolis', 
                             field='computer science', age='19')

print(user_profile)
