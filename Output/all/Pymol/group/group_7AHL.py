from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/7AHL.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 111-122 & chain A, resi 136-147 & chain A, resi 132-147 & chain B, resi 111-126 & chain B, resi 135-147 & chain C, resi 111-123 & chain C, resi 136-147 & chain D, resi 111-122 & chain D, resi 136-147 & chain E, resi 111-122 & chain E, resi 132-147 & chain F, resi 111-126 & chain F, resi 111-126 & chain G, resi 132-147 & chain G, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[26.72947937050431,32.95981439610117,19.664814426650093])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 153-158 & chain A, resi 164-171 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[54.15300015040806,4.336428544351032,39.913285800388884])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 228-234 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[63.01000050136021,4.254428608076913,54.09228515625])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 242-260 & chain A, resi 265-270 & chain A, resi 274-285 & chain A, resi 290-292 & chain A, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[62.18185052871704,-2.5103500042110682,33.79607492685318])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 153-158 & chain B, resi 164-171 & chain B, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[36.89128548758371,11.362000124795097,56.72107097080776])
cmd.color ("yellow", "Centroid4")


cmd.select("Group5", "(resi 228-234 & chain B, )")
cmd.color ("green", "Group5")


cmd.pseudoatom ("Centroid5", pos=[46.64485713413784,14.074571337018694,70.02271434238979])
cmd.color ("green", "Centroid5")


cmd.select("Group6", "(resi 242-260 & chain B, resi 265-270 & chain B, resi 274-285 & chain B, resi 290-292 & chain B, )")
cmd.color ("cyan", "Group6")


cmd.pseudoatom ("Centroid6", pos=[38.38162498474121,-0.7598750083474443,56.891550350189206])
cmd.color ("cyan", "Centroid6")


cmd.select("Group7", "(resi 153-158 & chain C, resi 164-171 & chain C, )")
cmd.color ("blue", "Group7")


cmd.pseudoatom ("Centroid7", pos=[30.02921417781285,34.5460718699864,63.377285548618865])
cmd.color ("blue", "Centroid7")


cmd.select("Group8", "(resi 228-234 & chain C, )")
cmd.color ("purple", "Group8")


cmd.pseudoatom ("Centroid8", pos=[41.978428976876394,38.0704277583531,74.52614375523159])
cmd.color ("purple", "Centroid8")


cmd.select("Group9", "(resi 242-260 & chain C, resi 265-270 & chain C, resi 274-285 & chain C, resi 290-292 & chain C, )")
cmd.color ("red", "Group9")


cmd.pseudoatom ("Centroid9", pos=[24.554949975013734,26.189574861526488,70.56327505111695])
cmd.color ("red", "Centroid9")


cmd.select("Group10", "(resi 153-158 & chain D, resi 164-171 & chain D, )")
cmd.color ("orange", "Group10")


cmd.pseudoatom ("Centroid10", pos=[38.79114300864084,56.432285581316265,54.81364277430943])
cmd.color ("orange", "Centroid10")


cmd.select("Group11", "(resi 228-234 & chain D, )")
cmd.color ("yellow", "Group11")


cmd.pseudoatom ("Centroid11", pos=[52.479000091552734,58.02942820957729,64.22328567504883])
cmd.color ("yellow", "Centroid11")


cmd.select("Group12", "(resi 242-261 & chain D, resi 264-270 & chain D, resi 274-285 & chain D, resi 290-292 & chain D, )")
cmd.color ("green", "Group12")


cmd.pseudoatom ("Centroid12", pos=[29.726595305261156,57.78728557768322,63.12945275079636])
cmd.color ("green", "Centroid12")


cmd.select("Group13", "(resi 153-158 & chain E, resi 164-171 & chain E, )")
cmd.color ("cyan", "Group13")


cmd.pseudoatom ("Centroid13", pos=[56.46214294433594,60.55614307948521,37.545928137642996])
cmd.color ("cyan", "Centroid13")


cmd.select("Group14", "(resi 228-234 & chain E, )")
cmd.color ("blue", "Group14")


cmd.pseudoatom ("Centroid14", pos=[70.23699951171875,59.11685725620815,46.963285718645366])
cmd.color ("blue", "Centroid14")


cmd.select("Group15", "(resi 242-260 & chain E, resi 265-270 & chain E, resi 274-285 & chain E, resi 290-292 & chain E, )")
cmd.color ("purple", "Group15")


cmd.pseudoatom ("Centroid15", pos=[53.00885033607483,71.17610034942626,42.72712483406067])
cmd.color ("purple", "Centroid15")


cmd.select("Group16", "(resi 153-158 & chain F, resi 164-171 & chain F, )")
cmd.color ("red", "Group16")


cmd.pseudoatom ("Centroid16", pos=[69.87042890276227,43.823286056518555,24.571571486336843])
cmd.color ("red", "Centroid16")


cmd.select("Group17", "(resi 228-234 & chain F, )")
cmd.color ("orange", "Group17")


cmd.pseudoatom ("Centroid17", pos=[81.85142626081195,40.33100019182478,35.66942868913923])
cmd.color ("orange", "Centroid17")


cmd.select("Group18", "(resi 242-260 & chain F, resi 265-270 & chain F, resi 274-285 & chain F, resi 290-292 & chain F, )")
cmd.color ("yellow", "Group18")


cmd.pseudoatom ("Centroid18", pos=[73.80845003128051,55.05847520828247,22.347499775886536])
cmd.color ("yellow", "Centroid18")


cmd.select("Group19", "(resi 153-158 & chain G, resi 164-171 & chain G, )")
cmd.color ("green", "Group19")


cmd.pseudoatom ("Centroid19", pos=[68.81607110159737,18.71792847769601,25.607500212533132])
cmd.color ("green", "Centroid19")


cmd.select("Group20", "(resi 228-234 & chain G, )")
cmd.color ("cyan", "Group20")


cmd.pseudoatom ("Centroid20", pos=[78.63857051304409,15.913999966212682,38.80514308384487])
cmd.color ("cyan", "Centroid20")


cmd.select("Group21", "(resi 242-260 & chain G, resi 265-270 & chain G, resi 274-285 & chain G, resi 290-292 & chain G, )")
cmd.color ("blue", "Group21")


cmd.pseudoatom ("Centroid21", pos=[78.00662536621094,22.332299971580504,18.38227514848113])
cmd.color ("blue", "Centroid21")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
