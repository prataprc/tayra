import re
from   copy         import deepcopy

def parsespecifiers( specifiers ) :
    try :
        first, rest = ' '.join( specifiers.splitlines() ).split(' ', 1)
    except :
        first, rest = specifiers, ''
    if first.startswith('#') :
        try :
            id_, classes = first[1:].split('.', 1)
        except :
            id_, classes = first[1:], ''
        classes = classes.replace('.', ' ')
    elif first.startswith('.') :
        id_, classes = '', first.replace('.', ' ').strip(' ')
    else :
        rest = ' '.join([ first, rest ])
        id_ = classes = ''

    id_ = 'id="%s"' % id_.strip() if id_ else id_
    classes = 'class="%s"' % classes.strip() if classes else classes
    
    # Parse tag-specifiers
    rest, tokens = rest.strip(' '), [ '' ]
    stringify = False
    for c in rest :
        if stringify :
            tokens[-1] += c
            if c == stringify :
                stringify = None
                tokens.append( '' )
            continue
        elif c == ' ' : 
            tokens.append( '' )
            continue
        tokens[-1] += c
        if tokens[-1] in '\'"' : stringify = tokens[-1]
    return id_, classes, filter( None, tokens )


_enctype = [
    'application/x-www-form-urlencoded', 'multipart/form-data', 'text/plain'
]
_shape  = [ 'default', 'rect', 'circle', 'poly' ]
_dir    = [ 'ltr', 'rtl' ]
_target = [ '_blank', '_self', '_parent', '_top' ]
_method = [ 'get', 'post' ]
def stdspecifiers( spectokens ):
    tokens = deepcopy( spectokens )
    leftover, specattrs = [], []
    while tokens :
        tok = tokens.pop(0)
        if tok in _shape :
            specattrs.append( 'shape="%s"' % tok )
            continue
        if tok in _dir :
            specattrs.append( 'dir="%s"' % tok )
            continue
        if tok in _target :
            specattrs.append( 'target="%s"' % tok )
            continue
        if tok in _method :
            specattrs.append( 'method="%s"' % tok )
            continue
        if tok in _enctype :
            specattrs.append( 'enctype="%s"' % tok )
            continue
        if tok == 'disabled' :
            specattrs.append( 'disabled="disabled"' )
            continue
        if tok == 'checked' :
            specattrs.append( 'checked="checked"' )
            continue
        if tok == 'readonly' :
            specattrs.append( 'readonly="readonly"' )
            continue
        if tok == 'selected' :
            specattrs.append( 'selected="selected"' )
            continue
        if tok == 'multiple' :
            specattrs.append( 'multiple="multiple"' )
            continue
        if tok == 'defer' :
            specattrs.append( 'defer="defer"' )
            continue
        leftover.append( tok )
    return filter(None, leftover), specattrs

def composetag( tagopen, specattrs, style, attrs, tagfinish ):
    tagopen = tagopen.rstrip(' ')
    style = 'style="%s"' % style.strip(' ') if style else style
    specattrs = ' '.join( specattrs )
    attrs = ' '.join( attrs )
    cont = ' '.join( filter( None, [ tagopen, specattrs, style, attrs ]) )
    return cont + tagfinish

def handle_default( tagopen, specifiers, style, attrs, tagfinish ):
    id_, classes, tokens = parsespecifiers( specifiers )
    tokens, specattrs = stdspecifiers( tokens )
    specattrs = filter( None, [id_, classes] ) + specattrs
    return composetag( tagopen, specattrs, style, attrs, tagfinish )
