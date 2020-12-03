from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1ZXU.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 38-43 & chain A, resi 54-58 & chain A, resi 63-68 & chain A, resi 77-81 & chain A, resi 87-92 & chain A, resi 101-106 & chain A, resi 115-120 & chain A, resi 131-135 & chain A, resi 146-149 & chain A, resi 158-161 & chain A, resi 167-173 & chain A, resi 187-191 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[9.862938433029473,0.5257845774292946,2.6726769286852616])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
