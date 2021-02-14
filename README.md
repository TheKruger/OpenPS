# OpenPS
Open source plugin system.

# Install

Windows
```
python setup.py build
```

Linux
```
python3 setup.py build
```

# How to use

```
.
├─── plugins
│    └─── hello.py
└─── main_prgram.py
```

You need to add a `plugin.py` file.
```
.
├─── plugins
│    └─── hello.py
├─── main_prgram.py
└─── plugin.py
```
Write the following code to the `plugin.py`


```py
# plugin.py
import OpenPS

event = OpenPS.Event("./plugins/")

call = lambda name: event.call(name)
register = lambda name: event.register(name)

event.init()
```

If you want to add your own events then add this line in the code **above the `event.init()` line**.

```py
# plugin.py
import OpenPS

event = OpenPS.Event("./plugins/")

call = lambda name: event.call(name)
register = lambda name: event.register(name)

event.create("OnProgramFoo") # Create event.

event.init()
```

```py
# main.py
import plugin

def main():
  plugin.call("OnProgramFoo")
  print("hello world!")

main()
```

```py
# /plugins/hello.py
import plugin

@plugin.register()
def function():
  print("hello from the plugin!")
```

When you run the `main.py` the output should be looks like this
```
hello from the plugin!
hello world!
```
