from django.contrib.sites.models import Site

from .models import Setting
from utils.get_setting import get_setting


def setting(requests):
    """ 自定义一些模板全局变量 """
    s = get_setting()
    site = Site.objects.get(id=1)
    return {
        'SITE_TITLE': s.title,
        'BAR_TITLE': s.bar_title,
        'BAR_DESC': s.bar_desc,
        'COMMENT_PAGE_COUNT': s.comment_page_count
    }
