import imp
from   io                   import StringIO
from   pluggdapps.plugin    import Plugin, implements
import pluggdapps.utils     as h
from   tayra                import BaseTTLPlugin

def __traceback_decorator__( frames ):
    from copy    import deepcopy
    from os.path import basename

    def _map2ttl( frame ):
        filename = frame.filename
        lineno = frame.lineno
        lines = open(filename).readlines()[:lineno]
        lines.reverse()
        rc = {}
        for l in lines :
            if l.strip().startswith('# lineno') :
                _, ttl_lineno = l.split(':', 1)
                ttl_lineno = int( ttl_lineno )
                ttl_text = open( _ttlfile ).readlines()[ ttl_lineno-1 ]
                return ttl_lineno, ttl_text
        return None, None

    newframes = []
    for frame in frames :
        newframes.append( frame )
        frameadded = getattr( frame, '_ttlframeadded', False )

        basen = basename( frame.filename )
        if basen.endswith( '.ttl.py' )              and basen == (basename( _ttlfile ) + '.py')              and frameadded == False :
            newframe = deepcopy( frame )
            frame._ttlframeadded = True
            try :
                newframe.lineno, newframe.linetext = _map2ttl( newframe )
                if newframe.lineno :
                    newframe.filename = _ttlfile
                    newframes.append( newframe )
            except :
                raise
                continue
    return newframes



def body( *args, **kwargs ) :  
  _m.pushbuf()
  # lineno:3
  _m.pushbuf()
  _m.extend( ['<html>'] )
  _m.pushbuf()
  # lineno:3
  _m.extend( [' ', '\n  ', '<!--', ' Trying to inline a comment ', '-->', '\n  '] )
  # lineno:5
  _m.extend( ['fair enough', '\n  '] )
  # lineno:6
  _m.pushbuf()
  _m.extend( ['<head>'] )
  _m.pushbuf()
  _m.extend( ['\n    ', '<!--', ' An inline comment spanning multiple\n      lines ', '-->', '\n  '] )
  _m.handletag( _m.popbuftext(), _m.popbuftext(), indent=False, nl='')
  # lineno:9
  _m.pushbuf()
  _m.extend( ['<body>'] )
  _m.pushbuf()
  _m.extend( ['\n    '] )
  # lineno:10
  _m.extend( ['try inline', '\n    ', '<!--', ' comments inside text-lines ', '-->', '\n    '] )
  # lineno:12
  _m.extend( ['again', '\n    ', '<!--', ' spanning across multiple\n    lines\n      with indentation ', '-->', '\n    '] )
  # lineno:16
  _m.extend( ['and finally finish it with text.', '\n'] )
  _m.handletag( _m.popbuftext(), _m.popbuftext(), indent=False, nl='')
  _m.handletag( _m.popbuftext(), _m.popbuftext(), indent=False, nl='')
  return _m.popbuftext()

# ---- Global Functions
# ---- Interface functions

# ---- Footer
_ttlhash = ''
_ttlfile = '/home/pratap/dev/tayra/tayra/test/stdttl/comments.ttl' 