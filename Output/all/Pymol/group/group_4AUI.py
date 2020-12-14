from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4AUI.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 2-21 & chain A, resi 40-47 & chain A, resi 54-62 & chain A, resi 78-83 & chain A, resi 86-94 & chain A, resi 124-135 & chain A, resi 138-145 & chain A, resi 157-165 & chain A, resi 169-178 & chain A, resi 185-198 & chain A, resi 201-214 & chain A, resi 221-234 & chain A, resi 242-248 & chain A, resi 262-272 & chain A, resi 277-289 & chain A, resi 293-307 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[23.35763121184024,-1.8589106123145234,53.186430115939515])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
