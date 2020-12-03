from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2LME.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 52-63 & chain A, resi 66-77 & chain A, resi 84-90 & chain A, resi 94-104 & chain A, resi 94-104 & chain B, resi 84-90 & chain B, resi 66-77 & chain B, resi 52-63 & chain B, resi 52-63 & chain C, resi 66-77 & chain C, resi 84-90 & chain C, resi 94-104 & chain C, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[0.276706342851477,-12.024174597942167,-0.4495476191301668])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
