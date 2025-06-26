import re

# Kommandoliste
commands = []

def parse_pattern(pattern):
    regex = "^"
    i = 0
    placeholders = []

    while i < len(pattern):
        optional = False
        if pattern[i] == "?":
            optional = True
            if pattern[i+1:i+4] in ("{n}", "{s}"):
                i += 1

        if pattern[i:i+3] == "{n}":
            part = r"\s*(\d+)"
            placeholders.append("n")
            i += 3
        elif pattern[i:i+3] == "{s}":
            part = r"\s*(.+)"
            placeholders.append("s")
            i += 3
        else:
            c = pattern[i]
            i += 1

            if c == "'":
                text = ""
                while i < len(pattern) and pattern[i] != "'":
                    text += pattern[i]
                    i += 1
                i += 1
                part = re.escape(text)
            elif c == "?":
                text = ""
                while i < len(pattern) and pattern[i] != "?":
                    text += pattern[i]
                    i += 1
                i += 1
                part = f"(?:\\s*{re.escape(text)})?"
            else:
                part = re.escape(c)

        if optional:
            part = f"(?:{part})?"

        regex += part

    regex += ".*$"
    return regex, placeholders


def add_command(pattern, func):
    regex, placeholders = parse_pattern(pattern)
    commands.append((re.compile(regex, re.IGNORECASE), placeholders, func))


def handle_input(text):
    for regex, placeholders, func in commands:
        match = regex.match(text)
        if match:
            raw_args = match.groups()
            final_args = []

            for placeholder, value in zip(placeholders, raw_args):
                if placeholder == "n":
                    final_args.append(int(value))
                elif placeholder == "s":
                    final_args.append(value)
            func(*final_args)
            return

    print("Kein passender Befehl gefunden.")


