from django.template.defaultfilters import stringfilter
from django import template
from django.utils.safestring import mark_safe
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from utils.mistune_markdown import text_markdown

register = template.Library()  # 名字是固定的register


@register.filter(is_safe=True)
@stringfilter
def comment_markdown(text):
    """ 给文章加上 markdown支持 和 代码高亮 """
    return mark_safe(text_markdown(text))


@register.simple_tag(takes_context=True)
def pagination_tag(context, object_list, page_count=2):
    """ context是Context 对象，object_list是你要分页的对象，page_count表示每页的数量 """
    paginator = Paginator(object_list, page_count)
    page = context['request'].GET.get('page')

    try:
        object_list = paginator.page(page)  # 根据页码获取对应页的数据

    except PageNotAnInteger:
        # 如果page不是int，字符串或为None，就返回第一页
        object_list = paginator.page(1)

    except EmptyPage:
        # 如果page是int, 负数，或0，或者超过最大页数，返回最后一页
        object_list = paginator.page(paginator.num_pages)

    # 模板里as可以取得return {% pagination_tag article_list 2 as article_list %}
    return object_list


from django.utils.timezone import now


@register.filter()
def time_filter(time):
    """ 自定义时间过滤器 """
    # timestamp为间隔时间, 这里需要注意 time和now有 是否包办时区之分的格式
    # 设置setting.USE_TZ为False 或者 去除时间里的 now=now.replace(tzinfo=None)
    timestamp = (now() - time).total_seconds()

    if timestamp < 60:
        return '%s 秒前' % timestamp
    elif (timestamp >= 60) and (timestamp < 60 * 60):
        minute = int(timestamp / 60)
        return '%s 分钟前' % minute
    elif (timestamp >= 60 * 60) and (timestamp < 60 * 60 * 24):
        hour = int(timestamp / 60 / 60)
        minute = int(timestamp % (60 * 60) / 60)
        return '%s 小时 %s 分钟前' % (hour, minute)
    elif (timestamp >= 60 * 60 * 24) and (timestamp < 60 * 60 * 24 * 30):
        day = int(timestamp / 60 / 60 / 24)
        return '%s 天前' % day
    else:
        return time.strftime('%Y/%m/%d %H:%M')
