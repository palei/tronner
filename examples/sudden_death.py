from tronner import App, command

app = App()

@app.timed_event('NEW_ROUND', 300)
def sudden_death():
    command.center_message('0xff0000SUDDEN DEATH!')
    command.command('CYCLE_RUBBER 0.1')
    command.command('CYCLE_BRAKE -100')

if __name__ == '__main__':
    app.run()
