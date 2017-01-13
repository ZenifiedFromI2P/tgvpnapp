from livereload import Server, shell

server = Server()

# output stdout into a file
shcmd = shell('transcrypt main.py',)
server.watch('views/*.py', shcmd)
server.watch('*.py', shcmd)

server.watch('wrap.js', shell('browserify -n -o bundle.js wrap.js'))

server.serve(root='.')
