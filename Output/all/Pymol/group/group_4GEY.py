from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4GEY.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 27-42 & chain A, resi 51-64 & chain A, resi 74-85 & chain A, resi 114-125 & chain A, resi 130-137 & chain A, resi 175-185 & chain A, resi 188-197 & chain A, resi 217-226 & chain A, resi 233-244 & chain A, resi 273-283 & chain A, resi 294-304 & chain A, resi 311-322 & chain A, resi 332-342 & chain A, resi 373-384 & chain A, resi 389-399 & chain A, resi 410-420 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[24.69874994651131,37.862396675607435,62.68967916654504])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 248-254 & chain A, resi 267-270 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[9.088909019123424,50.63018209284002,84.91827184503728])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
