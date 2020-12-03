from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3QQ2.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 748+749+750+751+752+753+754+755+756+757+758+759+760+761 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 996+997+998+999+1000+1001+1002+1003+1004+1005+1006+1007+1008 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 982+983+984+985+986+987+988+989+990+991+992+993 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 967+968+969+970+971+972+973+974+975+976+977+978 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 933+934+935+936+937+938+939+940+941+942+943+944+945+946+947 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 904+905+906+907+908+909+912+913+914+915+916+917+918+919+920+921+922+923+924+925+926+927+928 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 881+882+883+884+885+886+887+888+889+890+891+892+893+894+895+896+897+898+899 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 854+855+856+857+858+859+860+861+862+863+864+865+866+867+868+869+870+871+872+873+874+875+876 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 830+831+832+833+834+835+836+837+838+839+840+841+842+843+844+845+846+847+848 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 809+810+811+812+813+814+815+816+817+818+819+820+821+822+823+824+825+826 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 788+789+790+791+792+793+794+795+796+797+798+799+800+801+802+803+804+805 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 768+769+770+771+772+773+774+775+776+777+778+779+780+781+782+783+784+785 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
