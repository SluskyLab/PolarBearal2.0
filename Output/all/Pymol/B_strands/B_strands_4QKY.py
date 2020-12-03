from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4QKY.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 212+213+214+215+216+217+218 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 227+228+229+230+231+232+233+234+235+236+237+238+239 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 546+547+548+549+550+551+552+553 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 522+523+524+525+526+527+528+529+530+531 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 504+505+506+507+508+509+510+511+512+513+514+515+516+517+518+519 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 418+419+420+421+422+423+424+425+426+427+428+429+430 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 488+489+490+491+492+493+494+495+496+497+498 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 402+403+404+405+406+407+408+409+410+411+412+413+414+415 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 458+459+460+461+462+463+464+465+466+467+468+469+470+471 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 369+370+371+372+373+374+375+376+377+378+379 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 355+356+357+358+359+360+361+362+363+364+365 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 324+325+326+327+328+329+330+331+332+333+334+335+336+337+338+339+340 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 303+304+305+306+307+308+309+310+311+312+313+314+315+316+317+318+319+320 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 279+280+281+282+283+284+285+286+287+288+289+290+291+292 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 264+265+266+267+268+269+270+271+272+273+274+275+276 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 247+248+249+250+251+252+253+254+255+256+257 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
