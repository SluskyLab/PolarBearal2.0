from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6UCU.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 83-93 & chain A, resi 97-106 & chain A, resi 114-121 & chain A, resi 125-132 & chain A, resi 137-143 & chain A, resi 150-157 & chain A, resi 164-172 & chain A, resi 176-187 & chain A, resi 193-203 & chain A, resi 209-219 & chain A, resi 227-237 & chain A, resi 243-249 & chain A, resi 255-264 & chain A, resi 267-275 & chain A, resi 299-308 & chain A, resi 312-319 & chain A, resi 323-331 & chain A, resi 337-345 & chain A, resi 350-362 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[161.191541471534,166.8481822988605,150.13586198163955])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
