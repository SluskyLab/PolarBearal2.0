from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4EPA.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 140+141+142+143+144+145+146+147+148 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 152+153+154+155+156+157+158+159+160+161+162+163+164 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 168+169+170+171+172+173+174+175+176+177+178+179 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 196+197+198+199+200+201+202+203+204+205+206+207 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 214+215+216+217+218+219+220+221+222+223+224+225+226+227 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 253+254+255+256+257+258+259+260+261+262+263 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 273+274+275+276+277+278+279+280+281+282+283+284+285+286+287+288+289+290+291 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 294+295+296+297+300+301+302+303+304+305+306+307+308+309+310+311+312 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 320+321+322+323+324+325+326+327+328+329+330+331+332+333+334+335+336+337+338+339+340 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 345+346+347+348+349+350+351+352+353+354+355+356+357+358+359+360+361+362+363+364+365+366+367 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 372+373+374+375+376+377+378+379+380+381+382+383+384+385+386+387+388+389+390+391+392+393 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 396+397+398+399+400+401+402+403+404+405+406+407+408+409+410+411+412+413+414+415+416+417+418+419+420 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 454+455+456+457+458+459+460+461+462+463+464+465+466 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 423+424+425+426+427+428+429+430 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 470+471+472+473+474+475+476+477+478+479+480+481+482 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 501+502+503+504+505+506+507+508+509+510+511+512+513 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 520+521+522+523+524+525+526+527+528+529+530+531+532 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 550+551+552+553+554+555+556+557 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 567+568+569+570+571+572+573+574+575+576 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 592+593+594+595+596+597+598+599+600+601 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 607+608+609+610+611+612+613+614 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 641+642+643+644+645+646+647+648 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
