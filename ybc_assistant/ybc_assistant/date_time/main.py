from datetime import datetime

# 获取今天：年-月-日
def get_date(s='-'):
    # 获取当前时间对象
    t = datetime.now()
    # 转换时间格式为字符串
    t = t.strftime('%Y{}%m{}%d'.format(s, s))
    # 返回时间
    return t

# 获取时间：时：分：秒
def get_time(s=':'):
    # 获取当前时间对象
    t = datetime.now()
    # 转换时间格式为字符串
    t = t.strftime('%H{}%M{}%S'.format(s, s))
    # 返回时间
    return t

# 获取年月日时分秒
def get_datetime(s=' '):
    res = get_date() + '{}' + get_time()
    return res.format(s)








