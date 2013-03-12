from tronner import App
app = App()

@app.event('PLAYER_ENTERED <name>')
def player_entered(name):
  print "Greetings, %s" % name

if __name__ == '__main__':
  app.run()
