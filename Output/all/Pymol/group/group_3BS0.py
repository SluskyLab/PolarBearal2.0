from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3BS0.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 44-60 & chain A, resi 66-69 & chain A, resi 417-433 & chain A, resi 390-405 & chain A, resi 376-385 & chain A, resi 348-356 & chain A, resi 333-343 & chain A, resi 293-302 & chain A, resi 280-288 & chain A, resi 233-240 & chain A, resi 214-228 & chain A, resi 151-155 & chain A, resi 139-143 & chain A, resi 93-108 & chain A, resi 80-90 & chain A, resi 129-136 & chain A, resi 158-169 & chain A, resi 199-204 & chain A, resi 248-257 & chain A, resi 263-272 & chain A, resi 314-317 & chain A, resi 320-324 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[16.63203670808174,-2.3058073134289696,16.232426552349754])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
