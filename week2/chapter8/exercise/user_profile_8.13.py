# 用户简介
def build_profile(first, last, **user_info):
    # 创建一个字典，包含用户的所有信息
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('Shi', 'Lei', sex='male', filed='software engineering', location='Xi`An')
print(user_profile)
