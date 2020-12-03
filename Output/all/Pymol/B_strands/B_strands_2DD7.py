from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2DD7.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 4+5+6+7+8+9+10+11+12+13+14 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 17+18+19+20+21+22+23+24+25+26+27+28 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 31+32+33+34+35+36+37+38 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 202+203+204+205+206+207+208+209+210+211+212 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 188+189+190+191+192+193+194+195+196+197+198 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 130+131+132+133+136+137+138+139+140+141+142+143 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 147+148+149+150+151+152+153+154+155+156+157+158 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 163+164+165+166+167+168+169+170+171+172+173+174 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 81+82+83+84+85+86+87+88+89 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 94+95+96+97+98+99+100+101+102+103+104 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 107+108+109+110+111+112+113+114+115+116+117 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
