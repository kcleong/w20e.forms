from w20e.forms.rendering.interfaces import IControlRenderer
from zope.interface import implements
from templates import TEMPLATES


class HiddenRenderer:

    implements(IControlRenderer)

    def render(self, renderer, form, renderable, out, **kwargs):

        """ render Hidden to HTML """
    
        fmtmap = renderer.createFormatMap(form, renderable, **kwargs)

        try:
            value = form.getFieldValue(renderable.bind)
        except:
            value = ""
    
        print >> out, TEMPLATES['HIDDEN'](control=renderable, 
                                          value=value,
                                          extra_classes=fmtmap['extra_classes']
                                          )

