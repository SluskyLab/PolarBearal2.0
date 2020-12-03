from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1Y0G.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 24-27 & chain B, resi 55-60 & chain B, resi 70-76 & chain B, resi 104-115 & chain B, resi 118-127 & chain B, resi 130-145 & chain B, resi 151-162 & chain B, resi 178-189 & chain B, resi 34-42 & chain B, resi 46-52 & chain B, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-27.29436835238808,12.230031635886744,37.95686312223736])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
