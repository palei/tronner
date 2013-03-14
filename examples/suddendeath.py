from tronner import App, command

app = App()

# start sudden death after 30 seconds
@app.timed_event('NEW_ROUND', 30)
def sudden_death():
    command.center_message('0xff0000SUDDEN DEATH!')
    command.command('CYCLE_RUBBER 0.1')
    command.command('CYCLE_BRAKE -100')

# reset to normal settings when new round starts
@app.event('NEW_ROUND')
def new_round():
    command.include('settings_custom.cfg')

if __name__ == '__main__':
    app.run()
