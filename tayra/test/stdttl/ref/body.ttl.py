import imp
from   io                   import StringIO
from   pluggdapps.plugin    import Plugin, implements
import pluggdapps.utils     as h
from   tayra                import BaseTTLPlugin


def body( id="hello", cls="world", style='color: red;', *args, **kwargs ) :  
  _m.pushbuf()
  _m.pushbuf()
  _m.extend( ['<div #'] )
  _m.append(_m.evalexprs( 'id', '', globals(), locals()) )
  _m.extend( [' .'] )
  _m.append(_m.evalexprs( 'cls', '', globals(), locals()) )
  _m.extend( [' {'] )
  _m.append(_m.evalexprs( 'style', '', globals(), locals()) )
  _m.extend( ['} >'] )
  _m.pushbuf()
  _m.extend( ['\n'] )
  _m.handletag( _m.popbuftext(), _m.popbuftext(), indent=False, nl='')
  return _m.popbuftext()

# ---- Global Functions
# ---- Interface functions

# ---- Footer
_ttlhash = ''
_ttlfile = '/home/pratap/dev/tayra/tayra/test/stdttl/body.ttl' 