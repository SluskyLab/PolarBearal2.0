

using System;
using System.Collections.Generic;
using System.IO;
using System.Numerics;
using System.Linq;
using betaBarrelProgram.BarrelStructures;

namespace betaBarrelProgram
{

    public class PolarBearal
    {
        //polarBearal Variable 
        public static string PolarBearal_OUTPUT_DIR = Global.OUTPUT_DIR + "PolarBearal/";
        public static string PolarBearal_INPUT_DB_FILE = Global.DB_file; //Global.POLARBEARAL_DIR + "/DB/MonoDB_v5.txt"; //Global.MONO_DB_file;

        double zone = 13;
        bool use_zone = true;// when true, only +-zone (a.k.a. membrane) is considered for (most?) outputs
        static public void menu()
        {
            Console.WriteLine("1. Generate empty result files");
            Console.WriteLine("2. Create Protein Database");
            Console.WriteLine("3. Run Protein Database");
            Console.WriteLine("4. ?");
            Console.WriteLine("10. Quit");
        }

        static public void RunPolarBearal()
        {
            PolarBearal_OUTPUT_DIR = Global.OUTPUT_DIR + "PolarBearal/";
            PolarBearal_INPUT_DB_FILE = Global.DB_file;

            string choice = "";
            while (choice != "10")
            {
                menu();
                choice = Console.ReadLine();
                switch (choice)
                {
                    case "1":
                        PrepResults();
                        break;
                    case "2":
                        using (StreamWriter log = File.AppendText(Global.OUTPUT_DIR + "log.txt"))
                        {
                            log.WriteLine("starting create betabarrel ProteinDB at {0}", DateTime.Now);
                            log.WriteLine("{0}\t{1}\t{2}\t{3}\t{4}", "PdbName", "Success", "barrelType", "chainID", "numberOfStrands");
                        }
                        CreateBetaBarrelProteinDatabase();
                        using (StreamWriter log = File.AppendText(Global.OUTPUT_DIR + "log.txt"))
                        {
                            log.WriteLine("ending create betabarrel ProteinDB at {0}", DateTime.Now);
                        }
                        break;
                    case "3":
                        RunBetaBarrelProteinDatabase();
                        Results();
                        break;
                    case "4":
                        break;
                    default:
                        choice = "10";
                        break;
                }
            }
        }

        static public void PrepResults()
        {
            string output_sub_dir;

            Console.WriteLine("Currently in {0}", System.IO.Directory.GetCurrentDirectory());
            Console.WriteLine("Output will be in {0}", PolarBearal_OUTPUT_DIR);

            Console.WriteLine("Would you like to delete all files currently in output dir (Y/N)?");
            string response = Console.ReadLine();
            if (response == "Y")
            {
                if (System.IO.Directory.Exists(PolarBearal_OUTPUT_DIR))
                {
                    System.IO.Directory.Delete(PolarBearal_OUTPUT_DIR, true);
                }
            }

            // build any needed paths for output
            if (!System.IO.Directory.Exists(PolarBearal_OUTPUT_DIR))
            {
                System.IO.Directory.CreateDirectory(PolarBearal_OUTPUT_DIR);
            }
            output_sub_dir = PolarBearal_OUTPUT_DIR + "betaBarrel_aaOnly";
            if (!System.IO.Directory.Exists(output_sub_dir))
            {
                System.IO.Directory.CreateDirectory(output_sub_dir);
            }
            output_sub_dir = PolarBearal_OUTPUT_DIR + "betaBarrelRawData";
            if (!System.IO.Directory.Exists(output_sub_dir))
            {
                System.IO.Directory.CreateDirectory(output_sub_dir);
            }
            output_sub_dir = PolarBearal_OUTPUT_DIR + "betaBarrelStrands";
            if (!System.IO.Directory.Exists(output_sub_dir))
            {
                System.IO.Directory.CreateDirectory(output_sub_dir);
            }

            //create (or recreate) blank result files with headers
            using (StreamWriter output = new System.IO.StreamWriter(PolarBearal_OUTPUT_DIR + "PolarBearalResults.txt")) { }
            using (System.IO.StreamWriter output = new System.IO.StreamWriter(PolarBearal_OUTPUT_DIR + "ExamineZ.txt")) { }
            using (System.IO.StreamWriter output = new System.IO.StreamWriter(PolarBearal_OUTPUT_DIR + "PinNoutByProtein.txt"))
            {
                output.Write("\n {0} \t {1} \t {2} \t {3} \t {4} \t {5}", "PDB", "AAs", "IN", "Pin", "OUT", "Nout");
            }
            using (System.IO.StreamWriter output = new System.IO.StreamWriter(PolarBearal_OUTPUT_DIR + "DisplayAngles.txt"))
            {
                output.Write("{0}\t{1}\t{2}", "aa", "angle", "inward facing");
            }
        }

       
        static public void CreateBetaBarrelProteinDatabase()
        {
            Dictionary<string, int> pdbBeta = new Dictionary<string, int>();

            string fileOfPDBs = PolarBearal_INPUT_DB_FILE;
            if (File.Exists(fileOfPDBs))
            {
                using (StreamReader sr = new StreamReader(fileOfPDBs))
                {
                    String line;
                    string fileLocation2 = PolarBearal_OUTPUT_DIR + "AllBarrelChar.txt";
                    using (System.IO.StreamWriter file = new System.IO.StreamWriter(fileLocation2))
                    {
                        string newLine = "PDB" + "\t\t" + "Total Strands" +"\t" + "Length" + "\t" + "AvgLength" + "\t" + "MinLength" + "\t" + "MaxLength" + "\t" + "Radius" + "\t" + "Barrel Tilt";
                        file.WriteLine(newLine);
                        // Read and display lines from the file until the end of the file is reached.
                        while ((line = sr.ReadLine()) != null)
                        {
                            string[] splitLine = line.Split(new char[] { ' ', '\t', ',' });
                            string pdb = splitLine[0];
                            //Console.Write(pdb);
                            if (pdb != "IDs")
                            {
                                string fileName = pdb;
                                //string fileName = pdb + ".pdb";
                                Barrel myBarrel = Program.runThisBetaBarrel(pdb, Global.METHOD);
                                
                                try
                                {
                                    SharedFunctions.LogBarrel(ref myBarrel, Global.METHOD);
                                    if (myBarrel.Success)
                                    {
                                        PolarBearal roar = new PolarBearal(ref myBarrel);

                                        string char1 = myBarrel.PdbName;
                                        string char2 = myBarrel.Axis.Length().ToString();
                                        string char7 = myBarrel.StrandLength.Average().ToString();
                                        string char8 = myBarrel.StrandLength.Min().ToString();
                                        string char9 = myBarrel.StrandLength.Max().ToString();
                                        string char3 = myBarrel.AvgRadius.ToString();
                                        string char4 = myBarrel.Strands.Count.ToString();
                                        string char5 = myBarrel.AvgTilt.ToString();
                                        string char6 = myBarrel.ShearNum.ToString();
                                        string char10 = "-999";// myBarrel.PrevTwists.Average().ToString();
                                        newLine = char1 + "\t" + char4 + "\t" + char2 + "\t" + char7 + "\t" + char8 + "\t" + char9 + "\t" + char3 + "\t" + char5 + "\t" + char6 + "\t" + char10;
                                        file.WriteLine(newLine);

                                        #region Amino Acid Pair
                                        try
                                        {
                                            SharedFunctions.AminoAcidPairs(myBarrel.Strands, Global.OUTPUT_DIR, Global.DB_DIR, myBarrel.PdbName);
                                        }
                                        catch (Exception exception)
                                        {
                                            Console.WriteLine("Failed to make pairs");
                                            string fileLocation3 = PolarBearal_OUTPUT_DIR + "AAPairErrorLog.txt";
                                            using (StreamWriter file3 = new StreamWriter(fileLocation3, append: true))
                                            {
                                                string newLine3 = myBarrel.PdbName + "\t" + exception.InnerException + exception.Message + "\t" + exception.StackTrace +  "\t" + exception.Source + "\t" + exception.Data + "\n";
                                                file3.WriteLine(newLine3);
                                            }
                                        }
                                        #endregion
                                    }
                                }
                                //Console.WriteLine("Number of Proteins: {0} \t AAs: {1} \t Double Checked Directions: {2}", totalProteins, totalAAs, numDoubleChecks);
                                catch
                                {
                                    Console.WriteLine("Failed polarbearel creation for {0}", pdb);
                                }
                            }
                        }
                    }
                }
                //Console.WriteLine("Number of Proteins: {0} \t AAs: {1} \t Double Checked Directions: {2}", totalProteins, totalAAs, numDoubleChecks);
            }
            else
            {
                Console.WriteLine("I am in {0}", System.IO.Directory.GetCurrentDirectory());
                Console.WriteLine("could not open {0}", fileOfPDBs);
                Console.ReadLine();

            }
        }

        static public void RunBetaBarrelProteinDatabase()
        {
            string fileOfPDBs = PolarBearal_INPUT_DB_FILE;

            if (File.Exists(fileOfPDBs))
            {
                using (StreamReader sr = new StreamReader(fileOfPDBs))
                {
                    String line;
                    while ((line = sr.ReadLine()) != null)
                    {
                        string[] splitLine = Array.FindAll<string>(((string)line).Split(
                            new char[] { ' ', '\t', ',' }), delegate (string s) { return !String.IsNullOrEmpty(s); });
                        string pdb = splitLine[0];
                        if (pdb != "IDs")
                        {
                            string fileName = pdb.ToUpper(); //RYANpdb.Substring(0, 4).ToUpper();

                            PolarBearal polarRetest = new PolarBearal(fileName);
                            try { 
                            
                            //PolarBearal polarRetest = new PolarBearal(fileName);
                            }
                            catch
                            {

                                Console.WriteLine("Failed to run polarbearal results for {0}", pdb);
                            }
                        }
                    }
                }
            }
            else
            {
                Console.WriteLine("could not open {0}", fileOfPDBs);
                Console.ReadLine();

            }
        }

        static public void Results()
        {
            string file = @"PolarBearalResults.txt";
            using (StreamWriter output = File.AppendText(PolarBearal_OUTPUT_DIR + file))
            {
                output.Write("\n\nProteins:\t{0} \t\t Chains:\t{1} \t\t AAs:\t{2}", PolarBearal._totalProteins, PolarBearal._totalChains, PolarBearal._totalAAs);

                output.Write("\n\nSequence Length: \t\t 1 \t 2 \t 3 \t 4 \t 5 \t 6 \t 7 \t 8 \t 9 \t 10 \t 11 \t 12 \t 13 \t 14 \t 15 \t 16 \t 17 \t 18");
                output.Write("\nTotals \t\t {0} \t {1} \t {2} \t {3} \t {4} \t {5} \t {6} \t {7} \t {8} \t {9} \t {10} \t {11} \t {12} \t {13} \t {14} \t {15} \t {16} \t {17}", PolarBearal._seqCount[1], PolarBearal._seqCount[2], PolarBearal._seqCount[3], PolarBearal._seqCount[4], PolarBearal._seqCount[5], PolarBearal._seqCount[6], PolarBearal._seqCount[7], PolarBearal._seqCount[8], PolarBearal.seqCount[9], PolarBearal._seqCount[10], PolarBearal._seqCount[11], PolarBearal._seqCount[12], PolarBearal._seqCount[13], PolarBearal._seqCount[14], PolarBearal._seqCount[15], PolarBearal._seqCount[16], PolarBearal._seqCount[17], PolarBearal._seqCount[18]);
                output.Write("\n\n\n");

                int num = 0;
                output.Write("Strand Sizes:\n");
                foreach (int i in PolarBearal._strandSizes) output.Write("{0}\t", num++);
                output.Write("\n");
                foreach (int i in PolarBearal._strandSizes) output.Write("{0}\t", i);
                output.Write("\n\n\n");

                num = 0;
                output.Write("Alternating Sequence Sizes:\n");
                foreach (int i in PolarBearal._AlternatingInOutSeqLengths) output.Write("{0}\t", num++);
                output.Write("\n");
                foreach (int i in PolarBearal._AlternatingInOutSeqLengths) output.Write("{0}\t", i);

                output.Write("\n\n");
                output.Write("\n\t\tL \tW \tP \tV \tI \tF \tY \tH \tA \tM \tG \tT \tQ \tD \tN \tK \tS \tR \tE \tC");
                output.Write("\n\t");
                foreach (int i in __aa) output.Write("{0}\t", i);
                output.Write("\n\t");
                foreach (int i in _aaInward) output.Write("{0}\t", i);
                output.Write("\n\t");
                foreach (int i in _aaOutward) output.Write("{0}\t", i);
                output.Write("\n\n\t");
                foreach (int i in _aaDevInward) output.Write("{0}\t", i);
                output.Write("\n\t");
                foreach (int i in _aaDevOutward) output.Write("{0}\t", i);


                output.Write("\n\n");
                output.Write("\n\t\tL \tW \tP \tV \tI \tF \tY \tH \tA \tM \tG \tT \tQ \tD \tN \tK \tS \tR \tE \tC");
                output.Write("\n");
                output.Write("aa\t");
                foreach (int i in __aa) output.Write("{0}\t", i);
                output.Write("\n\n");
                output.Write("aap1\t");
                foreach (int i in _aap1) output.Write("{0}\t", i);
                output.Write("\n");
                output.Write("aap2\t");
                foreach (int i in _aap2) output.Write("{0}\t", i);
                output.Write("\n");
                output.Write("aax3\t");
                foreach (int i in _aan3) output.Write("{0}\t", i);
                output.Write("\n\n");
                output.Write("aan1\t");
                foreach (int i in _aan1) output.Write("{0}\t", i);
                output.Write("\n");
                output.Write("aan2\t");
                foreach (int i in _aan2) output.Write("{0}\t", i);
                output.Write("\n");
                output.Write("aax3\t");
                foreach (int i in _aap3) output.Write("{0}\t", i);
                output.Write("\n");



            }

            file = @"ExamineZ.txt";
            using (StreamWriter output = File.AppendText(PolarBearal_OUTPUT_DIR + file))
            {
                for (int i = 0; i < examineZP.Length; i++)
                    output.Write("\n{0}\t{1}\t{2}\t{3}", _ZP[i], _ZN[i], _examineZP[i], _examineZN[i]);
            }



        }


        //Constructor 
        //uses a previously extracted barrel data to create a quick model of a barrel
        public PolarBearal(string PDBid)
        {
            try
            { 
                largestAltSeq = 0;
                proteinID = PDBid;
                totalProteins++;

                string file = @"betaBarrel_aaOnly/" + PDBid + ".txt";
                string[] FindChains = File.ReadAllLines(PolarBearal_OUTPUT_DIR + file);
                numChains = FindChains.Length;

                simpleBarrel = new aa[numChains][];
                Queue<aa> chain = new Queue<aa>();
                file = @"betaBarrelRawData/" + PDBid + ".txt";
                string[] BarrelChains = File.ReadAllLines(PolarBearal_OUTPUT_DIR + file);

                int curChain = 0;
                char[] delPunc = { ':', ',' };
                foreach (string amino in BarrelChains)
                {
                    string[] preaa = amino.Split(delPunc);

                    if (preaa[0] != curChain.ToString())
                    {
                        simpleBarrel[curChain] = chain.ToArray();
                        chain.Clear();
                        curChain++;
                    }

                    aa tempaa = new aa(preaa[1]);

                    if (preaa[2] == "True")
                    {
                        tempaa.Inward = true;
                    }
                    else
                    {
                        tempaa.Inward = false;
                    }

                    tempaa.ResNum = Convert.ToInt16(preaa[3]);
                    tempaa.SeqID = Convert.ToInt16(preaa[4]);
                    tempaa.height = Double.Parse(preaa[5]);

                    tempaa.angle = Double.Parse(preaa[6]);
                    //Console.Write(preaa[0] + ":" + preaa[1] + "," + preaa[2] + "," + preaa[3] + "," + preaa[4] + "\n");
                    if (use_zone)
                    {
                        if (tempaa.height > -zone && tempaa.height < zone)
                        {
                            chain.Enqueue(tempaa);
                            file = @"DisplayAngles.txt";
                            using (StreamWriter output = File.AppendText(PolarBearal_OUTPUT_DIR + file))
                            {
                                output.Write("\n{0}\t{1}\t{2}", tempaa.m_aa_ID, tempaa.angle, tempaa.Inward);
                            }
                        }
                    }
                    else
                    {
                        chain.Enqueue(tempaa);
                        file = @"DisplayAngles.txt";
                        using (StreamWriter output = File.AppendText(PolarBearal_OUTPUT_DIR + file))
                        {
                            output.Write("\n{0}\t{1}\t{2}", tempaa.m_aa_ID, tempaa.angle, tempaa.Inward);
                        }
                    }
                }

                simpleBarrel[curChain] = chain.ToArray();
                seperatedBarrel = new Queue<aa[][]>();
                SeperateBarrel();

                if (use_zone) { printZ(); }
                PolarBearalCalculations();
                PinNoutByProtein();
                //update all db counts since attempt has successfullly completed
                _totalProteins = totalProteins;
                _totalChains = totalChains;
                _totalAAs = totalAAs;
                _seqCount = seqCount;
                _strandSizes = strandSizes;
                _AlternatingInOutSeqLengths = AlternatingInOutSeqLengths;
                __aa = _aa;
                _aaInward = aaInward;
                _aaDevInward = aaDevInward;
                _aaOutward = aaOutward;
                _aaDevOutward = aaDevOutward;
                _aap1 = aap1;
                _aap2 = aap2;
                _aap3 = aap3;
                _aan1 = aan1;
                _aan2 = aan2;
                _aan3 = aan3;
                _ZP = ZP;
                _ZN = ZN;
                _examineZP = examineZP;
                _examineZN = examineZN;

            }
            catch
            {
                //revert all db counts to what they were at the end of last successful attempt
                totalProteins = _totalProteins;
                totalChains = _totalChains;
                totalAAs = _totalAAs;
                seqCount = _seqCount;
                strandSizes = _strandSizes;
                AlternatingInOutSeqLengths = _AlternatingInOutSeqLengths;
                _aa = __aa;
                aaInward = _aaInward;
                aaDevInward = _aaDevInward;
                aaOutward = _aaOutward;
                aaDevOutward = _aaDevOutward;
                aap1 = _aap1;
                aap2 = _aap2;
                aap3 = _aap3;
                aan1 = _aan1;
                aan2 = _aan2;
                aan3 = _aan3;
                ZP = _ZP;
                ZN = _ZN;
                examineZP = _examineZP;
                examineZN = _examineZN;
            }

        }

        //Constructor 
        //uses xml and the rest of the program to discover a barrel
        //extracts important data and add it to file for quicker extraction in future program runs
        public PolarBearal(ref Barrel myBarrel)
        {
            numChains = myBarrel.Strands.Count;
            proteinID = myBarrel.PdbName;
            largestAltSeq = 0;
            totalProteins++;

            //2D array to store data;[chain number] [amino acid number]
            simpleBarrel = new aa[numChains][];

            //create simple barrel
            for (int curChain = 0; curChain < numChains; curChain++)
            {
                simpleBarrel[curChain] = new aa[myBarrel.Strands[curChain].NumOfRes + 1];
                //add aa
                for (int cur_aa = 0; cur_aa <= myBarrel.Strands[curChain].NumOfRes; cur_aa++)
                {
                    //add aa member variables here
                    simpleBarrel[curChain][cur_aa] = new aa(myBarrel.Strands[curChain].Residues[cur_aa].OneLetCode);
                    simpleBarrel[curChain][cur_aa].Inward = myBarrel.Strands[curChain].Residues[cur_aa].Inward;
                    simpleBarrel[curChain][cur_aa].ResNum = myBarrel.Strands[curChain].Residues[cur_aa].ResNum;
                    simpleBarrel[curChain][cur_aa].SeqID = myBarrel.Strands[curChain].Residues[cur_aa].SeqID;
                    simpleBarrel[curChain][cur_aa].X = myBarrel.Strands[curChain].Residues[cur_aa].BackboneCoords["CA"].X;
                    simpleBarrel[curChain][cur_aa].Y = myBarrel.Strands[curChain].Residues[cur_aa].BackboneCoords["CA"].Y;
                    simpleBarrel[curChain][cur_aa].height = myBarrel.Strands[curChain].Residues[cur_aa].BackboneCoords["CA"].Z;

                    simpleBarrel[curChain][cur_aa].angle = SharedFunctions.AngleBetween(myBarrel.Strands[curChain].Residues[cur_aa].BackboneCoords["CA"] - ((myBarrel.Strands[curChain].Residues[cur_aa].BackboneCoords["N"] + myBarrel.Strands[curChain].Residues[cur_aa].BackboneCoords["C"]) / 2), myBarrel.Axis);

                }
            }

            string file = @"betaBarrel_aaOnly/" + proteinID + ".txt";
            using (System.IO.StreamWriter output = new System.IO.StreamWriter(PolarBearal_OUTPUT_DIR + file))
            {
                for (int curChain = 0; curChain < simpleBarrel.GetLength(0); curChain++)
                {
                    //add aa
                    for (int cur_aa = 0; cur_aa < simpleBarrel[curChain].Length; cur_aa++)
                    {
                        output.Write(" {0} ", simpleBarrel[curChain][cur_aa].m_aa_ID);
                    }
                    output.WriteLine();
                }
            }

            file = @"betaBarrelRawData/" + proteinID + ".txt";
            using (System.IO.StreamWriter output = new System.IO.StreamWriter(PolarBearal_OUTPUT_DIR + file))
            {
                for (int curChain = 0; curChain < simpleBarrel.GetLength(0); curChain++)
                {
                    //add aa
                    for (int cur_aa = 0; cur_aa < simpleBarrel[curChain].Length; cur_aa++)
                    {
                        output.WriteLine("{0}:{1},{2},{3},{4},{5},{6}", curChain, simpleBarrel[curChain][cur_aa].m_aa_ID, simpleBarrel[curChain][cur_aa].Inward, simpleBarrel[curChain][cur_aa].ResNum, simpleBarrel[curChain][cur_aa].SeqID, simpleBarrel[curChain][cur_aa].height, simpleBarrel[curChain][cur_aa].angle);
                    }
                }
            }


            string _pdb;
            int _pdb_strands;
            string _res;
            int _res_num, _seqID;
            int _res_strand;
            double _res_ca_x;
            double _res_ca_y;
            double _res_ca_z;
            bool _inward;
            double _angle;

            file = @"betaBarrelStrands/" + proteinID + ".txt";
            using (System.IO.StreamWriter output = new System.IO.StreamWriter(PolarBearal_OUTPUT_DIR + file))
            {
                output.WriteLine("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}", "_pdb", "_pdb_strands", "_res", "_res_num", "_seqID", "_res_strand", "_res_ca_x", "_res_ca_y", "_res_ca_z", "_inward", "_angle");
                for (int curChain = 0; curChain < simpleBarrel.GetLength(0); curChain++)
                {
                    //add aa
                    for (int cur_aa = 0; cur_aa < simpleBarrel[curChain].Length; cur_aa++)
                    {
                        _pdb = proteinID;
                        _pdb_strands = simpleBarrel.GetLength(0);
                        _res = simpleBarrel[curChain][cur_aa].m_aa_ID;
                        _res_num = simpleBarrel[curChain][cur_aa].ResNum + 1;
                        _seqID = simpleBarrel[curChain][cur_aa].SeqID;
                        _res_strand = curChain + 1;
                        _res_ca_x = simpleBarrel[curChain][cur_aa].X;
                        _res_ca_y = simpleBarrel[curChain][cur_aa].Y;
                        _res_ca_z = simpleBarrel[curChain][cur_aa].height;
                        _inward = simpleBarrel[curChain][cur_aa].Inward;
                        _angle = simpleBarrel[curChain][cur_aa].angle;

                        output.WriteLine("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}", _pdb, _pdb_strands, _res, _res_num, _seqID, _res_strand, _res_ca_x, _res_ca_y, _res_ca_z, _inward, _angle);
                    }
                }
            }
        }


        //breaks a strand into substrands
        public void SeperateBarrel()
        {
            Queue<aa[]> seperatedChain = new Queue<aa[]>();
            int subChainCounter = 0;
            Queue<aa> subChain = new Queue<aa>();
            aa[] chain;

            for (int curChain = 0; curChain < numChains; curChain++)
            {
                chain = simpleBarrel[curChain];

                //break apart chain
                for (int cur_aa = 0; cur_aa < chain.Length; cur_aa++)
                {
                    if (subChain.Count == 0)
                    {
                        subChain.Enqueue(chain[cur_aa]);
                    }
                    else if (!alternating_aa(chain[cur_aa - 1], chain[cur_aa]))
                    {
                        //check for an increased largest chain count
                        if (subChain.Count > largestAltSeq) largestAltSeq = subChain.Count;

                        aa[] subChain_aa = new aa[subChain.Count];
                        subChainCounter = 0;
                        foreach (aa number in subChain)
                        {
                            subChain_aa[subChainCounter++] = number;
                        }

                        subChain.Clear();
                        subChain.Enqueue(chain[cur_aa]);

                        seperatedChain.Enqueue(subChain_aa);
                    }
                    else
                    {
                        subChain.Enqueue(chain[cur_aa]);
                    }
                }
                //adds last chain if it ended with alternating sequances
                if (subChain.Count > 0)
                {
                    if (subChain.Count > largestAltSeq) largestAltSeq = subChain.Count;

                    aa[] subChain_aa = new aa[subChain.Count];
                    subChainCounter = 0;
                    foreach (aa number in subChain)
                    {
                        subChain_aa[subChainCounter++] = number;
                    }
                    subChain.Clear();
                    seperatedChain.Enqueue(subChain_aa);
                }


                aa[][] newChain = new aa[seperatedChain.Count][];
                for (int curSubChain = 0; 0 < seperatedChain.Count; curSubChain++)
                {
                    newChain[curSubChain] = seperatedChain.Dequeue();
                }

                seperatedBarrel.Enqueue(newChain);
            }
        }

        //determines if two given AA are PtoN or NtoP
        private bool alternating_aa(aa prevAA, aa curAA)
        {
            if (prevAA != null && curAA != null)
            {
                if ('P' == prevAA.mPolarity || prevAA.mPolarity == 'Q')
                {
                    if ('N' == curAA.mPolarity || curAA.mPolarity == 'Q') return (true);
                    else return (false);
                }
                else if ('N' == prevAA.mPolarity || prevAA.mPolarity == 'Q')
                {
                    if ('P' == curAA.mPolarity || curAA.mPolarity == 'Q') return (true);
                    else return (false);
                }
                else//no other way to be alternating
                {
                    return (false);
                }
            }
            return (false);
        }


        //Displays IN, Pin, OUT, Nout for each protein
        public void PinNoutByProtein()
        {
            int AAs = 0, Pin = 0, Nout = 0, IN = 0, OUT = 0;

            foreach (aa[] strand in this.simpleBarrel)
            {
                foreach (aa amino in strand)
                {
                    AAs++;

                    if (amino.Inward)
                    {
                        IN++;
                        if (amino.mPolarity == 'P' || amino.mPolarity == 'Q') Pin++;
                    }

                    if (!amino.Inward)
                    {
                        OUT++;
                        if (amino.mPolarity == 'N' || amino.mPolarity == 'Q') Nout++;
                    }
                }
            }

            string file = @"PinNoutByProtein.txt";
            using (System.IO.StreamWriter output = File.AppendText(PolarBearal_OUTPUT_DIR + file))
            {
                output.Write("\n {0} \t {1} \t {2} \t {3} \t {4} \t {5}", proteinID, AAs, IN, Pin, OUT, Nout);
            }
        }

        //For normal calculations
        public void PolarBearalCalculations()
        {
            totalChains += simpleBarrel.Count();
            for (int i = 0; i < simpleBarrel.Length; i++)
            {
                strandSizes[simpleBarrel[i].Length]++;
            }

            foreach (aa[] strand in simpleBarrel)
            {
                foreach (aa amino in strand)
                {
                    _aa[IntOfeRes(amino.m_aa_ID)]++;
                    if (amino.Inward) aaInward[IntOfeRes(amino.m_aa_ID)]++;
                    else aaOutward[IntOfeRes(amino.m_aa_ID)]++;
                }
            }

            //numbers to make a graph of occurances by chain length
            int[] OcurrancesPerLengthOfAltSeq = new int[largestAltSeq + 1];

            aa[][] temp2D_aa;
            int tempLength;
            for (int curChain = 0; curChain < numChains; curChain++)
            {
                temp2D_aa = seperatedBarrel.Dequeue();
                for (int curSubChain = 0; curSubChain < temp2D_aa.Length; curSubChain++)
                {
                    tempLength = temp2D_aa[curSubChain].Length;
                    OcurrancesPerLengthOfAltSeq[tempLength]++;
                    seqCount[tempLength]++;
                }
                seperatedBarrel.Enqueue(temp2D_aa);
            }

            string file = @"PolarBearalGraphOccurances.txt";
            using (StreamWriter sw = File.AppendText(PolarBearal_OUTPUT_DIR + file))
            {
                sw.Write("{0} \t", proteinID);
                foreach (int occurances in OcurrancesPerLengthOfAltSeq)
                {
                    sw.Write("\t {0}", occurances);
                }
                sw.Write("\n");
            }

            AlternatingFacing();
        }

        //converts amino acid 1 letter ID into associated interger
        public int IntOfeRes(string aa)
        {
            switch (aa)
            {
                case "L":
                    return (1);
                case "W":
                    return (2);
                case "P":
                    return (3);
                case "V":
                    return (4);
                case "I":
                    return (5);
                case "F":
                    return (6);
                case "Y":
                    return (7);
                case "H":
                    return (8);
                case "A":
                    return (9);
                case "M":
                    return (10);
                case "G":
                    return (11);
                case "T":
                    return (12);
                case "Q":
                    return (13);
                case "D":
                    return (14);
                case "N":
                    return (15);
                case "K":
                    return (16);
                case "S":
                    return (17);
                case "R":
                    return (18);
                case "E":
                    return (19);
                case "C":
                    return (20);
                default:
                    return (0);
            }
        }

        //use to examine specific values at different Zs
        public void printZ()
        {
            foreach (aa[] strand in simpleBarrel)
            {
                bool first = true;
                aa previousAA = strand[0];
                int strandNum = 0;
                foreach (aa amino in strand)
                {
                    if (!first)
                    {
                        if (amino.height > -zone && amino.height < zone && previousAA.height > -zone && previousAA.height < zone)
                        {
                            if (amino.mPolarity == 'P' || amino.mPolarity == 'Q') ZP[(int)Math.Floor(amino.height) + Convert.ToInt16(zone)]++;
                            if (amino.mPolarity == 'N' || amino.mPolarity == 'Q') ZN[(int)Math.Floor(amino.height) + Convert.ToInt16(zone)]++;

                            if (amino.mPolarity == 'P' && previousAA.mPolarity == 'P')// || previousAA.mPolarity == 'Q' || amino.mPolarity == 'Q')
                            {
                                examineZP[(int)Math.Floor(amino.height) + Convert.ToInt16(zone)]++;
                            }
                            else if (amino.mPolarity == 'N' && previousAA.mPolarity == 'N')// || previousAA.mPolarity == 'Q' || amino.mPolarity == 'Q')
                            {
                                examineZN[(int)Math.Floor(amino.height) + Convert.ToInt16(zone)]++;
                            }
                            else { }


                        }
                        strandNum++;
                    }
                    first = false;
                    previousAA = amino;
                }
            }
        }

        public void angleBreakDown()
        {
            //foreach()
        }
        //Examine Alternating Directionality
        void AlternatingFacing()
        {
            bool prevAAInward = true;
            double prevAAHeight = 0.0;
            char prevAAPol = 'P';
            int aaCount, seqCount, seqCount2;
            aa aa1_PreDev = new aa("A"), aa2_Dev = new aa("A"), aa3_PostDev = new aa("A");
            foreach (aa[] strand in this.simpleBarrel)
            {
                aaCount = 0;
                seqCount = 0;
                seqCount2 = 0;
                bool range = false;
                foreach (aa amino in strand)
                {
                    if (!use_zone || (amino.height > -zone && amino.height < zone) )
                    {
                        totalAAs++;
                        range = true;
                        if (aaCount > 0)
                        {
                            //totalAAs++;
                            if (seqCount == 0)
                            {
                                seqCount++;
                            }
                            else
                            {
                                if (amino.Inward != prevAAInward) seqCount++;
                                else
                                {
                                    AlternatingInOutSeqLengths[seqCount]++;
                                    if (seqCount != 1)
                                    {
                                        if (amino.Inward && prevAAInward) aaDevInward[IntOfeRes(amino.m_aa_ID)]++;
                                        else if (!amino.Inward && !prevAAInward) aaDevOutward[IntOfeRes(amino.m_aa_ID)]++;
                                    }
                                    seqCount = 1;
                                }



                                if (seqCount2 == 0)
                                {
                                    seqCount2++;
                                    aa3_PostDev = amino;
                                }
                                else if (seqCount2 == 1)
                                {
                                    seqCount2++;
                                    aa2_Dev = aa3_PostDev;
                                    aa3_PostDev = amino;
                                }
                                else
                                {
                                    seqCount2++;
                                    aa1_PreDev = aa2_Dev;
                                    aa2_Dev = aa3_PostDev;
                                    aa3_PostDev = amino;

                                    if (aa1_PreDev.mPolarity == 'P' && aa2_Dev.mPolarity == 'P')
                                    {
                                        aap1[IntOfeRes(aa1_PreDev.m_aa_ID)]++;
                                        aap2[IntOfeRes(aa2_Dev.m_aa_ID)]++;
                                        aan3[IntOfeRes(aa3_PostDev.m_aa_ID)]++;
                                    }

                                    if (aa1_PreDev.mPolarity == 'N' && aa2_Dev.mPolarity == 'N')
                                    {
                                        aan1[IntOfeRes(aa1_PreDev.m_aa_ID)]++;
                                        aan2[IntOfeRes(aa2_Dev.m_aa_ID)]++;
                                        aap3[IntOfeRes(aa3_PostDev.m_aa_ID)]++;
                                    }
                                }
                            }
                        }
                        else if (use_zone){ seqCount++;}
                    }


                    prevAAInward = amino.Inward;
                    prevAAHeight = amino.height;
                    prevAAPol = amino.mPolarity;
                    aaCount++;
                }
                if (aa3_PostDev.mPolarity == 'P' && aa2_Dev.mPolarity == 'P')
                {
                    aap1[IntOfeRes(aa2_Dev.m_aa_ID)]++;
                    aap2[IntOfeRes(aa3_PostDev.m_aa_ID)]++;
                    aan3[21]++;
                }

                if (aa3_PostDev.mPolarity == 'N' && aa2_Dev.mPolarity == 'N')
                {
                    aan1[IntOfeRes(aa2_Dev.m_aa_ID)]++;
                    aan2[IntOfeRes(aa3_PostDev.m_aa_ID)]++;
                    aap3[21]++;
                }
                if (range) AlternatingInOutSeqLengths[seqCount]++;
            }
        }

        //member class aa
        class aa
        {
            //contructors
            public aa(string aa_ID)
            {
                m_aa_ID = aa_ID;
                mPolarity = 'U';
                assignPolarity();
                Inward = false;
                ResNum = -100;
                SeqID = -100;
                height = -100;
            }

            //assigns polarity from amino acid ID
            public void assignPolarity()
            {
                string ID = this.m_aa_ID;

                if (P.Contains(ID))
                {
                    mPolarity = 'P';
                }
                else if (N.Contains(ID))
                {
                    mPolarity = 'N';
                }
                else
                {
                    mPolarity = 'Q';
                }
            }

            //member variables
            public string m_aa_ID;//stores amino acid's 3 letter abreviation
            public char mPolarity;//should be P,N, or U(represent unassigned polarity}
            public bool Inward;//is true if amino acid is facing inward, false if facing outward
            public int ResNum;//residue number in protein
            public int SeqID;//residue sequence position (includes unresolved residues and may not start at 1)
            public double X;//height along z axis
            public double Y;//height along z axis
            public double height;//height along z axis
            public double angle;
        }


        //member variables
        string proteinID;
        aa[][] simpleBarrel;
        Queue<aa[][]> seperatedBarrel;
        int numChains, largestAltSeq;
        // probably a better way to do this, but i duplicated all the following variables so that they
        // can be reverted to previous successful attempt should current attempt fail (so only working barrels in db are counted)
        public static int totalProteins = 0, totalChains = 0, totalAAs = 0;
        public static int _totalProteins = 0, _totalChains = 0, _totalAAs = 0;

        public static int[] seqCount = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
        public static int[] _seqCount = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
        public static string P = "DEKNQRSTCH", N = "AFILVWYMP", Q = "G";

        public static int[] _aa = new int[21];
        public static int[] __aa = new int[21];

        public static int[] aaInward = new int[21];
        public static int[] _aaInward = new int[21];

        public static int[] aaOutward = new int[21];
        public static int[] _aaOutward = new int[21];

        public static int[] aaDevInward = new int[21];
        public static int[] _aaDevInward = new int[21];

        public static int[] aaDevOutward = new int[21];
        public static int[] _aaDevOutward = new int[21];

        public static int[] strandSizes = new int[50];
        public static int[] _strandSizes = new int[50];
        public static int[] ZP = new int[150];
        public static int[] _ZP = new int[150];
        public static int[] ZN = new int[150];
        public static int[] _ZN = new int[150];
        public static int[] AlternatingInOutSeqLengths = new int[100];
        public static int[] _AlternatingInOutSeqLengths = new int[100];
        public static int[] examineZP = new int[125];
        public static int[] _examineZP = new int[125];
        public static int[] examineZN = new int[125];
        public static int[] _examineZN = new int[125];
        public static int numDoubleChecks = 0;

        //new data 10-3-15 Ryan
        public static int[] aap1 = new int[21];
        public static int[] aan1 = new int[21];
        public static int[] aap2 = new int[21];
        public static int[] aan2 = new int[21];
        public static int[] aap3 = new int[22];
        public static int[] aan3 = new int[22];

        public static int[] _aap1 = new int[21];
        public static int[] _aan1 = new int[21];
        public static int[] _aap2 = new int[21];
        public static int[] _aan2 = new int[21];
        public static int[] _aap3 = new int[22];
        public static int[] _aan3 = new int[22];
    }
}
