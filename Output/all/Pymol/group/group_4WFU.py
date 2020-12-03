from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4WFU.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 14-25 & chain A, resi 41-45 & chain A, resi 50-59 & chain A, resi 36-38 & chain A, resi 62-71 & chain A, resi 77-82 & chain A, resi 85-94 & chain A, resi 97-105 & chain A, resi 109-119 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-32.26129109346414,26.900303913068168,-14.38164555724663])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
