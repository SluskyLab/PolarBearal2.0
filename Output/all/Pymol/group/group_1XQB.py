from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1XQB.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 4-6 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[12.289333661397299,25.817333857218426,30.297666549682617])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 10-13 & chain A, resi 33-38 & chain A, resi 116-123 & chain A, resi 100-113 & chain A, resi 56-62 & chain A, resi 131-137 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[24.789956424547277,16.852587067562602,17.51621737687484])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 163-165 & chain A, resi 225-227 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[16.749666849772137,-9.018166542053223,0.28683334589004517])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 210-213 & chain A, resi 216-219 & chain A, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[11.137374877929688,2.292250070720911,3.10699999704957])
cmd.color ("purple", "Centroid3")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
