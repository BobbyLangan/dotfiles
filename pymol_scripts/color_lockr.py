from pymol import cmd, util
import re


def color_lockr(sequence):
    for obj in cmd.get_names():
        fasta_preformat = cmd.get_fastastr(obj)
        obj_sequence = ""
        for line in fasta_preformat.splitlines():
            if re.match("^>", line):
                continue
            obj_sequence += line

        loc = obj_sequence.find(sequence)
        print(obj, obj_sequence, loc)
        if loc < 0:
            continue

        loc = loc + 1  # normalize to resnumbering
        cmd.color("skyblue", obj)
        cmd.color("orange", f"{obj} and res {loc}-{loc + len(sequence) - 1}")
        util.cnc()
        cmd.show("sticks", f"{obj} and not name c+o+n")

    cmd.hide("sticks", "(h. and (e. c extend 1))")


cmd.extend("lockr", color_lockr)
