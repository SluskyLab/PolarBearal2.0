from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5NXR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 2-4 & chain A, resi 9-23 & chain A, resi 39-49 & chain A, resi 54-65 & chain A, resi 75-86 & chain A, resi 90-98 & chain A, resi 129-138 & chain A, resi 148-155 & chain A, resi 175-185 & chain A, resi 188-198 & chain A, resi 222-234 & chain A, resi 237-247 & chain A, resi 261-271 & chain A, resi 277-289 & chain A, resi 298-311 & chain A, resi 316-325 & chain A, resi 343-351 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-22.966366163368434,39.40553005406114,-40.33436605317996])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 207-210 & chain A, resi 213-216 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[-54.53900098800659,40.359750270843506,-43.10400056838989])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
