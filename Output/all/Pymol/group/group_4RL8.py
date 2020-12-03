from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4RL8.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 16-32 & chain A, resi 35-38 & chain A, resi 253-267 & chain A, resi 238-250 & chain A, resi 221-233 & chain A, resi 196-207 & chain A, resi 181-193 & chain A, resi 152-163 & chain A, resi 137-148 & chain A, resi 109-118 & chain A, resi 93-96 & chain A, resi 67-79 & chain A, resi 41-57 & chain A, resi 62-64 & chain A, resi 87-90 & chain A, resi 99-102 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[4.422813254172903,15.413283081388617,14.9408975633153])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 166-169 & chain A, resi 174-178 & chain A, resi 210-212 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[26.83566665649414,7.881166696548462,5.60866666212678])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
