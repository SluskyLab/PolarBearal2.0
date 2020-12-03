from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3DZM.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 3-13 & chain A, resi 16-25 & chain A, resi 33-43 & chain A, resi 69-83 & chain A, resi 93-110 & chain A, resi 120-141 & chain A, resi 144-155 & chain A, resi 160-165 & chain A, resi 171-176 & chain A, resi 195-206 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[61.08869081202561,-58.906235671624906,-23.22193495432536])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
