from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1KMO.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 224+225+226+227+228+229+230+231+232+233 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 732+733+734+735+736+737+738+739+740 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 700+701+702+703+704+705+706 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 681+682+683+684+685+686+687+688+689+690+691 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 647+648+649+650+651+652+653+654+655+656 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 634+635+636+637+638+639+640+641+642 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 604+605+606+607+608+609+610+611+612+613+614+615+616+617 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 579+580+581+582+583+584+585+586+587+588+589+590+591+592+593 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 551+552+553+554+505+555+506+507+556+508+557+509+558+460+461+510+462+559+463+511+560+512+401+403+464+400+402+465+514+513+561+405+404+353+562+466+352+515+467+406+355+407+354+516+357+563+356+408+468+409+565+359+358+469+564+361+411+360+410+363+470+362+365+471+413+412+364+366+367+472+414+473+415+369+368+417+416+474+370+475+371+418+419+476+420+477+421+422+423 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 332+333+334+377+376+335+375+336+374+380+381+337+436+438+437+382+439+338+440+383+441+339+442+384+443+340+385+444+341+386+483+484+445+535+485+446+486+342+387+536+537+487+388+447+343+488+448+490+489+539+538+389+344+492+449+491+450+540+541+390+345+494+493+543+542+545+451+391+496+544+452+495+346+546+392+547+497+498+454+453+393+499+455+500+394+456+501+502+395+457+396+397 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 295+296+297+298+299+300+301+302+303+304+305+306+307+308+309 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 278+279+280+281+282+283+284+285+286+287+288+289 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 258+259+260+261+262+263+264+265+266+267+268+269 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 243+244+245+246+247+248+249+250+251+252+253 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
