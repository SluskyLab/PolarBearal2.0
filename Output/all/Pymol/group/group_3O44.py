from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3O44.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 142-151 & chain A, resi 179-190 & chain A, resi 205-211 & chain A, resi 219-221 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[161.31131219863892,105.4056556224823,238.86768674850464])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 158-160 & chain A, resi 171-173 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[174.29299926757812,80.88933436075847,255.94466654459634])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 228-232 & chain A, resi 241-260 & chain A, resi 337-344 & chain A, resi 303-334 & chain A, resi 279-299 & chain A, resi 303-334 & chain B, resi 279-298 & chain B, resi 337-344 & chain B, resi 241-260 & chain B, resi 228-232 & chain B, resi 303-334 & chain C, resi 279-298 & chain C, resi 337-344 & chain C, resi 241-260 & chain C, resi 228-232 & chain C, resi 303-334 & chain D, resi 279-299 & chain D, resi 337-344 & chain D, resi 241-260 & chain D, resi 228-232 & chain D, resi 303-334 & chain E, resi 279-298 & chain E, resi 337-344 & chain E, resi 241-260 & chain E, resi 228-232 & chain E, resi 303-334 & chain F, resi 279-298 & chain F, resi 337-344 & chain F, resi 241-260 & chain F, resi 228-232 & chain F, resi 279-298 & chain G, resi 303-334 & chain G, resi 337-344 & chain G, resi 241-260 & chain G, resi 228-232 & chain G, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[151.72990625787222,63.079100511381576,217.63336690266928])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 266-271 & chain A, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[145.97733306884766,102.21883392333984,237.1943333943685])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 142-151 & chain B, resi 179-190 & chain B, resi 205-211 & chain B, resi 219-221 & chain B, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[133.02656197547913,104.27437472343445,234.56450033187866])
cmd.color ("yellow", "Centroid4")


cmd.select("Group5", "(resi 158-160 & chain B, resi 171-173 & chain B, )")
cmd.color ("green", "Group5")


cmd.pseudoatom ("Centroid5", pos=[133.18099975585938,81.56949996948242,257.9038314819336])
cmd.color ("green", "Centroid5")


cmd.select("Group6", "(resi 266-271 & chain B, )")
cmd.color ("cyan", "Group6")


cmd.pseudoatom ("Centroid6", pos=[125.38416544596355,98.10600026448567,222.2334976196289])
cmd.color ("cyan", "Centroid6")


cmd.select("Group7", "(resi 142-151 & chain C, resi 179-190 & chain C, resi 205-211 & chain C, resi 219-221 & chain C, )")
cmd.color ("blue", "Group7")


cmd.pseudoatom ("Centroid7", pos=[118.81578087806702,97.69128108024597,210.56784391403198])
cmd.color ("blue", "Centroid7")


cmd.select("Group8", "(resi 158-160 & chain C, resi 171-173 & chain C, )")
cmd.color ("purple", "Group8")


cmd.pseudoatom ("Centroid8", pos=[106.13866678873698,73.42683410644531,228.21016438802084])
cmd.color ("purple", "Centroid8")


cmd.select("Group9", "(resi 266-271 & chain C, )")
cmd.color ("red", "Group9")


cmd.pseudoatom ("Centroid9", pos=[124.5589993794759,91.25716654459636,197.39716593424478])
cmd.color ("red", "Centroid9")


cmd.select("Group10", "(resi 142-151 & chain D, resi 179-190 & chain D, resi 205-211 & chain D, resi 219-221 & chain D, )")
cmd.color ("orange", "Group10")


cmd.pseudoatom ("Centroid10", pos=[129.44843792915344,90.60209369659424,184.82756233215332])
cmd.color ("orange", "Centroid10")


cmd.select("Group11", "(resi 158-160 & chain D, resi 171-173 & chain D, )")
cmd.color ("yellow", "Group11")


cmd.pseudoatom ("Centroid11", pos=[113.53733444213867,62.47866694132487,188.9298324584961])
cmd.color ("yellow", "Centroid11")


cmd.select("Group12", "(resi 266-271 & chain D, )")
cmd.color ("green", "Group12")


cmd.pseudoatom ("Centroid12", pos=[144.35333251953125,86.94700113932292,181.2653325398763])
cmd.color ("green", "Centroid12")


cmd.select("Group13", "(resi 142-151 & chain E, resi 179-190 & chain E, resi 205-211 & chain E, resi 219-221 & chain E, )")
cmd.color ("cyan", "Group13")


cmd.pseudoatom ("Centroid13", pos=[156.8561863899231,88.5518753528595,176.83228158950806])
cmd.color ("cyan", "Centroid13")


cmd.select("Group14", "(resi 158-160 & chain E, resi 171-173 & chain E, )")
cmd.color ("blue", "Group14")


cmd.pseudoatom ("Centroid14", pos=[149.57633463541666,57.56866645812988,169.9636662801107])
cmd.color ("blue", "Centroid14")


cmd.select("Group15", "(resi 266-271 & chain E, )")
cmd.color ("purple", "Group15")


cmd.pseudoatom ("Centroid15", pos=[169.58666483561197,88.30499903361003,186.10616556803384])
cmd.color ("purple", "Centroid15")


cmd.select("Group16", "(resi 142-151 & chain F, resi 179-190 & chain F, resi 205-211 & chain F, resi 219-221 & chain F, )")
cmd.color ("red", "Group16")


cmd.pseudoatom ("Centroid16", pos=[180.41874980926514,92.7302188873291,192.55800008773804])
cmd.color ("red", "Centroid16")


cmd.select("Group17", "(resi 158-160 & chain F, resi 171-173 & chain F, )")
cmd.color ("orange", "Group17")


cmd.pseudoatom ("Centroid17", pos=[187.24100240071616,61.68299929300944,185.4663314819336])
cmd.color ("orange", "Centroid17")


cmd.select("Group18", "(resi 265-271 & chain F, )")
cmd.color ("yellow", "Group18")


cmd.pseudoatom ("Centroid18", pos=[182.7078574044364,94.89200047084263,207.9271458217076])
cmd.color ("yellow", "Centroid18")


cmd.select("Group19", "(resi 142-151 & chain G, resi 179-190 & chain G, resi 205-211 & chain G, resi 219-221 & chain G, )")
cmd.color ("green", "Group19")


cmd.pseudoatom ("Centroid19", pos=[182.36453104019165,100.21175050735474,220.2239990234375])
cmd.color ("green", "Centroid19")


cmd.select("Group20", "(resi 158-160 & chain G, resi 171-173 & chain G, )")
cmd.color ("cyan", "Group20")


cmd.pseudoatom ("Centroid20", pos=[198.2169977823893,71.99516677856445,223.87449900309244])
cmd.color ("cyan", "Centroid20")


cmd.select("Group21", "(resi 266-271 & chain G, )")
cmd.color ("blue", "Group21")


cmd.pseudoatom ("Centroid21", pos=[170.8748321533203,100.43583170572917,230.97733561197916])
cmd.color ("blue", "Centroid21")


cmd.select("Group22", "(resi 142-151 & chain H, resi 179-190 & chain H, resi 205-211 & chain H, resi 219-221 & chain H, )")
cmd.color ("purple", "Group22")


cmd.pseudoatom ("Centroid22", pos=[138.09715628623962,149.98443746566772,306.51909255981445])
cmd.color ("purple", "Centroid22")


cmd.select("Group23", "(resi 158-160 & chain H, resi 171-173 & chain H, )")
cmd.color ("red", "Group23")


cmd.pseudoatom ("Centroid23", pos=[109.65866597493489,165.78199768066406,305.04200236002606])
cmd.color ("red", "Centroid23")


cmd.select("Group24", "(resi 228-232 & chain H, resi 241-260 & chain H, resi 337-344 & chain H, resi 326-334 & chain H, )")
cmd.color ("orange", "Group24")


cmd.pseudoatom ("Centroid24", pos=[116.62683341616676,150.0633098057338,301.09825933547245])
cmd.color ("orange", "Centroid24")


cmd.select("Group25", "(resi 265-271 & chain H, )")
cmd.color ("yellow", "Group25")


cmd.pseudoatom ("Centroid25", pos=[138.37699672154017,139.28185817173548,295.0741402762277])
cmd.color ("yellow", "Centroid25")


cmd.select("Group26", "(resi 279-298 & chain H, resi 303-334 & chain I, resi 279-299 & chain I, resi 337-344 & chain I, resi 241-260 & chain I, resi 228-232 & chain I, resi 303-334 & chain J, resi 279-299 & chain J, resi 337-344 & chain J, resi 241-260 & chain J, resi 228-232 & chain J, resi 303-334 & chain K, resi 279-298 & chain K, resi 337-344 & chain K, resi 241-260 & chain K, resi 228-232 & chain K, resi 303-334 & chain L, resi 279-299 & chain L, resi 337-344 & chain L, resi 241-260 & chain L, resi 228-232 & chain L, resi 303-334 & chain M, resi 279-299 & chain M, resi 337-344 & chain M, resi 241-260 & chain M, resi 228-232 & chain M, resi 303-334 & chain N, resi 279-298 & chain N, resi 337-344 & chain N, resi 241-260 & chain N, resi 228-232 & chain N, )")
cmd.color ("green", "Group26")


cmd.pseudoatom ("Centroid26", pos=[100.47898311829299,116.83123995034435,313.54302972800724])
cmd.color ("green", "Centroid26")


cmd.select("Group27", "(resi 142-151 & chain I, resi 179-190 & chain I, resi 205-211 & chain I, resi 219-221 & chain I, )")
cmd.color ("cyan", "Group27")


cmd.pseudoatom ("Centroid27", pos=[141.81675124168396,128.6778120994568,287.6678714752197])
cmd.color ("cyan", "Centroid27")


cmd.select("Group28", "(resi 158-160 & chain I, resi 171-173 & chain I, )")
cmd.color ("blue", "Group28")


cmd.pseudoatom ("Centroid28", pos=[115.81166712443034,141.1356658935547,272.5363311767578])
cmd.color ("blue", "Centroid28")


cmd.select("Group29", "(resi 265-271 & chain I, )")
cmd.color ("purple", "Group29")


cmd.pseudoatom ("Centroid29", pos=[139.9258575439453,113.1481443132673,288.73057338169644])
cmd.color ("purple", "Centroid29")


cmd.select("Group30", "(resi 142-151 & chain J, resi 179-190 & chain J, resi 205-211 & chain J, resi 219-221 & chain J, )")
cmd.color ("red", "Group30")


cmd.pseudoatom ("Centroid30", pos=[141.3355631828308,100.52596831321716,292.43724822998047])
cmd.color ("red", "Centroid30")


cmd.select("Group31", "(resi 158-160 & chain J, resi 171-173 & chain J, )")
cmd.color ("orange", "Group31")


cmd.pseudoatom ("Centroid31", pos=[116.85299936930339,100.01533381144206,270.9718373616536])
cmd.color ("orange", "Centroid31")


cmd.select("Group32", "(resi 265-271 & chain J, )")
cmd.color ("yellow", "Group32")


cmd.pseudoatom ("Centroid32", pos=[137.14071437290735,92.00157274518695,304.90743146623885])
cmd.color ("yellow", "Centroid32")


cmd.select("Group33", "(resi 142-151 & chain K, resi 179-190 & chain K, resi 205-211 & chain K, resi 219-221 & chain K, )")
cmd.color ("green", "Group33")


cmd.pseudoatom ("Centroid33", pos=[136.7289056777954,86.76078176498413,317.219407081604])
cmd.color ("green", "Centroid33")


cmd.select("Group34", "(resi 158-160 & chain K, resi 171-173 & chain K, )")
cmd.color ("cyan", "Group34")


cmd.pseudoatom ("Centroid34", pos=[111.33766682942708,73.38133239746094,301.8246663411458])
cmd.color ("cyan", "Centroid34")


cmd.select("Group35", "(resi 266-271 & chain K, )")
cmd.color ("blue", "Group35")


cmd.pseudoatom ("Centroid35", pos=[131.25466664632162,92.73899968465169,330.7359975179036])
cmd.color ("blue", "Centroid35")


cmd.select("Group36", "(resi 142-151 & chain L, resi 179-190 & chain L, resi 205-211 & chain L, resi 219-221 & chain L, )")
cmd.color ("purple", "Group36")


cmd.pseudoatom ("Centroid36", pos=[131.49946856498718,97.61618733406067,343.2523441314697])
cmd.color ("purple", "Centroid36")


cmd.select("Group37", "(resi 158-160 & chain L, resi 171-173 & chain L, )")
cmd.color ("red", "Group37")


cmd.pseudoatom ("Centroid37", pos=[103.4509989420573,81.18250147501628,341.16200256347656])
cmd.color ("red", "Centroid37")


cmd.select("Group38", "(resi 265-271 & chain L, )")
cmd.color ("orange", "Group38")


cmd.pseudoatom ("Centroid38", pos=[128.3528551374163,112.11985669817243,348.2959987095424])
cmd.color ("orange", "Centroid38")


cmd.select("Group39", "(resi 142-151 & chain M, resi 179-190 & chain M, resi 205-211 & chain M, resi 219-221 & chain M, )")
cmd.color ("yellow", "Group39")


cmd.pseudoatom ("Centroid39", pos=[129.66543793678284,125.13856220245361,351.10493564605713])
cmd.color ("yellow", "Centroid39")


cmd.select("Group40", "(resi 158-160 & chain M, resi 171-173 & chain M, )")
cmd.color ("green", "Group40")


cmd.pseudoatom ("Centroid40", pos=[99.26016616821289,117.80250040690105,360.1413319905599])
cmd.color ("green", "Centroid40")


cmd.select("Group41", "(resi 265-271 & chain M, )")
cmd.color ("cyan", "Group41")


cmd.pseudoatom ("Centroid41", pos=[129.25757162911552,138.44928414481026,342.84071132114957])
cmd.color ("cyan", "Centroid41")


cmd.select("Group42", "(resi 142-151 & chain N, resi 179-190 & chain N, resi 205-211 & chain N, resi 219-221 & chain N, )")
cmd.color ("blue", "Group42")


cmd.pseudoatom ("Centroid42", pos=[132.70812487602234,148.31481266021729,334.70025062561035])
cmd.color ("blue", "Centroid42")


cmd.select("Group43", "(resi 158-160 & chain N, resi 171-173 & chain N, )")
cmd.color ("purple", "Group43")


cmd.pseudoatom ("Centroid43", pos=[102.29533386230469,155.39600118001303,343.97649637858075])
cmd.color ("purple", "Centroid43")


cmd.select("Group44", "(resi 266-271 & chain N, )")
cmd.color ("red", "Group44")


cmd.pseudoatom ("Centroid44", pos=[133.01283264160156,149.05416870117188,318.9586690266927])
cmd.color ("red", "Centroid44")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
