from user.models import Setting


def get_setting():
    """ 返回一个setting实例 """
    if Setting.objects.count():
        return Setting.objects.first()
    else:
        s = Setting()
        s.title = 'V2EX'
        s.bar_title = '麦芽 = 麦 + 芽'
        s.bar_desc = '是一个关于爬虫分享和探索的地方'
        s.save()
        return s
