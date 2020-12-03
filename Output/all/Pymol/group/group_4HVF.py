from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4HVF.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 6-15 & chain A, resi 18-29 & chain A, resi 34-41 & chain A, resi 111-121 & chain A, resi 98-108 & chain A, resi 85-93 & chain A, resi 168-178 & chain A, resi 151-162 & chain A, resi 134-137 & chain A, resi 140-148 & chain A, resi 192-202 & chain A, resi 206-216 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-18.037519985198976,4.331839987099171,-5.654656023271382])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
