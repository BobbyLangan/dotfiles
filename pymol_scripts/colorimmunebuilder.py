from pymol import cmd


def coloribuild(selection="all"):
    """
    AUTHOR
    Christian Balbin

    DESCRIPTION
    Colors Alphafold structures by pLDDT

    USAGE
    coloraf sele

    PARAMETERS

    sele (string)
    The name of the selection/object to color by pLDDT. Default: all
    """

    cmd.color("blue", f"({selection}) and b < 0.5")
    cmd.color("cyan", f"({selection}) and b > 0.5 and b < 1")
    cmd.color("yellow", f"({selection}) and b > 1 and b < 1.5")
    cmd.color("orange", f"({selection}) and b > 1.5")


cmd.extend("coloribuild", coloribuild)
cmd.auto_arg[0]["coloribuild"] = [cmd.object_sc, "object", ""]
