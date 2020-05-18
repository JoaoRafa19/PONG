import cx_Freeze

executables = [cx_Freeze.Executable("main.py", base = "Win32GUI",icon="icon.ico")]

cx_Freeze.setup(
    name="Pong",
    options={"build_exe": {"packages": ["pygame"],
                          "include_files": ["ball.png","player.png","split.png"]}},
    description="A Pong copy",

    executables = executables
    )