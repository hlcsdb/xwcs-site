from wagtail import hooks
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup

@hooks.register("register_icons")
def register_icons(icons):
    return icons + [
        "wagtailadmin/icons/media.svg"
    ]

class H5PViewSet(SnippetViewSet):
    ...