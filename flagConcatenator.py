import os
import time

## variabel yang digunakan untuk menampung jumlah flag dan urutan flag
containerFlag = []
flagAmount = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]

## function yang digunakan untuk meminta input ari pengguna dengan maksimal input flag sebanyak 10 bagian
def inputFlag():
    print("<-----FLAG CONCATENATOR----->")
    for i in flagAmount:
        flagInput = input(f"Insert {i} flag (quit for stop): ")

        ## mengecek apakah panjang dari variable yang menyimpan pecahan flag lebih dari 10 
        if len(containerFlag) == 10: 
            print("the limit of the input flag is 10!")
            return

        ## mengecek apakah user masih ingin melanjutkan mengisi flag atau ingi lanjut ke kode berikutnya
        if flagInput.lower() == "quit":
            break
        containerFlag.append(flagInput)

## function yang digunakan jika user ingin mengedit flag yang salah
def editFlag():
    ## memberi pilihan apakah ada flag yang ingin di edit
    while True:
        want_edit = input("\nDo you want to edit any flag? (yes/no): ").lower()
        if want_edit == "no":
            break
        elif want_edit == "yes": ## jika ada flag yang ingin diedit, program menampilkan beberapa flag yang sudah diinput oleh user sebelumnya
            print("\nCurrent flags:")
            for idx, (label, flag) in enumerate(zip(flagAmount, containerFlag), 1):
                print(f"{idx}. {label} flag: {flag}")
            
            ## meminta user untuk memasukan flag mana yang ingin diedit
            try:
                choice = int(input("Enter the number of the flag you want to edit (1-10): "))
                if 1 <= choice <= 10:
                    new_flag = input(f"Insert new {flagAmount[choice-1]} flag: ")
                    containerFlag[choice-1] = new_flag
                    print("Flag updated successfully.")
                else:
                    print("Invalid number. Must be between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("Please answer with 'yes' or 'no'.")

        
# final function yang digunakan untuk menggabungkan beberapa pecahan flag menjadi satu
def concatFlag():
    print("\n<-----SEPARATED FLAG----->")
    for label, flag in zip(flagAmount, containerFlag):
        print(f"{label} flag: {flag}")
    print("\n<-----CONCATED FLAG----->")
    concatedFlag = ''.join(containerFlag)
    print(f"{concatedFlag}")


if __name__ == "__main__":
    inputFlag()
    editFlag()
    concatFlag()