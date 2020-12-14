from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2Y0L.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 21-33 & chain A, resi 42-52 & chain A, resi 62-111 & chain A, resi 114-121 & chain A, resi 139-147 & chain A, resi 153-164 & chain A, resi 191-198 & chain A, resi 204-213 & chain A, resi 217-229 & chain A, resi 234-246 & chain A, resi 256-268 & chain A, resi 271-281 & chain A, resi 311-320 & chain A, resi 329-339 & chain A, resi 352-362 & chain A, resi 372-382 & chain A, resi 388-400 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-5.362023899935489,27.846722551510094,5.18607658033736])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
