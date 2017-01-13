from const import SLOT as SLOT
from views.login import Login

def ParseHParams(hstr):
    g1 = hstr.split('?')
    g2 = g1[len(g1)-1]
    # hstr == '?key=value', g1 = 'key=value'
    g3 = g2.split('&')
    # hstr == '?t1=t2&g1=g2', g1 = 't1=t2&g1=g2', g2 = ['t1=t2', 'g1=g2']
    results = {}
    for i in g3:
        s = i.split('=')
        results.update({s[0]: s[1]})
    return results

def NopFunc(ignored):
    print("Faced NOP in router")
    pass

def ParseHash(hash):
    g1 = hash.split('?')
    return g1[0] # Anything before ?

def hashchange():
    dlh = document.location.hash or '?#'
    print(dlh)
    parsedhash = ParseHash(dlh.split('#')[1])
    hparams = ParseHParams(dlh)
    f = window.routes.get(parsedhash, window.routes['login'])
    f(hparams)
    pass

window.routes = {
    'login': Login().do,
}
window.psh = ParseHParams
window.addEventListener("hashchange", hashchange, False);
# On website load time, this is fired
hashchange() # Runtime
