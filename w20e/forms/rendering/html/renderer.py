from zope.interface import implements

from w20e.forms.rendering.interfaces import IRenderer
from w20e.forms.rendering.baserenderer import BaseRenderer


class HTMLRenderer(BaseRenderer):

    """ The HTML renderer expects to recive some kind of output
    stream, that can be used to append to. This can obviously be
    sys.stdout, but also a stringIO instance.
    """
    
    implements(IRenderer)


    def __init__(self, **kwargs):

        BaseRenderer.__init__(self, **kwargs)
        

    def renderFrontMatter(self, form, out):

        """ Render whatever needs to be rendered before the actual form
        components """
        
        print >> out, """<form class="w20e-form" method="post" action="%s" enctype="multipart/form-data">""" % getattr(form.submission, 'action', '')
        print >> out, """<input type="hidden" name="formprocess" value="1"/>"""
        print >> out, """<div class="alert"></div>"""


    def renderBackMatter(self, form, out):

        print >> out, "</form>"


    def render(self, form, renderable, out, errors={}, **kwargs):

        try:            
            rtype = renderable.type
            renderer = self.getRendererForType(rtype, "html")()
            try:
                field_errors = errors.get(renderable.bind, [])
            except:
                field_errors = []
            renderer.render(self, form, renderable, out, errors=field_errors, **kwargs)
        except:

            print >> out, "<blink>No renderer found for %s!</blink>" % rtype
