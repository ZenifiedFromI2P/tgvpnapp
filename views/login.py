from const import SLOT
from db import db
import views.dashboard as dashboard
_t1 = """
<form id="login">
<div class="form-group">
	<input id="f1-bitaddr" name="f1-ba" type="text" placeholder="Bitcoin private key" required class="form-control" />
</div>
<button type="submit" class="btn btn-lg btn-primary">Submit</button>
</form>
<button id="shouldgenrand" type="button" class="btn btn-lg btn-primary">Generate a random one?</button>
<div id="errslot"></div>
""".strip()


class Login():

    def post(self):
        ba = jQuery("#f1-bitaddr").val()
        if not ba.strip():
            jQuery("#errslot").html("NO DATA SUPPLIED, ALERT!")
        try:
            db['pk'] = Buffer(ba, 'hex')
            db['ck'] = coinkey(db['pk'])
        except:
            window.alert("Faced exception, check console")
            # The exception, we must consume it immediately!
            window.alert(__except0__.message)
            console.log(__except0__.message)
            return False
        dashboard.View().do({})
        return False  # Failed callback, don't worry, we consumed it, no other stuff

    def head(self):
        cko = coinkey.createRandom()
        db['pk'] = cko.publicKey
        db['ck'] = cko
        dashboard.View().do({})
        return False

    def do(self, params):
        jQuery(SLOT).html(_t1)
        jQuery("#login").submit(self.post)
        jQuery("#shouldgenrand").click(self.head)
