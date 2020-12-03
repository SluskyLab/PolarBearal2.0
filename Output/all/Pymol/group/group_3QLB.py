from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3QLB.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 54-59 & chain A, resi 127-134 & chain A, resi 148-154 & chain A, resi 106-108 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[48.1166664759318,-37.5094579855601,-3.5140833432475724])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 162-170 & chain A, resi 174-184 & chain A, resi 191-201 & chain A, resi 212-222 & chain A, resi 228-240 & chain A, resi 275-289 & chain A, resi 294-317 & chain A, resi 323-346 & chain A, resi 353-381 & chain A, resi 401-422 & chain A, resi 426-443 & chain A, resi 448-465 & chain A, resi 471-482 & chain A, resi 497-508 & chain A, resi 515-532 & chain A, resi 540-558 & chain A, resi 563-577 & chain A, resi 595-604 & chain A, resi 613-622 & chain A, resi 638-648 & chain A, resi 659-666 & chain A, resi 689-697 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[52.49424012018917,-32.588847979767344,-5.015121564908819])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 674-677 & chain A, resi 682-684 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[44.46614292689732,-13.33914293561663,-14.678999900817871])
cmd.color ("orange", "Centroid2")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
