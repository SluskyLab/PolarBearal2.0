from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5IVA.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 51+52+53+54 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 567+568+569+570+571+572+573+574+575+576+577+578 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 74+75+76+77+78+79+80+81+82+83 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 553+554+555+556+557+558+559+560+561+562 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 89+90+91+92+93+94+95+96+97+98 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 538+539+540+541+542+543+544+545+546+547+548 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 508+509+510+511+512+513+514+515+516 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 475+476+477+478+479+480+481+482+483+484 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 463+464+465+466+467+468+469+470+471 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 416+417+418+419+420+421+422+423+424+425+426+427+428 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 346+347+348+349+350+351+352+353+354+355+356+357+358+359+360+361 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 399+400+401+402+403+404+405+406+407+408+409+410+411+412 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 321+322+323+324+325+326+327+328+329+330+331+332+333+334+335+336+337+338+339+340+341+342+343 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 286+287+288+289+290+291+292+293+294+295+296+297+298+299+300+301+302 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 267+268+269+270+271+272+273+274+275+276+277+278 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 225+226+227+228+229+230+231+232+233+234+235+236 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 206+207+208+209+210+211+212+213+214+215+216 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 185+186+187+188+189+190+191+192+193+194+195+196 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 171+172+173+174+175+176+177+178+179+180+181 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 489+490+491+492+493+494+495+496+497+498+499 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 142+143+144+145+146+147+148+149+150+151 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 126+127+128+129+130+131+132+133+134+135+136 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 101+102+103+104+105+106+107+108+109+110+111 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 602+603+604+605+606+607+608+609+610+611+612+613+614+615 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 583+584+585+586+587+588+589+590+591+592+593+594+595+596 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 60+61+62+63 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
