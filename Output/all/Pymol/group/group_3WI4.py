from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3WI4.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 3-21 & chain A, resi 26-29 & chain A, resi 41-51 & chain A, resi 54-63 & chain A, resi 78-84 & chain A, resi 87-95 & chain A, resi 125-132 & chain A, resi 139-146 & chain A, resi 158-167 & chain A, resi 170-181 & chain A, resi 190-204 & chain A, resi 207-220 & chain A, resi 227-238 & chain A, resi 247-253 & chain A, resi 267-277 & chain A, resi 282-293 & chain A, resi 300-312 & chain A, resi 32-37 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[20.14473931473541,-13.322776644867151,30.803404250043503])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
