from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4K3B.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 425+425+426+427+428+429+430+431+432+433+437+438+439+440+441+442+443+444+445+446+447+448+449+454+455+456+457+458+459+460+461+462+466+467+468+469+470+471+472+473+474+475+476+477+478+479+483+484+485+486+487+488+489+490+491+492+493+494+507+508+509+510+511+512+513+514+515+516+517+518+519+520+526+527+528+529+530+531+532+533+534+535+536+537+538+539+564+565+566+567+568+569+570+571+572+573+574+575+576+577+578+579+580+591+592+593+594+595+596+597+598+599+600+609+610+611+612+613+614+615+616+617+618+619+620+626+627+628+629+630+631+632+633+634+635+685+686+687+688+689+690+691+692+693+694+695+706+707+708+709+710+711+712+713+714+715+716+717+718+749+750+751+752+753+754+755+756+757+758+759+764+765+766+767+768+769+770+771+772+773+784+785+786+787+788+789 & chain A")
cmd.load_cgo( [9.0, -38.331543,-4.0679817,-5.593107, 6.3882313, 17.418457, -38.893112, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
