from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6FOK.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 141+142+143+144+145+146+147+148+149+150+151 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 155+156+157+158+159+160+161+162+163+164+165+166 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 169+170+171+172+173+174+175+176+177+178+179+180 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 195+196+197+198+199+200+201+202+203+204+205+206 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 212+213+214+215+216+217+218+219+220+221+222+223+224+225 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 233+234+235+236+237+238+239+240+241+242+243+244+245+246+247+248+249 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 255+256+257+258+259+260+261+262+263+264+265+266+267+268+269+270+271+272 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 290+291+292+293+294+295+296+297+298+299+300+301+302+303+304+305+306+307+308 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 311+312+313+314+315+316+317+318+319+320+321+322+323+324+325+326+327+328+329+330+331+332 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 465+466+467+468+469+470+471+472+473+474+475+476+477 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 347+348+349+350+351+352+353+354+355+356+357+358+359+360+361+362+363 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 427+428+429+430+431+432+433+434+435+436+437+438 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 369+370+371+372+373+374+375+376+377+378+379+380+381+382+383+384 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 406+407+408+409+410+411+412+413+414+415+416+417+418+419+420+421 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 481+482+483+484+485+486+487+488+489+490+491+492+493+494+495+496+497+498+499+500+501 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 508+509+510+511+512+513+514+515+516+517+518+519+520+521+522+523+524+525+526+527+528 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 533+534+535+536+537+538+539+540+541+542+543+544+545+546 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 560+561+562+563+564+565+566+567+568+569 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 572+573+574+575+576+577+578+579+580+581 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 605+606+607+608+609+610+611+612+613+614+615 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 620+621+622+623+624+625+626+627 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 660+661+662+663+664+665+666+667+668 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
