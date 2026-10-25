import http.server,json,os,sys,urllib.parse,datetime
ROOT=__import__('os').path.dirname(__import__('os').path.dirname(__import__('os').path.abspath(__file__)));STORE={}
class H(http.server.SimpleHTTPRequestHandler):
    def __init__(s,*a,**k): super().__init__(*a,directory=ROOT,**k)
    def log_message(s,*a): pass
    def _j(s,o,c=200):
        b=json.dumps(o,ensure_ascii=False).encode();s.send_response(c);s.send_header('Content-Type','application/json');s.send_header('Content-Length',str(len(b)));s.end_headers();s.wfile.write(b)
    def do_GET(s):
        u=urllib.parse.urlparse(s.path);q=urllib.parse.parse_qs(u.query)
        if u.path=='/api/listele':
            il=q['il'][0];return s._j([{'ym':ym,'boyut':len(v['b']),'guncelleme':v['t'],'yukleyen':v['u']} for (i,ym),v in STORE.items() if i==il])
        if u.path=='/api/indir':
            v=STORE.get((q['il'][0],q['ym'][0]))
            if not v:return s._j({'hata':'yok'},404)
            s.send_response(200);s.send_header('Content-Length',str(len(v['b'])));s.end_headers();s.wfile.write(v['b']);return
        return super().do_GET()
    def do_POST(s):
        u=urllib.parse.urlparse(s.path);q=urllib.parse.parse_qs(u.query);n=int(s.headers.get('Content-Length',0));b=s.rfile.read(n)
        rol=q.get('rol',[''])[0];kil=q.get('kil',[''])[0];il=q.get('il',[''])[0]
        ok=rol=='super_admin' or (rol=='il_admin' and kil==il)
        if u.path in('/api/yukle','/api/sil') and not ok:return s._j({'hata':'yetki yok'},403)
        if u.path=='/api/yukle':
            STORE[(il,q['ym'][0])]={'b':b,'t':datetime.datetime.now().isoformat(),'u':q.get('ad',[''])[0]};return s._j({'ok':1})
        if u.path=='/api/sil':
            STORE.pop((il,q['ym'][0]),None);return s._j({'ok':1})
        if u.path=='/api/ozet':
            return s._j({'ok':1,'boyut':len(b)})
        s._j({'hata':'?'},404)
http.server.ThreadingHTTPServer(('',int(sys.argv[1])),H).serve_forever()
