import OpenPS

event = OpenPS.Event()

event.init() # Initialize the events otherwise the built-in events will won't works.

event.create("OnProgramFoo") # Create event.
event.call("OnProgramFoo") # Call the event.
