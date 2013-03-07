An Armagetron Advanced Event Handling Framework
===============================================
- [Examples](#examples)
- [Installation](#installation)

# <a id="examples"></a>Examples
## A simple greeter

    #!/usr/bin/env python
    from tronner import App
    app = App()

    @app.event('PLAYER_ENTERED')
    def player_entered():
        print "Welcome, %s" % app.L[1]

    app.run()

# <a id="installation"></a>Installation
    git clone git@bitbucket.org:noob13/tronner.git
## Requirements

## Examples
