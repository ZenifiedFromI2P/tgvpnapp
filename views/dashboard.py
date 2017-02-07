from const import SLOT
from db import db
_t1 = """
<hr>
<form id="smsg">
<div class="form-group">
	<input id="f2-whattosign" name="f1-wts" type="text" placeholder="What to sign? Generate some words?" required class="form-control" />
</div>
<button type="submit" class="btn btn-lg btn-primary">Submit</button>
</form>
<hr>
<button id="genat" type="button" class="btn btn-lg btn-primary">Generate a random authentication token?</button>
""".strip()

_t2 = """
Original message: {msg}
Username: {addr}
Password: {sig}
""".strip()


class View(object):

    def spost(self, ev):
        # Ignore event, let it be garbage-collected.
        try:
            con = jQuery("#f2-whattosign").val()
            privkey = db['ck'].privateKey
            sig = coinmsg.sign(privkey, con)  # a-ck
            b64encoded = btoa(String.fromCharCode.apply(null, sig))
            formatted = _t2.format(
                msg=con,
                addr=db['ck'].publicAddress,
                sig=b64encoded)
        except:
            window.alert("Exception occurred")
            window.alert(__except0__.message)
        else:
            jQuery(SLOT).append(
                "<pre><code>{s}</code></pre>".format(s=formatted))
        return False
        pass

        def genat(self):
            def cb(resp):
                if resp.error is not None:
                    window.alert("Fatal error, server sent alert.")
                    window.alert(resp.errormsg)
                    return False
                    pass
                w = resp.words
                privkey = db['ck'].privateKey
                sig = coinmsg.sign(privkey, w)  # a-ck
                # Signed, transmit
                b64encoded = btoa(String.fromCharCode.apply(null, sig))
                formatted = _t2.format(
                    msg=con, addr=db['ck'].publicAddress, sig=b64encoded)
                jQuery(SLOT).append(
                    "<pre><code>{s}</code></pre>".format(s=formatted))
                pass
            names = __new__(Object)
            names.baddr = db['ck'].publicAddress
            jQuery.getJSON('/d/api/getwords/', names, cb)
            pass

    def do(self, hashparams):
        jQuery(SLOT).empty()
        jQuery(SLOT).append(
            "<p>The address is {}</p>".format(db.get('ck').publicAddress))
        jQuery(SLOT).append(_t1)
        jQuery("#smsg").submit(self.spost)
        pass
