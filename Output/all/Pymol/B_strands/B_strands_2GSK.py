from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2GSK.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 137+138+139+140+141+142+143+144+145 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 585+586+587+588+589+590+591+592+593 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 559+560+561+562+563+564+565+566 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 544+545+546+547+548+549+550+551+552+553+554 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 514+515+516+517+518+519+520+521+522+523 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 501+502+503+504+505+506+507+508+509+510+511 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 475+476+477+478+479+480+481+482+483+484+485+486+487+488 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 459+460+461+462+463+464+465+466+467+468+469+470+471+472 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 429+430+431+432+433+434+435+436+437+438+439+440+441 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 413+414+415+416+417+418+419+420+421+422+423+424+425+426 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 383+384+385+386+387+388+389+390+391+392+393+394 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 366+367+368+369+370+371+372+373+374+375+376+377+378+379+380 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 351+352+353+354+355+356+357+358+359+360+361+362 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 333+334+335+336+337+338+339+340+341+342+343+344+345+346+347+348 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 309+310+311+312+313+314+315+316+317+318+319+320+321+322 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 289+290+291+292+293+294+295+296+297+298+299+300+301+302+303+304+305 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 261+262+263+264+265+266+267+268+269+270+271+272+273+274+275+276+277 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 242+243+244+245+246+247+248+249+250+251+252+253+254+255+256+257 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 214+215+216+217+218+219+220+221+222+223+224+225+226+227+228 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 195+196+197+198+199+200+201+202+203+204+205+206+207+208+209 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 164+165+166+167+168+169+170+171+172+173+174+175+176+177+178 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 149+150+151+152+153+154+155+156+157+158+159+160+161 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
