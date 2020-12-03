from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3IA8.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 18+19+20+21+22+26+27+28+29+30 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 33+34+35+36+37+38+39+40+41+42+43+44+45 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 150+151+152+153+154+155+156+157+158+159+160+161+162+163 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 139+140+141+142+143+144+145+146+147 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 124+125+126+127+128+129+130+131+132+133 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 105+106+107+108+109+110+111+112+113+114+115 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 93+94+95+96+97+98+99+100+101+102 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 82+83+84+85+86+87+88+89 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 66+67+68+69+70+71+72+73+74+75+76 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 51+52+53+54+55+56+57+58+59 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
