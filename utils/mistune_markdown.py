import mistune
from pygments.util import ClassNotFound
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.lexers.python import Python3Lexer
from pygments.formatters import html


# The fastest markdown parser in pure Python with renderer features, inspired by marked.
# https://github.com/lepture/mistune

class CommentRenderer(mistune.Renderer):
    """ 对评论进行 markdown显示，和 代码高亮 """

    def block_code(self, code, lang=None):
        """Rendering block level code. ``pre > code``.

        :param code: text content of the code block.
        :param lang: language of the given code.
        """
        code = code.rstrip('\n')  # 去掉尾部的换行符
        return '<pre><code>%s\n</code></pre>\n' % code




def text_markdown(text):
    """ 对传入的text文本进行markdown """
    renderer = CommentRenderer()
    markdown = mistune.Markdown(renderer=renderer)
    return markdown(text)
