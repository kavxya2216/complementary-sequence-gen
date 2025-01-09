def complementary_seq_generator():
    should_continue = True
    while should_continue:
        print("""
            ***************************************
            *                                     *
            *              WELCOME TO             *
            *   The Complementary Sequence Gen!   *
            *                                     *
            ***************************************
            """)

        dna_sequence = input("🐝Enter the DNA sequence in FASTA format:").upper()
        dna_lenght = len(dna_sequence)
        dna_list = list(dna_sequence)
        complementary_seq = ""
        for nucleotide in dna_list:

            if nucleotide == "A":
                complementary_seq += "T"
            elif nucleotide == "T":
                complementary_seq += "A"
            elif nucleotide == "G":
                complementary_seq += "C"
            elif nucleotide == "C":
                complementary_seq += "G"


        print(f"\n🔬Your original sequence was: {dna_sequence}")
        print(f"🧬The complementary sequence is: {complementary_seq}")
        print(f"🐞Number of bases: {dna_lenght}")
        print("✨" * 10)
        restart = input("Do you want to insert another sequence? Enter Yes or No.").lower()
        if restart != "yes":
            print("\nThanks for using Complementary Sequence Generator! 🧬✨\nSee you soon!🦠")
            should_continue = False

complementary_seq_generator()


