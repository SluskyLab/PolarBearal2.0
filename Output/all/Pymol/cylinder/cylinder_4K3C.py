from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4K3C.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 421+421+422+423+424+425+426+427+428+429+430+434+435+436+437+438+439+440+441+442+443+444+445+446+451+452+453+454+455+456+457+458+459+463+464+465+466+467+468+469+470+471+472+473+474+475+481+482+483+484+485+486+487+488+489+490+491+492+503+504+505+506+507+508+509+510+511+512+513+514+515+521+522+523+524+525+526+527+528+529+530+531+532+533+534+535+564+565+566+569+570+571+572+573+574+575+576+577+578+589+590+591+592+593+594+595+596+597+598+599+607+608+609+610+611+612+613+614+615+616+617+618+619+627+628+629+630+631+632+633+634+635+636+637+638+639+691+692+693+694+695+696+697+698+699+700+701+714+715+716+717+718+719+720+721+722+723+724+725+726+750+751+752+753+754+755+756+757+758+759+760+761+764+765+766+767+768+769+770+771+772+773+774+775+782+783+784+785+786+787+788+789+790+791+792 & chain A")
cmd.load_cgo( [9.0, -12.129558,-8.87452,-43.01337, 8.039969, 35.30513, -75.06113, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
