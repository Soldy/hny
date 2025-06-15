"""
These are just a couple of simple vt100 true color functions (concept). Not less not more.
"""


def __print(text: str):
  print(
    text,
    end="",
    sep="",
    flush=True
  )
def cstr (text: str, color: str)->str:
  return (
    "\x1b[38;2;"+
    color+
    "m"+
    text+
    "\x1b[0m"
  )

def fcstr (text: str, color: str, background: str)->str:
  return (
    "\x1b[38;2;"+
    color+
    "m\x1b[48;2;"+
    background+
    "m"+
    text+
    "\x1b[0m"
  )

def cprint (text: str, color: str)->str:
  print(
    "\x1b[38;2;",
    color,
    "m",
    text,
    "\x1b[0m",
    end="",
    sep="",
    flush=True
  )

def fcprint (text: str, color: str, background: str)->str:
  print(
    "\x1b[38;2;",
    color,
    "m\x1b[48;2;",
    background,
    "m",
    text,
    "\x1b[0m",
    end="",
    sep="",
    flush=True
  )

def aprint (text: str, color: str, background: str, col: int, row: int)->str:
  print(
    "\x1b[",
    str(col),
    ";",
    str(row),
    "H\x1b[38;2;",
    color,
    "m\x1b[48;2;",
    background,
    "m",
    text,
    "\x1b[0m",
    end="",
    sep="",
    flush=True
  )

