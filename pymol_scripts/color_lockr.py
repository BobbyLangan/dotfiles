from pymol import cmd, util


def color_lockr(sequence):
    for obj in cmd.get_names():
        obj_sequence = cmd.get_fastastr(obj)
        loc = obj_sequence.find(sequence)
        if loc < 0:
            continue

        loc = loc + 1  # normalize to resnumbering
        cmd.color("skyblue", obj)
        cmd.color("orange", f"{obj} and res {loc}-{loc + len(sequence) - 1}")
        util.cnc()
        cmd.show("sticks", f"{obj} and not name c+o+n")

    cmd.hide("sticks", "(h. and (e. c extend 1))")


cmd.extend("lockr", color_lockr)
