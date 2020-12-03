from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3KVN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 347+347+348+349+350+351+352+353+354+355+356+357+358+359+360+369+370+371+372+373+374+375+376+377+378+379+380+381+382+383+388+389+390+391+392+393+394+395+396+397+398+399+400+401+402+403+408+409+410+411+412+413+414+415+416+417+418+419+420+421+422+423+424+425+428+429+430+431+432+433+434+435+436+437+438+439+440+441+442+443+444+445+446+447+448+449+450+453+454+455+456+457+458+459+460+461+462+463+464+465+466+467+468+469+470+471+472+473+474+484+485+486+487+488+489+490+491+492+493+494+495+496+497+498+499+517+518+519+520+521+522+523+524+525+526+527+528+529+530+531+532+533+538+539+540+541+542+543+544+545+546+547+548+549+579+580+581+582+583+584+585+586+587+588+589+590+591+592+595+596+597+598+599+600+601+602+603+604+605+606+609+610+611+612+613+614+615+616+617+618+619+620+621 & chain A")
cmd.load_cgo( [9.0, 34.66449,43.41144,43.536316, -40.25615, 43.411343, 13.167039, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
