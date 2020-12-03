from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5FQ8.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 49-51 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 122-123 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 138-139 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 221-223 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 248-250 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 317-320 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Bstrand6", "resi 44-48 & chain B ")
cmd.color ("red", "Bstrand6")


cmd.select("Bstrand7", "resi 71-75 & chain B ")
cmd.color ("green", "Bstrand7")


cmd.select("Bstrand8", "resi 84-88 & chain B ")
cmd.color ("orange", "Bstrand8")


cmd.select("Bstrand9", "resi 101-103 & chain B ")
cmd.color ("teal", "Bstrand9")


cmd.select("Bstrand10", "resi 113-115 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Bstrand11", "resi 125-128 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 138-144 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 161-166 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 177-188 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 201-202 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 205-206 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 222-229 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 232-237 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 252-264 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 268-280 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 289-303 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 306-320 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 376-394 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 398-417 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 446-469 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 472-495 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 513-534 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 538-549 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 558-569 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 582-596 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 607-614 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 617-620 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 629-631 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Bstrand34", "resi 634-635 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 643-656 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 661-673 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 676-680 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Bstrand38", "resi 689-693 & chain B ")
cmd.color ("orange", "Bstrand38")


cmd.select("Bstrand39", "resi 697-712 & chain B ")
cmd.color ("teal", "Bstrand39")


cmd.select("Bstrand40", "resi 716-731 & chain B ")
cmd.color ("yellow", "Bstrand40")


cmd.select("Bstrand41", "resi 741-746 & chain B ")
cmd.color ("blue", "Bstrand41")


cmd.select("Bstrand42", "resi 752-756 & chain B ")
cmd.color ("red", "Bstrand42")


cmd.select("Bstrand43", "resi 761-766 & chain B ")
cmd.color ("green", "Bstrand43")


cmd.select("Bstrand44", "resi 777-778 & chain B ")
cmd.color ("orange", "Bstrand44")


cmd.select("Bstrand45", "resi 793-794 & chain B ")
cmd.color ("teal", "Bstrand45")


cmd.select("Bstrand46", "resi 802-812 & chain B ")
cmd.color ("yellow", "Bstrand46")


cmd.select("Bstrand47", "resi 815-825 & chain B ")
cmd.color ("blue", "Bstrand47")


cmd.select("Bstrand48", "resi 828-831 & chain B ")
cmd.color ("red", "Bstrand48")


cmd.select("Bstrand49", "resi 859-865 & chain B ")
cmd.color ("green", "Bstrand49")


cmd.select("Bstrand50", "resi 868-873 & chain B ")
cmd.color ("orange", "Bstrand50")


cmd.select("Bstrand51", "resi 899-901 & chain B ")
cmd.color ("teal", "Bstrand51")


cmd.select("Bstrand52", "resi 904-915 & chain B ")
cmd.color ("yellow", "Bstrand52")


cmd.select("Bstrand53", "resi 928-941 & chain B ")
cmd.color ("blue", "Bstrand53")


cmd.select("Bstrand54", "resi 965-966 & chain B ")
cmd.color ("red", "Bstrand54")


cmd.select("Bstrand55", "resi 973-983 & chain B ")
cmd.color ("green", "Bstrand55")


cmd.select("Cstrand56", "resi 49-51 & chain C ")
cmd.color ("orange", "Cstrand56")


cmd.select("Cstrand57", "resi 122-123 & chain C ")
cmd.color ("teal", "Cstrand57")


cmd.select("Cstrand58", "resi 138-139 & chain C ")
cmd.color ("yellow", "Cstrand58")


cmd.select("Cstrand59", "resi 221-223 & chain C ")
cmd.color ("blue", "Cstrand59")


cmd.select("Cstrand60", "resi 248-250 & chain C ")
cmd.color ("red", "Cstrand60")


cmd.select("Cstrand61", "resi 317-320 & chain C ")
cmd.color ("green", "Cstrand61")


cmd.select("Dstrand62", "resi 44-48 & chain D ")
cmd.color ("orange", "Dstrand62")


cmd.select("Dstrand63", "resi 71-75 & chain D ")
cmd.color ("teal", "Dstrand63")


cmd.select("Dstrand64", "resi 84-88 & chain D ")
cmd.color ("yellow", "Dstrand64")


cmd.select("Dstrand65", "resi 101-104 & chain D ")
cmd.color ("blue", "Dstrand65")


cmd.select("Dstrand66", "resi 107-108 & chain D ")
cmd.color ("red", "Dstrand66")


cmd.select("Dstrand67", "resi 113-115 & chain D ")
cmd.color ("green", "Dstrand67")


cmd.select("Dstrand68", "resi 125-128 & chain D ")
cmd.color ("orange", "Dstrand68")


cmd.select("Dstrand69", "resi 138-144 & chain D ")
cmd.color ("teal", "Dstrand69")


cmd.select("Dstrand70", "resi 161-166 & chain D ")
cmd.color ("yellow", "Dstrand70")


cmd.select("Dstrand71", "resi 177-189 & chain D ")
cmd.color ("blue", "Dstrand71")


cmd.select("Dstrand72", "resi 201-202 & chain D ")
cmd.color ("red", "Dstrand72")


cmd.select("Dstrand73", "resi 205-206 & chain D ")
cmd.color ("green", "Dstrand73")


cmd.select("Dstrand74", "resi 222-225 & chain D ")
cmd.color ("orange", "Dstrand74")


cmd.select("Dstrand75", "resi 234-237 & chain D ")
cmd.color ("teal", "Dstrand75")


cmd.select("Dstrand76", "resi 252-264 & chain D ")
cmd.color ("yellow", "Dstrand76")


cmd.select("Dstrand77", "resi 268-280 & chain D ")
cmd.color ("blue", "Dstrand77")


cmd.select("Dstrand78", "resi 289-303 & chain D ")
cmd.color ("red", "Dstrand78")


cmd.select("Dstrand79", "resi 306-320 & chain D ")
cmd.color ("green", "Dstrand79")


cmd.select("Dstrand80", "resi 376-394 & chain D ")
cmd.color ("orange", "Dstrand80")


cmd.select("Dstrand81", "resi 398-417 & chain D ")
cmd.color ("teal", "Dstrand81")


cmd.select("Dstrand82", "resi 446-469 & chain D ")
cmd.color ("yellow", "Dstrand82")


cmd.select("Dstrand83", "resi 472-495 & chain D ")
cmd.color ("blue", "Dstrand83")


cmd.select("Dstrand84", "resi 513-534 & chain D ")
cmd.color ("red", "Dstrand84")


cmd.select("Dstrand85", "resi 538-549 & chain D ")
cmd.color ("green", "Dstrand85")


cmd.select("Dstrand86", "resi 558-569 & chain D ")
cmd.color ("orange", "Dstrand86")


cmd.select("Dstrand87", "resi 582-596 & chain D ")
cmd.color ("teal", "Dstrand87")


cmd.select("Dstrand88", "resi 607-614 & chain D ")
cmd.color ("yellow", "Dstrand88")


cmd.select("Dstrand89", "resi 617-620 & chain D ")
cmd.color ("blue", "Dstrand89")


cmd.select("Dstrand90", "resi 629-631 & chain D ")
cmd.color ("red", "Dstrand90")


cmd.select("Dstrand91", "resi 634-635 & chain D ")
cmd.color ("green", "Dstrand91")


cmd.select("Dstrand92", "resi 643-656 & chain D ")
cmd.color ("orange", "Dstrand92")


cmd.select("Dstrand93", "resi 661-673 & chain D ")
cmd.color ("teal", "Dstrand93")


cmd.select("Dstrand94", "resi 676-680 & chain D ")
cmd.color ("yellow", "Dstrand94")


cmd.select("Dstrand95", "resi 689-693 & chain D ")
cmd.color ("blue", "Dstrand95")


cmd.select("Dstrand96", "resi 697-712 & chain D ")
cmd.color ("red", "Dstrand96")


cmd.select("Dstrand97", "resi 717-731 & chain D ")
cmd.color ("green", "Dstrand97")


cmd.select("Dstrand98", "resi 741-746 & chain D ")
cmd.color ("orange", "Dstrand98")


cmd.select("Dstrand99", "resi 752-756 & chain D ")
cmd.color ("teal", "Dstrand99")


cmd.select("Dstrand100", "resi 763-765 & chain D ")
cmd.color ("yellow", "Dstrand100")


cmd.select("Dstrand101", "resi 794-797 & chain D ")
cmd.color ("blue", "Dstrand101")


cmd.select("Dstrand102", "resi 800-811 & chain D ")
cmd.color ("red", "Dstrand102")


cmd.select("Dstrand103", "resi 815-831 & chain D ")
cmd.color ("green", "Dstrand103")


cmd.select("Dstrand104", "resi 860-862 & chain D ")
cmd.color ("orange", "Dstrand104")


cmd.select("Dstrand105", "resi 871-873 & chain D ")
cmd.color ("teal", "Dstrand105")


cmd.select("Dstrand106", "resi 899-901 & chain D ")
cmd.color ("yellow", "Dstrand106")


cmd.select("Dstrand107", "resi 904-915 & chain D ")
cmd.color ("blue", "Dstrand107")


cmd.select("Dstrand108", "resi 928-941 & chain D ")
cmd.color ("red", "Dstrand108")


cmd.select("Dstrand109", "resi 965-966 & chain D ")
cmd.color ("green", "Dstrand109")


cmd.select("Dstrand110", "resi 972-983 & chain D ")
cmd.color ("orange", "Dstrand110")


cmd.select("Estrand111", "resi 17-27 & chain E ")
cmd.color ("teal", "Estrand111")


cmd.select("Estrand112", "resi 30-32 & chain E ")
cmd.color ("yellow", "Estrand112")


cmd.select("Estrand113", "resi 86-87 & chain E ")
cmd.color ("blue", "Estrand113")


cmd.select("Estrand114", "resi 94-108 & chain E ")
cmd.color ("red", "Estrand114")


cmd.select("Fstrand115", "resi 17-27 & chain F ")
cmd.color ("green", "Fstrand115")


cmd.select("Fstrand116", "resi 30-32 & chain F ")
cmd.color ("orange", "Fstrand116")


cmd.select("Fstrand117", "resi 86-87 & chain F ")
cmd.color ("teal", "Fstrand117")


cmd.select("Fstrand118", "resi 94-108 & chain F ")
cmd.color ("yellow", "Fstrand118")


cmd.select("Gstrand119", "resi 10-19 & chain G ")
cmd.color ("blue", "Gstrand119")


cmd.select("Gstrand120", "resi 24-27 & chain G ")
cmd.color ("red", "Gstrand120")


cmd.select("Gstrand121", "resi 38-42 & chain G ")
cmd.color ("green", "Gstrand121")


cmd.select("Gstrand122", "resi 45-46 & chain G ")
cmd.color ("orange", "Gstrand122")


cmd.select("Gstrand123", "resi 52-54 & chain G ")
cmd.color ("teal", "Gstrand123")


cmd.select("Gstrand124", "resi 63-72 & chain G ")
cmd.color ("yellow", "Gstrand124")


cmd.select("Gstrand125", "resi 78-87 & chain G ")
cmd.color ("blue", "Gstrand125")


cmd.select("Gstrand126", "resi 98-102 & chain G ")
cmd.color ("red", "Gstrand126")


cmd.select("Gstrand127", "resi 106-110 & chain G ")
cmd.color ("green", "Gstrand127")


cmd.select("Gstrand128", "resi 115-116 & chain G ")
cmd.color ("orange", "Gstrand128")


cmd.select("Gstrand129", "resi 120-125 & chain G ")
cmd.color ("teal", "Gstrand129")


cmd.select("Gstrand130", "resi 130-133 & chain G ")
cmd.color ("yellow", "Gstrand130")


cmd.select("Gstrand131", "resi 154-159 & chain G ")
cmd.color ("blue", "Gstrand131")


cmd.select("Gstrand132", "resi 165-171 & chain G ")
cmd.color ("red", "Gstrand132")


cmd.select("Gstrand133", "resi 181-187 & chain G ")
cmd.color ("green", "Gstrand133")


cmd.select("Gstrand134", "resi 193-200 & chain G ")
cmd.color ("orange", "Gstrand134")


cmd.select("Gstrand135", "resi 204-206 & chain G ")
cmd.color ("teal", "Gstrand135")


cmd.select("Gstrand136", "resi 209-211 & chain G ")
cmd.color ("yellow", "Gstrand136")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand* or Gstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
