from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2LME.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 52+53+54+55+56+57+58+59+60+61+62+63 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 94+95+96+97+98+99+100+101+102+103+104 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Cstrand2", "resi 52+53+54+55+56+57+58+59+60+61+62+63 & chain C ")
cmd.color ("orange", "Cstrand2")


cmd.select("Bstrand3", "resi 52+53+54+55+56+57+58+59+60+61+62+63 & chain B ")
cmd.color ("teal", "Bstrand3")


cmd.select("Cstrand4", "resi 66+67+68+69+70+71+72+73+74+75+76+77 & chain C ")
cmd.color ("yellow", "Cstrand4")


cmd.select("Cstrand5", "resi 84+85+86+87+88+89+90 & chain C ")
cmd.color ("blue", "Cstrand5")


cmd.select("Cstrand6", "resi 94+95+96+97+98+99+100+101+102+103+104 & chain C ")
cmd.color ("red", "Cstrand6")


cmd.select("Bstrand7", "resi 66+67+68+69+70+71+72+73+74+75+76+77 & chain B ")
cmd.color ("green", "Bstrand7")


cmd.select("Bstrand8", "resi 84+85+86+87+88+89+90 & chain B ")
cmd.color ("orange", "Bstrand8")


cmd.select("Bstrand9", "resi 94+95+96+97+98+99+100+101+102+103+104 & chain B ")
cmd.color ("teal", "Bstrand9")


cmd.select("Astrand10", "resi 84+85+86+87+88+89+90 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 66+67+68+69+70+71+72+73+74+75+76+77 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("barrel", "Astrand* or Cstrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
